from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage


class BasicAuthPage(BasePage):
    _MESSAGE = (By.CSS_SELECTOR, ".example p")

    def load(self, username: str, password: str) -> "BasicAuthPage":
        authed_url = self.base_url.replace("https://", f"https://{username}:{password}@")
        self.driver.get(f"{authed_url}/basic_auth")
        return self

    def success_message(self) -> str:
        return self.text_of(self._MESSAGE)
