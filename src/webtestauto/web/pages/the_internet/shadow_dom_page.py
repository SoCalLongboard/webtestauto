from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage

_HOST_ELEMENTS = (By.TAG_NAME, "my-paragraph")


class ShadowDomPage(BasePage):
    def load(self) -> "ShadowDomPage":
        """Navigate to the /shadowdom page.

        Returns
        -------
        ShadowDomPage
            `self`, for chaining.
        """
        self.open("/shadowdom")
        return self

    def shadow_paragraph_text(self, index: int) -> str:
        """Read the text of a `<p>` inside one shadow host's shadow root.

        Parameters
        ----------
        index : int
            0-based index into the page's `<my-paragraph>` host elements.

        Returns
        -------
        str
            Text of the `<p>` element inside that host's open shadow root.
            Note this content is unreachable via a normal page-level query
            (e.g. `driver.find_element`), since shadow DOM content is
            encapsulated - it must be traversed through `shadow_root`.
        """
        # ShadowRoot.find_element only supports CSS_SELECTOR, unlike normal elements.
        host = self.driver.find_elements(*_HOST_ELEMENTS)[index]
        return host.shadow_root.find_element(By.CSS_SELECTOR, "p").text
