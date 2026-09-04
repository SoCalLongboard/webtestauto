from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage


class BasicAuthPage(BasePage):
    _MESSAGE = (By.CSS_SELECTOR, ".example p")

    def load(self, username: str, password: str) -> "BasicAuthPage":
        """Navigate to /basic_auth with credentials embedded in the URL.

        Selenium has no API for answering an HTTP Basic Auth browser prompt,
        so this authenticates the way plain HTTP clients do: via
        ``https://user:pass@host/...`` userinfo in the URL.

        Parameters
        ----------
        username : str
            Basic auth username.
        password : str
            Basic auth password.

        Returns
        -------
        BasicAuthPage
            `self`, for chaining.
        """
        authed_url = self.base_url.replace("https://", f"https://{username}:{password}@")
        self.driver.get(f"{authed_url}/basic_auth")
        return self

    def success_message(self) -> str:
        """Read the congratulations message shown after successful auth.

        Returns
        -------
        str
            Text of the message element.
        """
        return self.text_of(self._MESSAGE)
