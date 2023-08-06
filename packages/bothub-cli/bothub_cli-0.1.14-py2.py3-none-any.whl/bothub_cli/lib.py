# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

import os
import sys
import json
import time
import click
import tarfile
import traceback

from six.moves import input

from bothub_client.clients import NluClientFactory

from bothub_cli import __version__
from bothub_cli import exceptions as exc
from bothub_cli.api import Api
from bothub_cli.config import Config
from bothub_cli.config import ProjectConfig
from bothub_cli.clients import ConsoleChannelClient
from bothub_cli.clients import ExternalHttpStorageClient
from bothub_cli.utils import safe_mkdir
from bothub_cli.utils import read_content_from_file
from bothub_cli.utils import get_latest_version_from_pypi
from bothub_cli.utils import cmp_versions


def make_dist_package(dist_file_path):
    '''Make dist package file of current project directory.
    Includes all files of current dir, bothub dir and tests dir.
    Dist file is compressed with tar+gzip.'''
    if os.path.isfile(dist_file_path):
        os.remove(dist_file_path)

    with tarfile.open(dist_file_path, 'w:gz') as tout:
        for fname in os.listdir('.'):
            if os.path.isfile(fname):
                tout.add(fname)
            elif os.path.isdir(fname) and fname in ['bothub', 'tests']:
                tout.add(fname)


def extract_dist_package(dist_file_path):
    '''Extract dist package file to current directory.'''
    with tarfile.open(dist_file_path, 'r:gz') as tin:
        tin.extractall()


def make_event(message):
    '''Make dummy event for test mode.'''
    data = {
        'trigger': 'cli',
        'channel': 'cli',
        'sender': {
            'id': 'localuser',
            'name': 'Local user'
        },
        'raw_data': message
    }

    if message.startswith('/location'):
        _, latitude, longitude = message.split()
        data['location'] = {
            'latitude': latitude,
            'longitude': longitude
        }
    elif message:
        data['content'] = message

    return data


def is_latest_version():
    pypi_version = get_latest_version_from_pypi()
    return (cmp_versions(__version__, pypi_version) >= 0, pypi_version)


def check_latest_version():
    try:
        is_latest, pypi_version = is_latest_version()
        if not is_latest:
            raise exc.NotLatestVersion(__version__, pypi_version)

    except exc.Timeout:
        pass


class Cli(object):
    '''A CLI class represents '''
    def __init__(self, api=None, config=None, project_config=None):
        self.api = api or Api()
        self.config = config or Config()
        self.project_config = project_config or ProjectConfig()

    def load_auth(self):
        '''Load auth token from bothub config and inject to API class'''
        self.config.load()
        self.api.load_auth(self.config)

    def get_current_project_id(self):
        self.project_config.load()
        project_id = self.project_config.get('id')
        if not project_id:
            raise exc.ImproperlyConfigured()
        return project_id

    def get_project(self, project_id):
        self.load_auth()
        return self.api.get_project(project_id)

    def authenticate(self, username, password):
        token = self.api.authenticate(username, password)
        self.config.set('auth_token', token)
        self.config.save()

    def get_project_id_with_name(self, project_name):
        self.load_auth()
        projects = self.api.list_projects()
        for p in projects:
            if p['name'] == project_name:
                return p['id']
        raise exc.ProjectNameNotFound(project_name)

    def init(self, name, description):
        self.load_auth()
        project = self.api.create_project(name, description)
        project_id = project['id']
        programming_language = 'python3'
        self.api.upload_code(project_id, programming_language)

    def deploy(self, console=None):
        self.load_auth()
        self.project_config.load()

        safe_mkdir('dist')
        dist_file_path = os.path.join('dist', 'bot.tgz')
        make_dist_package(dist_file_path)

        if console:
            console('Upload code')
        with open(dist_file_path, 'rb') as dist_file:
            dependency = read_content_from_file('requirements.txt') or 'bothub'
            project_id = self.get_current_project_id()
            self.api.upload_code(
                project_id,
                self.project_config.get('programming-language'),
                dist_file,
                dependency
            )
        if console:
            console('Deploying', nl=False)
        for _ in range(30):
            project = self.api.get_project(project_id)
            if project['status'] == 'online':
                console('.')
                return

            if console:
                console('.', nl=False)
            time.sleep(1)
        console('.')
        raise exc.DeployFailed()

    def clone(self, project_name):
        project_id = self.get_project_id_with_name(project_name)
        self.load_auth()

        response = self.api.get_code(project_id)
        code = response['code']
        code_byte = eval(code)

        with open('code.tgz', 'wb') as code_file:
            code_file.write(code_byte)

        extract_dist_package('code.tgz')
        if os.path.isfile('code.tgz'):
            os.remove('code.tgz')

    def ls(self, verbose=False):
        self.load_auth()
        projects = self.api.list_projects()
        if verbose:
            result = [[p['name'], p['status'], p['regdate']] for p in projects]
        else:
            result = [[p['name']] for p in projects]
        return result

    def rm(self, name):
        self.load_auth()
        projects = self.api.list_projects()
        _projects = [p for p in projects if p['name'] == name]
        if not _projects:
            raise exc.ProjectNameNotFound(name)
        for project in _projects:
            self.api.delete_project(project['id'])

    def add_channel(self, channel, credentials):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        self.api.add_project_channel(project_id, channel, credentials)

    def ls_channel(self, verbose=False):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        channels = self.api.get_project_channels(project_id)
        if verbose:
            result = [[c['channel'], c['credentials']] for c in channels]
        else:
            result = [[c['channel']] for c in channels]
        return result

    def rm_channel(self, channel):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        self.api.delete_project_channels(project_id, channel)

    def ls_properties(self):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        return self.api.get_project_property(project_id)

    def get_properties(self, key):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        data = self.api.get_project_property(project_id)
        return data[key]

    def set_properties(self, key, value):
        try:
            _value = json.loads(value)
        except ValueError:
            _value = value

        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        return self.api.set_project_property(project_id, key, _value)

    def rm_properties(self, key):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        self.api.delete_project_property(project_id, key)

    def test(self):
        self.load_auth()
        self.project_config.load()

        try:
            readline = __import__('readline')
            if os.path.isfile('.history'):
                readline.read_history_file('.history')
        except ImportError:
            pass

        try:
            sys.path.append('.')
            __import__('bothub.bot')
        except ImportError:
            if sys.exc_info()[-1].tb_next:
                raise
            else:
                raise exc.ModuleLoadException()

        event = {
            'sender': {
                'id': '-1'
            },
            'channel': 'console'
        }
        context = {}

        project_id = self.get_current_project_id()
        nlus = self.api.get_project_nlus(project_id)
        context['nlu'] = dict([(nlu['nlu'], nlu['credentials']) for nlu in nlus])

        mod = sys.modules['bothub.bot']
        channel_client = ConsoleChannelClient()
        storage_client = ExternalHttpStorageClient(
            self.config.get('auth_token'),
            self.get_current_project_id()
        )
        nlu_client_factory = NluClientFactory(context)
        bot = mod.Bot(
            channel_client=channel_client,
            storage_client=storage_client,
            nlu_client_factory=nlu_client_factory,
            event=event
        )

        line = input('BotHub> ')
        while line:
            try:
                event = make_event(line)
                context = {}
                bot.handle_message(event, context)
                line = input('BotHub> ')
            except EOFError:
                break
            except Exception:
                traceback.print_exc()
                line = input('BotHub> ')

        try:
            readline = __import__('readline')
            readline.write_history_file('.history')
        except ImportError:
            pass

    def add_nlu(self, nlu, credentials):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        self.api.add_project_nlu(project_id, nlu, credentials)

    def ls_nlus(self, verbose=False):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        nlus = self.api.get_project_nlus(project_id)
        if verbose:
            result = [[nlu['nlu'], nlu['credentials']] for nlu in nlus]
        else:
            result = [[nlu['nlu']] for nlu in nlus]
        return result

    def rm_nlu(self, nlu):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        self.api.delete_project_nlu(project_id, nlu)

    def logs(self):
        self.load_auth()
        self.project_config.load()
        project_id = self.get_current_project_id()
        logs = self.api.get_project_execution_logs(project_id)
        return sorted(logs, key=lambda x: x['regdate'])
