from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage


class LoginPage(BasePage):
    _USERNAME_INPUT = (By.ID, "username")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _FLASH_MESSAGE = (By.ID, "flash")

    def load(self) -> "LoginPage":
        self.open("/login")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        self.type_text(self._USERNAME_INPUT, username)
        self.type_text(self._PASSWORD_INPUT, password)
        self.click(self._LOGIN_BUTTON)
        return self

    def flash_message(self) -> str:
        return self.text_of(self._FLASH_MESSAGE)
