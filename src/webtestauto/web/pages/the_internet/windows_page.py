from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage

_NEW_WINDOW_LINK = (By.LINK_TEXT, "Click Here")
_HEADING = (By.TAG_NAME, "h3")


class WindowsPage(BasePage):
    def load(self) -> "WindowsPage":
        """Navigate to the /windows page.

        Returns
        -------
        WindowsPage
            `self`, for chaining.
        """
        self.open("/windows")
        return self

    def open_new_window(self) -> str:
        """Click the link that opens a new browser window/tab.

        Blocks until a new window handle actually appears, so callers don't
        need their own wait/poll logic before switching to it.

        Returns
        -------
        str
            The Selenium window handle of the newly opened window. Note the
            driver's focus does not switch automatically; pass this to
            `switch_to` to interact with the new window.
        """
        original_handles = set(self.driver.window_handles)
        self.click(_NEW_WINDOW_LINK)
        self.wait.until(lambda d: set(d.window_handles) - original_handles)
        new_handle = (set(self.driver.window_handles) - original_handles).pop()
        return new_handle

    def switch_to(self, handle: str) -> None:
        """Switch the driver's focus to a specific window.

        Parameters
        ----------
        handle : str
            A window handle, typically obtained from `open_new_window` or
            `driver.current_window_handle`.

        Raises
        ------
        selenium.common.exceptions.NoSuchWindowException
            If `handle` refers to a window that has since been closed.
        """
        self.driver.switch_to.window(handle)

    def heading_text(self) -> str:
        """Read the `<h3>` heading of the currently focused window.

        Returns
        -------
        str
            Text of the heading element.
        """
        return self.text_of(_HEADING)
