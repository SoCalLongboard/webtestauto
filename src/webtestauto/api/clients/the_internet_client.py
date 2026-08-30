import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from webtestauto.api.clients.base_client import BaseAPIClient


class TheInternetAuthClient(BaseAPIClient):
    def basic_auth(self, username: str, password: str) -> requests.Response:
        return self.get("/basic_auth", auth=HTTPBasicAuth(username, password))

    def digest_auth(self, username: str, password: str) -> requests.Response:
        return self.get("/digest_auth", auth=HTTPDigestAuth(username, password))
