import requests

from webtestauto.api.clients.base_client import BaseAPIClient


class ReqresClient(BaseAPIClient):
    def __init__(self, base_url: str, api_key: str = "reqres-free-v1"):
        """Create a client for the reqres.in users API.

        Parameters
        ----------
        base_url : str
            Root URL of the reqres deployment to test against, e.g.
            ``"https://reqres.in"``.
        api_key : str, optional
            Value sent in the ``x-api-key`` header on every request. Defaults
            to reqres's public free-tier key.
        """
        super().__init__(base_url, headers={"x-api-key": api_key})

    def list_users(self, page: int = 1) -> requests.Response:
        """List users via ``GET /api/users``.

        Parameters
        ----------
        page : int, optional
            1-indexed page of results to request. Defaults to 1.

        Returns
        -------
        requests.Response
            The raw response; on success, ``.json()["data"]`` is a list of
            user objects and ``.json()["page"]`` echoes the requested page.
        """
        return self.get("/api/users", params={"page": page})

    def get_user(self, user_id: int) -> requests.Response:
        """Fetch a single user via ``GET /api/users/{user_id}``.

        Parameters
        ----------
        user_id : int
            Id of the user to fetch.

        Returns
        -------
        requests.Response
            Status ``200`` with the user under ``.json()["data"]`` when the
            id exists, or ``404`` when it doesn't - unlike PUT/PATCH/DELETE,
            GET does validate the id.
        """
        return self.get(f"/api/users/{user_id}")

    def create_user(self, name: str, job: str) -> requests.Response:
        """Create a user via ``POST /api/users``.

        Parameters
        ----------
        name : str
            Name to set on the new user.
        job : str
            Job title to set on the new user.

        Returns
        -------
        requests.Response
            Status ``201`` with the created payload (including a generated
            ``id``) in the response body.
        """
        return self.post("/api/users", json={"name": name, "job": job})

    def update_user(self, user_id: int, name: str, job: str) -> requests.Response:
        """Replace a user via ``PUT /api/users/{user_id}``.

        Parameters
        ----------
        user_id : int
            Id of the user to update. reqres does not verify this id exists;
            it echoes the payload back with ``200`` regardless.
        name : str
            Name to set on the user.
        job : str
            Job title to set on the user.

        Returns
        -------
        requests.Response
            Status ``200`` with the updated fields echoed back in the body.
        """
        return self.put(f"/api/users/{user_id}", json={"name": name, "job": job})

    def patch_user(self, user_id: int, **fields) -> requests.Response:
        """Partially update a user via ``PATCH /api/users/{user_id}``.

        Parameters
        ----------
        user_id : int
            Id of the user to update. As with `update_user`, reqres does not
            verify this id exists; it echoes the payload back with ``200``
            regardless.
        **fields
            Field name/value pairs to update (e.g. ``name=``, ``job=``). Only
            the fields passed are sent, making this a true partial update.

        Returns
        -------
        requests.Response
            Status ``200`` with the updated fields echoed back in the body.
        """
        return self.patch(f"/api/users/{user_id}", json=fields)

    def delete_user(self, user_id: int) -> requests.Response:
        """Delete a user via ``DELETE /api/users/{user_id}``.

        Parameters
        ----------
        user_id : int
            Id of the user to delete.

        Returns
        -------
        requests.Response
            Status ``204`` with an empty body, whether or not the id existed.
        """
        return self.delete(f"/api/users/{user_id}")
