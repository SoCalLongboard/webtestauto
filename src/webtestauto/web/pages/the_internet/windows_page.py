from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage

_NEW_WINDOW_LINK = (By.LINK_TEXT, "Click Here")
_HEADING = (By.TAG_NAME, "h3")


class WindowsPage(BasePage):
    def load(self) -> "WindowsPage":
        self.open("/windows")
        return self

    def open_new_window(self) -> str:
        """Clicks the link that opens a new window/tab and returns its handle."""
        original_handles = set(self.driver.window_handles)
        self.click(_NEW_WINDOW_LINK)
        self.wait.until(lambda d: set(d.window_handles) - original_handles)
        new_handle = (set(self.driver.window_handles) - original_handles).pop()
        return new_handle

    def switch_to(self, handle: str) -> None:
        self.driver.switch_to.window(handle)

    def heading_text(self) -> str:
        return self.text_of(_HEADING)
