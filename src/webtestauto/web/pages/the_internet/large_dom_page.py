from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from webtestauto.web.pages.base_page import BasePage

_NO_SIBLINGS = (By.ID, "no-siblings")
_LAST_CELL = (By.CSS_SELECTOR, "#large-table tr:last-child td:last-child")


class LargeDomPage(BasePage):
    def load(self) -> "LargeDomPage":
        """Navigate to the /large page.

        Returns
        -------
        LargeDomPage
            `self`, for chaining.
        """
        self.open("/large")
        return self

    def no_siblings_text(self) -> str:
        """Read the text of the deeply nested `#no-siblings` element.

        Returns
        -------
        str
            Text of the element.
        """
        return self.text_of(_NO_SIBLINGS)

    def last_table_cell_text(self) -> str:
        """Read the text of the last cell in the large table's last row.

        Returns
        -------
        str
            Text of the cell.
        """
        return self.text_of(_LAST_CELL)

    def wait_for_missing(self, locator: tuple[str, str], timeout: float = 2) -> None:
        """Wait for `locator` to appear, expecting it never to.

        Used to assert a negative case: that a given locator is genuinely
        absent from the (very large) DOM within a bounded wait, rather than
        failing to find it for some other reason.

        Parameters
        ----------
        locator : tuple[str, str]
            A Selenium locator, e.g. ``(By.ID, "does-not-exist")``.
        timeout : float, optional
            Seconds to wait before giving up. Defaults to 2.

        Raises
        ------
        selenium.common.exceptions.TimeoutException
            If `locator` does not appear within `timeout` seconds - the
            expected outcome when asserting the element is missing.
        """
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
