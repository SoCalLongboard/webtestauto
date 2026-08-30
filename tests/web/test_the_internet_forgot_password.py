import pytest

from webtestauto.web.pages.the_internet.forgot_password_page import ForgotPasswordPage

pytestmark = [pytest.mark.web, pytest.mark.parametrize("site", ["the_internet"], indirect=True)]


def test_submitting_email_returns_internal_server_error(driver, site):
    """Documents a live defect: /forgot_password 500s on submission (verified via
    curl and a real browser session, reproducible 3/3), rather than showing the
    confirmation message the page implies. Revisit this test if the site is fixed.
    """
    page = ForgotPasswordPage(driver, site.base_url).load()
    page.request_reset("test@example.com")

    assert "internal server error" in page.submission_result_text().lower()
