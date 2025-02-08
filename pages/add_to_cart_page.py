from selenium.webdriver import ActionChains

from conftest import driver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):

    ITEM_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    BUTTON_CART = (By.ID, "shopping_cart_container")
    CHECK_ITEM = (By.CSS_SELECTOR, "[data-test=inventory-item-name]")
    QUANTITY_ITEM = (By.CLASS_NAME, "shopping_cart_badge")

    def move_to_item_cart(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(self.ITEM_CART)).perform()

    def move_to_shop_cart(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element(self.BUTTON_CART))

    def click_add(self):
        self.click_element(self.ITEM_CART)

    def click_button_cart(self):
        self.click_element(self.BUTTON_CART)

    def find_quantity(self):
       return self.find_element(self.QUANTITY_ITEM).text

    def find_name(self):
        return self.find_element(self.CHECK_ITEM).text