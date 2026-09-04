from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage


class LoginPage(BasePage):
    _USERNAME_INPUT = (By.ID, "username")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _FLASH_MESSAGE = (By.ID, "flash")

    def load(self) -> "LoginPage":
        """Navigate to the /login page.

        Returns
        -------
        LoginPage
            `self`, for chaining.
        """
        self.open("/login")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        """Fill the login form and submit it.

        Parameters
        ----------
        username : str
            Value to enter in the username field.
        password : str
            Value to enter in the password field.

        Returns
        -------
        LoginPage
            `self`; unlike saucedemo, this site's page doesn't navigate away
            on success, so the flash message can be read from the same
            instance via `flash_message`.
        """
        self.type_text(self._USERNAME_INPUT, username)
        self.type_text(self._PASSWORD_INPUT, password)
        self.click(self._LOGIN_BUTTON)
        return self

    def flash_message(self) -> str:
        """Read the flash message shown after a login attempt.

        Returns
        -------
        str
            Text of the flash message element, for either a success or
            failure outcome.
        """
        return self.text_of(self._FLASH_MESSAGE)
