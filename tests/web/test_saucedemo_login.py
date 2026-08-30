import pytest

from webtestauto.web.pages.saucedemo.login_page import LoginPage

pytestmark = [pytest.mark.web, pytest.mark.parametrize("site", ["saucedemo"], indirect=True)]


def test_valid_login_shows_inventory(driver, site):
    login_page = LoginPage(driver, site.base_url).load()
    inventory_page = login_page.login(site.username, site.password)

    assert inventory_page.is_loaded()
    assert len(inventory_page.item_names()) > 0


def test_invalid_login_shows_error(driver, site):
    login_page = LoginPage(driver, site.base_url).load()
    login_page.login("locked_out_user", "wrong_password")

    assert "do not match" in login_page.error_message().lower()
