from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage

_HOST_ELEMENTS = (By.TAG_NAME, "my-paragraph")


class ShadowDomPage(BasePage):
    def load(self) -> "ShadowDomPage":
        self.open("/shadowdom")
        return self

    def shadow_paragraph_text(self, index: int) -> str:
        # ShadowRoot.find_element only supports CSS_SELECTOR, unlike normal elements.
        host = self.driver.find_elements(*_HOST_ELEMENTS)[index]
        return host.shadow_root.find_element(By.CSS_SELECTOR, "p").text
