import pytest

from webtestauto.web.pages.the_internet.login_page import LoginPage

pytestmark = [pytest.mark.web, pytest.mark.parametrize("site", ["the_internet"], indirect=True)]


def test_valid_login_shows_success_message(driver, site):
    login_page = LoginPage(driver, site.base_url).load()
    login_page.login(site.username, site.password)

    assert "you logged into a secure area" in login_page.flash_message().lower()


def test_invalid_login_shows_error_message(driver, site):
    login_page = LoginPage(driver, site.base_url).load()
    login_page.login("invalid_user", "invalid_password")

    assert "invalid" in login_page.flash_message().lower()
