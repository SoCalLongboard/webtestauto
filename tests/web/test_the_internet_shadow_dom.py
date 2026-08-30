import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from webtestauto.web.pages.the_internet.shadow_dom_page import ShadowDomPage

pytestmark = [pytest.mark.web, pytest.mark.parametrize("site", ["the_internet"], indirect=True)]


def test_shadow_root_paragraphs_are_accessible(driver, site):
    page = ShadowDomPage(driver, site.base_url).load()

    assert "different text" in page.shadow_paragraph_text(0).lower()
    assert "in a list" in page.shadow_paragraph_text(1).lower()


def test_shadow_content_not_reachable_from_page_level_query(driver, site):
    ShadowDomPage(driver, site.base_url).load()

    with pytest.raises(NoSuchElementException):
        driver.find_element(By.TAG_NAME, "p")
