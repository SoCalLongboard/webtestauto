# webtestauto

A demonstration framework for web UI and API test automation in Python, built to be
extended to any number of target sites without changing framework code.

- **Python 3.14**, dependency management via [uv](https://docs.astral.sh/uv/)
- **pytest** as the single test runner for both web and API suites
- **Selenium 4** for web UI automation (Page Object Model), local or via a Selenium Grid
- **requests** for API automation

## Project layout

```
config/                     # site registry + env-driven settings (framework-level, not test code)
src/webtestauto/
  web/
    driver_factory.py       # builds local or remote (Grid) WebDriver
    pages/                  # Page Object Model, one subpackage per site
  api/
    clients/                # requests.Session-based API clients, one per site
tests/
  conftest.py                # CLI options (--browser/--headless/--grid-url/--site) + fixtures
  web/                        # Selenium tests, marked @pytest.mark.web
  api/                        # requests tests, marked @pytest.mark.api
```

## Adding a new target site

1. Add an entry to `SITE_REGISTRY` in [config/sites.py](config/sites.py).
2. For web: add a `pages/<site>/` subpackage with page objects extending `BasePage`.
3. For API: add a `clients/<site>_client.py` extending `BaseAPIClient`.
4. Add tests under `tests/web/` or `tests/api/`, parametrizing the `site` fixture with your new
   site key (see existing tests for the pattern).

No other framework code needs to change — everything else reads the site key at test time.

## API verb coverage

`tests/api/test_reqres_users.py` exercises every HTTP verb the reqres.in `/api/users` resource
supports, each with a positive case and a negative case where reqres' behavior meaningfully
differs:

| Verb   | Positive                          | Negative                                                              |
|--------|------------------------------------|-------------------------------------------------------------------------|
| GET    | list users, fetch by id           | unknown id → `404`                                                      |
| POST   | create user → `201`               | —                                                                        |
| PUT    | update user → `200`               | unknown id still → `200` (reqres doesn't validate ids on PUT)           |
| PATCH  | partial update user → `200`       | unknown id still → `200` (reqres doesn't validate ids on PATCH)         |
| DELETE | delete user → `204`               | —                                                                        |

Only GET enforces the id lookup; PUT/PATCH/DELETE echo back a success response regardless of
whether the id exists, which the negative-path tests assert directly rather than assuming a
`404` that reqres doesn't return.

## Setup

```bash
uv sync
cp .env.example .env   # optional; CLI flags below override these values
```

## Running tests

```bash
# Everything
uv run pytest

# Just API tests
uv run pytest -m api

# Just web tests, headless Chrome
uv run pytest -m web --headless

# Web tests against Firefox
uv run pytest -m web --browser firefox

# Web tests against a running Selenium Grid instead of a local browser
uv run pytest -m web --grid-url http://localhost:4444/wd/hub

# Parallel run with an HTML report
uv run pytest --html=report.html --self-contained-html -n auto
```

CLI options (`--browser`, `--headless`/`--no-headless`, `--grid-url`, `--site`) default to the
values in `.env`/environment variables (see `config/settings.py`) and can be overridden per
invocation.

### Running headed (non-headless)

Headed runs need a real display. On a machine with a desktop, `--no-headless` alone is enough.
On a headless Linux host (a server, container, or CI runner) with no display attached, install
[Xvfb](https://www.x.org/releases/X11R7.7/doc/man/man1/Xvfb.1.xhtml) and wrap the command with
`xvfb-run`, which creates a throwaway virtual display for the duration of the run:

```bash
xvfb-run -a uv run pytest -m web --no-headless
```

## CI

Both `.github/workflows/ci.yml` (GitHub Actions) and `.gitlab-ci.yml` (GitLab CI) run the same
`uv sync` → API tests → headless web tests → full parallel run with HTML report pipeline.
