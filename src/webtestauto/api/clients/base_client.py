"""Thin requests.Session wrapper shared by all per-site API clients."""

import requests


class BaseAPIClient:
    def __init__(self, base_url: str, headers: dict[str, str] | None = None):
        """Create a client bound to a single base URL.

        Parameters
        ----------
        base_url : str
            Root URL every request is issued against, e.g. ``"https://reqres.in"``.
            A trailing slash, if present, is stripped.
        headers : dict[str, str] or None, optional
            Headers to attach to every request made through the underlying
            `requests.Session` (e.g. an API key). Defaults to no extra headers.
        """
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)

    def get(self, path: str, **kwargs) -> requests.Response:
        return self.session.get(f"{self.base_url}{path}", **kwargs)

    def post(self, path: str, **kwargs) -> requests.Response:
        return self.session.post(f"{self.base_url}{path}", **kwargs)

    def put(self, path: str, **kwargs) -> requests.Response:
        return self.session.put(f"{self.base_url}{path}", **kwargs)

    def patch(self, path: str, **kwargs) -> requests.Response:
        return self.session.patch(f"{self.base_url}{path}", **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self.session.delete(f"{self.base_url}{path}", **kwargs)
