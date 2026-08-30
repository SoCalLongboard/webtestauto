"""Environment-driven settings shared across the test suite.

Values here are defaults; pytest CLI options (see tests/conftest.py) take
precedence when explicitly passed.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, slots=True)
class Settings:
    browser: str = os.getenv("BROWSER", "chrome")
    headless: bool = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")
    grid_url: str | None = os.getenv("GRID_URL") or None
    default_site: str = os.getenv("SITE", "saucedemo")


settings = Settings()
