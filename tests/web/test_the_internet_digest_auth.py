import pytest

from webtestauto.api.clients.the_internet_client import TheInternetAuthClient
from webtestauto.web.pages.the_internet.digest_auth_page import DigestAuthPage

pytestmark = pytest.mark.parametrize("site", ["the_internet"], indirect=True)

_USERNAME = "admin"
_PASSWORD = "admin"


@pytest.mark.web
def test_valid_credentials_shows_congratulations(driver, site):
    page = DigestAuthPage(driver, site.base_url).load(_USERNAME, _PASSWORD)

    assert "congratulations" in page.success_message().lower()


@pytest.mark.api
def test_invalid_credentials_returns_401(site):
    client = TheInternetAuthClient(site.base_url)

    response = client.digest_auth("wrong", "wrong")

    assert response.status_code == 401
