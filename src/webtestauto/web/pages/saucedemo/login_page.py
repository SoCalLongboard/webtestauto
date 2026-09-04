from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage
from webtestauto.web.pages.saucedemo.inventory_page import InventoryPage


class LoginPage(BasePage):
    _USERNAME_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self) -> "LoginPage":
        """Navigate to the saucedemo login page.

        Returns
        -------
        LoginPage
            `self`, for chaining (e.g. ``LoginPage(driver, url).load()``).
        """
        self.open("/")
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        """Fill the login form and submit it.

        Parameters
        ----------
        username : str
            Value to enter in the username field.
        password : str
            Value to enter in the password field.

        Returns
        -------
        InventoryPage
            A page object for the page navigated to on submit. On success
            this is the inventory listing; on failure it's still the login
            page underneath, so callers checking for an error should read
            `error_message` from the *original* `LoginPage` instance, not
            this return value.
        """
        self.type_text(self._USERNAME_INPUT, username)
        self.type_text(self._PASSWORD_INPUT, password)
        self.click(self._LOGIN_BUTTON)
        return InventoryPage(self.driver, self.base_url)

    def error_message(self) -> str:
        """Read the inline validation error shown after a failed login.

        Returns
        -------
        str
            Text of the error banner element.
        """
        return self.text_of(self._ERROR_MESSAGE)
