from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    _EMAIL_INPUT = (By.ID, "email")
    _SUBMIT_BUTTON = (By.ID, "form_submit")
    _BODY = (By.TAG_NAME, "body")

    def load(self) -> "ForgotPasswordPage":
        self.open("/forgot_password")
        return self

    def request_reset(self, email: str) -> "ForgotPasswordPage":
        self.type_text(self._EMAIL_INPUT, email)
        self.click(self._SUBMIT_BUTTON)
        return self

    def submission_result_text(self) -> str:
        """Text of the page shown after submitting.

        As of this writing, the-internet.herokuapp.com/forgot_password returns a
        genuine HTTP 500 on every submission (reproduced via curl and a live
        browser session) rather than a confirmation message. This method reads
        whatever the site actually renders, so the test documents real behavior.
        """
        return self.text_of(self._BODY)
