from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage
from webtestauto.web.pages.saucedemo.inventory_page import InventoryPage


class LoginPage(BasePage):
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self) -> "LoginPage":
        self.open("/")
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        self.type_text(self._USERNAME_INPUT, username)
        self.type_text(self._PASSWORD_INPUT, password)
        self.click(self._LOGIN_BUTTON)
        return InventoryPage(self.driver, self.base_url)

    def error_message(self) -> str:
        return self.text_of(self._ERROR_MESSAGE)
