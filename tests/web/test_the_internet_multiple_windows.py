import pytest
from selenium.common.exceptions import NoSuchWindowException

from webtestauto.web.pages.the_internet.windows_page import WindowsPage

pytestmark = [pytest.mark.web, pytest.mark.parametrize("site", ["the_internet"], indirect=True)]


def test_new_window_opens_with_expected_heading(driver, site):
    page = WindowsPage(driver, site.base_url).load()
    original_handle = driver.current_window_handle

    new_handle = page.open_new_window()
    assert len(driver.window_handles) == 2

    page.switch_to(new_handle)
    assert page.heading_text() == "New Window"

    driver.close()
    page.switch_to(original_handle)
    assert len(driver.window_handles) == 1


def test_switching_to_closed_window_raises(driver, site):
    page = WindowsPage(driver, site.base_url).load()
    original_handle = driver.current_window_handle

    new_handle = page.open_new_window()
    page.switch_to(new_handle)
    driver.close()
    page.switch_to(original_handle)

    with pytest.raises(NoSuchWindowException):
        page.switch_to(new_handle)
