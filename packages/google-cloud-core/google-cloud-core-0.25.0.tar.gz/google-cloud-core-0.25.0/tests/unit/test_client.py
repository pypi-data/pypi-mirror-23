# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import json
import unittest

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class Test_ClientFactoryMixin(unittest.TestCase):

    @staticmethod
    def _get_target_class():
        from google.cloud.client import _ClientFactoryMixin

        return _ClientFactoryMixin

    def test_virtual(self):
        klass = self._get_target_class()
        self.assertFalse('__init__' in klass.__dict__)


class TestClient(unittest.TestCase):

    @staticmethod
    def _get_target_class():
        from google.cloud.client import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_unpickleable(self):
        import pickle

        CREDENTIALS = _make_credentials()
        HTTP = object()

        client_obj = self._make_one(credentials=CREDENTIALS, _http=HTTP)
        with self.assertRaises(pickle.PicklingError):
            pickle.dumps(client_obj)

    def test_ctor_defaults(self):
        from google.cloud._testing import _Monkey
        from google.cloud import client

        CREDENTIALS = _make_credentials()
        FUNC_CALLS = []

        def mock_get_credentials():
            FUNC_CALLS.append('get_credentials')
            return CREDENTIALS

        with _Monkey(client, get_credentials=mock_get_credentials):
            client_obj = self._make_one()

        self.assertIs(client_obj._credentials, CREDENTIALS)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(FUNC_CALLS, ['get_credentials'])

    def test_ctor_explicit(self):
        CREDENTIALS = _make_credentials()
        HTTP = object()
        client_obj = self._make_one(credentials=CREDENTIALS, _http=HTTP)

        self.assertIs(client_obj._credentials, CREDENTIALS)
        self.assertIs(client_obj._http_internal, HTTP)

    def test_ctor_bad_credentials(self):
        CREDENTIALS = object()

        with self.assertRaises(ValueError):
            self._make_one(credentials=CREDENTIALS)

    def test_from_service_account_json(self):
        from google.cloud import _helpers

        klass = self._get_target_class()

        # Mock both the file opening and the credentials constructor.
        info = {'dummy': 'value', 'valid': 'json'}
        json_fi = io.StringIO(_helpers._bytes_to_unicode(json.dumps(info)))
        file_open_patch = mock.patch(
            'io.open', return_value=json_fi)
        constructor_patch = mock.patch(
            'google.oauth2.service_account.Credentials.'
            'from_service_account_info',
            return_value=_make_credentials())

        with file_open_patch as file_open:
            with constructor_patch as constructor:
                client_obj = klass.from_service_account_json(
                    mock.sentinel.filename)

        self.assertIs(
            client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        # Check that mocks were called as expected.
        file_open.assert_called_once_with(
            mock.sentinel.filename, 'r', encoding='utf-8')
        constructor.assert_called_once_with(info)

    def test_from_service_account_json_bad_args(self):
        KLASS = self._get_target_class()

        with self.assertRaises(TypeError):
            KLASS.from_service_account_json(
                mock.sentinel.filename, credentials=mock.sentinel.credentials)

    def test__http_property_existing(self):
        credentials = _make_credentials()
        http = object()
        client = self._make_one(credentials=credentials, _http=http)
        self.assertIs(client._http_internal, http)
        self.assertIs(client._http, http)

    def test__http_property_new(self):
        credentials = _make_credentials()
        client = self._make_one(credentials=credentials)
        self.assertIsNone(client._http_internal)

        patch = mock.patch('google_auth_httplib2.AuthorizedHttp',
                           return_value=mock.sentinel.http)
        with patch as mocked:
            self.assertIs(client._http, mock.sentinel.http)
            # Check the mock.
            mocked.assert_called_once_with(credentials)
            self.assertEqual(mocked.call_count, 1)
            # Make sure the cached value is used on subsequent access.
            self.assertIs(client._http_internal, mock.sentinel.http)
            self.assertIs(client._http, mock.sentinel.http)
            self.assertEqual(mocked.call_count, 1)


class TestClientWithProject(unittest.TestCase):

    @staticmethod
    def _get_target_class():
        from google.cloud.client import ClientWithProject

        return ClientWithProject

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        from google.cloud._testing import _Monkey
        from google.cloud import client

        PROJECT = 'PROJECT'
        CREDENTIALS = _make_credentials()
        FUNC_CALLS = []

        def mock_determine_proj(project):
            FUNC_CALLS.append((project, '_determine_default_project'))
            return PROJECT

        def mock_get_credentials():
            FUNC_CALLS.append('get_credentials')
            return CREDENTIALS

        with _Monkey(client, get_credentials=mock_get_credentials,
                     _determine_default_project=mock_determine_proj):
            client_obj = self._make_one()

        self.assertEqual(client_obj.project, PROJECT)
        self.assertIs(client_obj._credentials, CREDENTIALS)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(
            FUNC_CALLS,
            [(None, '_determine_default_project'), 'get_credentials'])

    def test_ctor_missing_project(self):
        from google.cloud._testing import _Monkey
        from google.cloud import client

        FUNC_CALLS = []

        def mock_determine_proj(project):
            FUNC_CALLS.append((project, '_determine_default_project'))
            return None

        with _Monkey(client, _determine_default_project=mock_determine_proj):
            self.assertRaises(EnvironmentError, self._make_one)

        self.assertEqual(FUNC_CALLS, [(None, '_determine_default_project')])

    def test_ctor_w_invalid_project(self):
        CREDENTIALS = _make_credentials()
        HTTP = object()
        with self.assertRaises(ValueError):
            self._make_one(project=object(), credentials=CREDENTIALS,
                           _http=HTTP)

    def _explicit_ctor_helper(self, project):
        import six

        CREDENTIALS = _make_credentials()
        HTTP = object()

        client_obj = self._make_one(project=project, credentials=CREDENTIALS,
                                    _http=HTTP)

        if isinstance(project, six.binary_type):
            self.assertEqual(client_obj.project, project.decode('utf-8'))
        else:
            self.assertEqual(client_obj.project, project)
        self.assertIs(client_obj._credentials, CREDENTIALS)
        self.assertIs(client_obj._http_internal, HTTP)

    def test_ctor_explicit_bytes(self):
        PROJECT = b'PROJECT'
        self._explicit_ctor_helper(PROJECT)

    def test_ctor_explicit_unicode(self):
        PROJECT = u'PROJECT'
        self._explicit_ctor_helper(PROJECT)

    def _from_service_account_json_helper(self, project=None):
        from google.cloud import _helpers

        klass = self._get_target_class()

        info = {'dummy': 'value', 'valid': 'json'}
        if project is None:
            expected_project = 'eye-d-of-project'
        else:
            expected_project = project

        info['project_id'] = expected_project
        # Mock both the file opening and the credentials constructor.
        json_fi = io.StringIO(_helpers._bytes_to_unicode(json.dumps(info)))
        file_open_patch = mock.patch(
            'io.open', return_value=json_fi)
        constructor_patch = mock.patch(
            'google.oauth2.service_account.Credentials.'
            'from_service_account_info',
            return_value=_make_credentials())

        with file_open_patch as file_open:
            with constructor_patch as constructor:
                kwargs = {}
                if project is not None:
                    kwargs['project'] = project
                client_obj = klass.from_service_account_json(
                    mock.sentinel.filename, **kwargs)

        self.assertIs(
            client_obj._credentials, constructor.return_value)
        self.assertIsNone(client_obj._http_internal)
        self.assertEqual(client_obj.project, expected_project)
        # Check that mocks were called as expected.
        file_open.assert_called_once_with(
            mock.sentinel.filename, 'r', encoding='utf-8')
        constructor.assert_called_once_with(info)

    def test_from_service_account_json(self):
        self._from_service_account_json_helper()

    def test_from_service_account_json_project_set(self):
        self._from_service_account_json_helper(project='prah-jekt')
