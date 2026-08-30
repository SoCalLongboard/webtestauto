from selenium.webdriver.common.by import By

from webtestauto.web.pages.base_page import BasePage


class InventoryPage(BasePage):
    _INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def is_loaded(self) -> bool:
        return self.find(self._INVENTORY_LIST).is_displayed()

    def item_names(self) -> list[str]:
        self.find(self._INVENTORY_LIST)
        return [el.text for el in self.driver.find_elements(*self._ITEM_NAMES)]
