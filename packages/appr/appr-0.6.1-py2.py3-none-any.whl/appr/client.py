import re
import json
import logging
import requests
from requests.utils import urlparse
import appr
from appr.discovery import ishosted, discover_sources
from appr.auth import ApprAuth
from appr.config import ApprConfig

logger = logging.getLogger(__name__)
DEFAULT_REGISTRY = 'http://localhost:5000'
DEFAULT_PREFIX = "/cnr"


class ApprClient(object):
    def __init__(self, endpoint=DEFAULT_REGISTRY, auth=None, config=None, insecure=False):
        if not auth:
            auth = ApprAuth()
        if not config:
            config = ApprConfig()
        self.auth = auth
        self.config = config
        self.endpoint = self._configure_endpoint(endpoint, insecure)
        self.host = self.endpoint.geturl()
        self._headers = {
            'Content-Type': 'application/json',
            'User-Agent': "apprpy-cli/%s" % appr.__version__
        }

    def _url(self, path):
        return self.endpoint.geturl() + path

    def auth_token(self):
        """ return the Authorization bearer """
        return self.auth.token(self.host)

    def _configure_endpoint(self, endpoint, insecure):
        if endpoint is None:
            endpoint = DEFAULT_REGISTRY
        alias = self.config.get_registry_alias(endpoint)
        if alias:
            endpoint = alias
        if not re.match("https?://", endpoint):
            if insecure or str.startswith(endpoint, "localhost"):
                scheme = "http://"
            else:
                scheme = "https://"
            endpoint = scheme + endpoint
        return urlparse(endpoint + DEFAULT_PREFIX)

    @property
    def headers(self):
        token = self.auth_token()
        headers = {}
        headers.update(self._headers)
        if token is not None:
            headers['Authorization'] = token
        return headers

    def version(self):
        path = "/version"
        resp = requests.get(self._url(path), headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def show_package(self, package, version, media_type=None):
        path = "/api/v1/packages/%s" % (package)
        if version and version != 'default':
            path = path + "/%s" % version
        params = {}
        if media_type:
            params["media_type"] = media_type
        resp = requests.get(self._url(path), params=params, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def _get_pull_url(self, package, version_parts, media_type):
        if media_type is None:
            raise ValueError("media-type is not set")

        organization, name = package.split("/")
        if version_parts['key'] == "digest":
            digest = version_parts['value']
            url = "/api/v1/packages/%s/%s/blobs/sha256/%s" % (organization, name, digest)
        elif version_parts['key'] == "channel":
            chan_name = version_parts['value']
            channel = self.show_channels(package, chan_name)
            version = channel['current']
            url = "/api/v1/packages/%s/%s/%s/%s/pull" % (organization, name, version, media_type)
        elif version_parts['key'] == "version":
            version = version_parts['value']
            url = "/api/v1/packages/%s/%s/%s/%s/pull" % (organization, name, version, media_type)
        else:
            url = "/api/v1/packages/%s/%s/%s/%s/pull" % (organization, name,
                                                         version_parts['value'], media_type)
        return url

    def _pull_path(self, name, version_parts, media_type):
        if ishosted(name):
            sources = discover_sources(name, version_parts['value'], media_type)
            path = sources[0]
        else:
            path = self._url(self._get_pull_url(name, version_parts, media_type))
        return path

    def pull(self, name, version_parts, media_type):
        path = self._pull_path(name, version_parts, media_type)
        resp = requests.get(path, headers=self.headers)
        resp.raise_for_status()
        return resp.content

    def pull_json(self, name, version_parts, media_type):
        path = self._pull_path(name, version_parts, media_type)
        resp = requests.get(path, params={'format': 'json'}, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def list_packages(self, params):
        path = "/api/v1/packages"
        resp = requests.get(self._url(path), params=params, headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def push(self, name, body, force=False):
        organization, pname = name.split("/")
        body['name'] = pname
        body['organization'] = organization
        body['package'] = name
        path = "/api/v1/packages/%s/%s" % (organization, pname)
        resp = requests.post(
            self._url(path), params={"force": str(force).lower()}, data=json.dumps(body),
            headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def delete_package(self, name, version, media_type):
        organization, name = name.split("/")
        path = "/api/v1/packages/%s/%s/%s/%s" % (organization, name, version, media_type)
        resp = requests.delete(self._url(path), headers=self.headers)
        resp.raise_for_status()
        return resp.json()

    def _crud_channel(self, name, channel='', action='get'):
        if channel is None:
            channel = ''
        path = "/api/v1/packages/%s/channels/%s" % (name, channel)
        resp = getattr(requests, action)(self._url(path), params={}, headers=self.headers)
        if channel == '' and resp.status_code == 404:
            return []
        resp.raise_for_status()

        return resp.json()

    def show_channels(self, name, channel=None):
        return self._crud_channel(name, channel)

    def create_channel(self, name, channel):
        return self._crud_channel(name, channel, 'post')

    def delete_channel(self, name, channel):
        return self._crud_channel(name, channel, 'delete')

    def create_channel_release(self, name, channel, release):
        path = "%s/%s" % (channel, release)
        return self._crud_channel(name, path, 'post')

    def delete_channel_release(self, name, channel, release):
        path = "%s/%s" % (channel, release)
        return self._crud_channel(name, path, 'delete')

    def login(self, username, password):
        path = "/api/v1/users/login"
        resp = requests.post(
            self._url(path), data=json.dumps({
                "user": {
                    "username": username,
                    "password": password
                }
            }), headers=self.headers)
        resp.raise_for_status()
        result = resp.json()
        self.auth.add_token(self.host, result['token'])
        return result

    def signup(self, username, password, password_confirmation, email):
        path = "/api/v1/users"
        resp = requests.post(
            self._url(path), data=json.dumps({
                "user": {
                    "username": username,
                    "password": password,
                    "password_confirmation": password_confirmation,
                    "email": email
                }
            }), headers=self.headers)
        resp.raise_for_status()
        result = resp.json()
        self.auth.add_token(self.host, result['token'])
        return result
