import requests

from webtestauto.api.clients.base_client import BaseAPIClient


class ReqresClient(BaseAPIClient):
    def __init__(self, base_url: str, api_key: str = "reqres-free-v1"):
        super().__init__(base_url, headers={"x-api-key": api_key})

    def list_users(self, page: int = 1) -> requests.Response:
        return self.get("/api/users", params={"page": page})

    def get_user(self, user_id: int) -> requests.Response:
        return self.get(f"/api/users/{user_id}")

    def create_user(self, name: str, job: str) -> requests.Response:
        return self.post("/api/users", json={"name": name, "job": job})

    def update_user(self, user_id: int, name: str, job: str) -> requests.Response:
        return self.put(f"/api/users/{user_id}", json={"name": name, "job": job})

    def patch_user(self, user_id: int, **fields) -> requests.Response:
        return self.patch(f"/api/users/{user_id}", json=fields)

    def delete_user(self, user_id: int) -> requests.Response:
        return self.delete(f"/api/users/{user_id}")
