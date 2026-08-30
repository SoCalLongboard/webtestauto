from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webtestauto.web.pages.base_page import BasePage

_NO_SIBLINGS = (By.ID, "no-siblings")
_LAST_CELL = (By.CSS_SELECTOR, "#large-table tr:last-child td:last-child")


class LargeDomPage(BasePage):
    def load(self) -> "LargeDomPage":
        self.open("/large")
        return self

    def no_siblings_text(self) -> str:
        return self.text_of(_NO_SIBLINGS)

    def last_table_cell_text(self) -> str:
        return self.text_of(_LAST_CELL)

    def wait_for_missing(self, locator: tuple[str, str], timeout: float = 2) -> None:
        """Waits for `locator` to appear; raises TimeoutException if it never does."""
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
