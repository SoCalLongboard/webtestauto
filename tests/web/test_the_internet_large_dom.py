import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from webtestauto.web.pages.the_internet.large_dom_page import LargeDomPage

pytestmark = [pytest.mark.web, pytest.mark.parametrize("site", ["the_internet"], indirect=True)]


def test_deeply_nested_element_is_reachable(driver, site):
    page = LargeDomPage(driver, site.base_url).load()

    assert page.no_siblings_text() == "No siblings"


def test_large_table_last_cell_has_expected_value(driver, site):
    page = LargeDomPage(driver, site.base_url).load()

    assert page.last_table_cell_text() == "50.50"


def test_missing_element_raises_timeout(driver, site):
    page = LargeDomPage(driver, site.base_url).load()

    with pytest.raises(TimeoutException):
        page.wait_for_missing((By.ID, "does-not-exist"), timeout=2)
