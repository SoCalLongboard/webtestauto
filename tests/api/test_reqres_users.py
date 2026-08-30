import pytest

from webtestauto.api.clients.reqres_client import ReqresClient

pytestmark = [pytest.mark.api, pytest.mark.parametrize("site", ["reqres"], indirect=True)]


@pytest.fixture
def client(site):
    return ReqresClient(site.base_url)


def test_list_users_returns_page_of_results(client):
    response = client.list_users(page=2)

    assert response.status_code == 200
    body = response.json()
    assert body["page"] == 2
    assert len(body["data"]) > 0


def test_get_single_user_returns_matching_id(client):
    response = client.get_user(2)

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2


def test_get_unknown_user_returns_404(client):
    response = client.get_user(23)

    assert response.status_code == 404


def test_create_user_returns_created_payload(client):
    response = client.create_user(name="Morpheus", job="Leader")

    assert response.status_code == 201
    body = response.json()
    assert body["name"] == "Morpheus"
    assert body["job"] == "Leader"
    assert "id" in body


def test_update_user_returns_updated_payload(client):
    response = client.update_user(2, name="Neo", job="The One")

    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Neo"
    assert body["job"] == "The One"


def test_delete_user_returns_no_content(client):
    response = client.delete_user(2)

    assert response.status_code == 204
