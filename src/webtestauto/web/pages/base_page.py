"""Common Selenium 4 wait/interaction helpers shared by all page objects."""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 10


class BasePage:
    def __init__(self, driver: WebDriver, base_url: str, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path: str = "/") -> None:
        self.driver.get(f"{self.base_url}{path}")

    def find(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator: tuple[str, str], text: str) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def text_of(self, locator: tuple[str, str]) -> str:
        return self.find(locator).text

    @property
    def title(self) -> str:
        return self.driver.title
