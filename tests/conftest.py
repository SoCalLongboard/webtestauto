"""Shared fixtures and CLI options for the whole suite.

Run selection examples:
    uv run pytest -m api
    uv run pytest -m web --browser firefox --headless
    xvfb-run -a uv run pytest -m web --no-headless   # headed, via a virtual display (see README)
    uv run pytest -m web --grid-url http://localhost:4444/wd/hub
"""

import pytest

from config.settings import settings
from config.sites import SiteConfig, get_site
from webtestauto.web.driver_factory import build_driver


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--browser", default=settings.browser, help="chrome | firefox")
    parser.addoption(
        "--headless",
        dest="headless",
        action="store_true",
        default=settings.headless,
        help="Run the browser headlessly (default: on, or via HEADLESS env var)",
    )
    parser.addoption(
        "--no-headless",
        dest="headless",
        action="store_false",
        help="Run the browser headed; needs a real display, or run under `xvfb-run` (see README)",
    )
    parser.addoption(
        "--grid-url",
        default=settings.grid_url,
        help="Selenium Grid / Remote WebDriver URL, e.g. http://localhost:4444/wd/hub",
    )
    parser.addoption(
        "--site",
        default=settings.default_site,
        help="Default site key from config/sites.py (overridable per-test via fixtures)",
    )


@pytest.fixture
def browser_name(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--browser")


@pytest.fixture
def headless(request: pytest.FixtureRequest) -> bool:
    return request.config.getoption("--headless")


@pytest.fixture
def grid_url(request: pytest.FixtureRequest) -> str | None:
    return request.config.getoption("--grid-url")


@pytest.fixture
def driver(browser_name: str, headless: bool, grid_url: str | None):
    drv = build_driver(browser=browser_name, headless=headless, grid_url=grid_url)
    yield drv
    drv.quit()


@pytest.fixture
def site(request: pytest.FixtureRequest) -> SiteConfig:
    """Resolves the active site: test-level override (via indirect param) or --site CLI default."""
    key = getattr(request, "param", None) or request.config.getoption("--site")
    return get_site(key)
