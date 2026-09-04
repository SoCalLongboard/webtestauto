import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from webtestauto.api.clients.base_client import BaseAPIClient


class TheInternetAuthClient(BaseAPIClient):
    def basic_auth(self, username: str, password: str) -> requests.Response:
        """Hit ``GET /basic_auth`` with HTTP Basic credentials.

        Parameters
        ----------
        username : str
            Username to authenticate with.
        password : str
            Password to authenticate with.

        Returns
        -------
        requests.Response
            Status ``200`` for the fixed valid credentials (``admin``/``admin``),
            or ``401`` with an empty body for any other credentials.
        """
        return self.get("/basic_auth", auth=HTTPBasicAuth(username, password))

    def digest_auth(self, username: str, password: str) -> requests.Response:
        """Hit ``GET /digest_auth`` with HTTP Digest credentials.

        Parameters
        ----------
        username : str
            Username to authenticate with.
        password : str
            Password to authenticate with.

        Returns
        -------
        requests.Response
            Status ``200`` for the fixed valid credentials (``admin``/``admin``),
            or ``401`` with an empty body for any other credentials.
        """
        return self.get("/digest_auth", auth=HTTPDigestAuth(username, password))
