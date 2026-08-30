"""Registry of target sites the framework can run tests against.

Add a new entry here to point the framework at another web or API target —
no other framework code needs to change.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SiteConfig:
    key: str
    base_url: str
    username: str | None = None
    password: str | None = None


SITE_REGISTRY: dict[str, SiteConfig] = {
    "saucedemo": SiteConfig(
        key="saucedemo",
        base_url="https://www.saucedemo.com",
        username="standard_user",
        password="secret_sauce",
    ),
    "the_internet": SiteConfig(
        key="the_internet",
        base_url="https://the-internet.herokuapp.com",
        username="tomsmith",
        password="SuperSecretPassword!",
    ),
    "reqres": SiteConfig(
        key="reqres",
        base_url="https://reqres.in",
    ),
}


def get_site(key: str) -> SiteConfig:
    try:
        return SITE_REGISTRY[key]
    except KeyError as exc:
        known = ", ".join(sorted(SITE_REGISTRY))
        raise ValueError(f"Unknown site {key!r}. Known sites: {known}") from exc
