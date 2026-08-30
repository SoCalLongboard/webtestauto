"""Builds a Selenium 4 WebDriver, local or remote (Selenium Grid)."""

import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

_OPTIONS_BY_BROWSER = {
    "chrome": ChromeOptions,
    "firefox": FirefoxOptions,
}

# Ubuntu's /usr/bin/firefox is a shell-script stub that re-execs the snap's
# sandboxed launcher; geckodriver rejects it as "not a Firefox executable".
# Point at the real ELF binary the snap ships when that stub is in play.
_UBUNTU_SNAP_FIREFOX_BINARY = "/snap/firefox/current/usr/lib/firefox/firefox"


def _is_ubuntu_snap_firefox_stub() -> bool:
    path = shutil.which("firefox")
    if not path:
        return False
    with open(path, "rb") as f:
        return f.read(2) == b"#!"


def build_driver(
    browser: str = "chrome",
    headless: bool = True,
    grid_url: str | None = None,
) -> WebDriver:
    browser = browser.lower()
    if browser not in _OPTIONS_BY_BROWSER:
        known = ", ".join(sorted(_OPTIONS_BY_BROWSER))
        raise ValueError(f"Unsupported browser {browser!r}. Known browsers: {known}")

    options = _OPTIONS_BY_BROWSER[browser]()
    if headless:
        options.add_argument("--headless=new" if browser == "chrome" else "-headless")
    if browser == "chrome":
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    if browser == "firefox" and not grid_url and _is_ubuntu_snap_firefox_stub():
        options.binary_location = _UBUNTU_SNAP_FIREFOX_BINARY

    if grid_url:
        return webdriver.Remote(command_executor=grid_url, options=options)

    driver_cls = getattr(webdriver, browser.capitalize())
    return driver_cls(options=options)
