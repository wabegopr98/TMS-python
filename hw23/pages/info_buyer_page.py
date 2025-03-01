from selenium.webdriver.common.by import By

from hw23.pages.base_page import BasePage


class BuyerInfo(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESSFULL_BUY = (By.CLASS_NAME, "complete-header")

    def enter_first_name(self, first_name):
        self.enter_text(self.FIRST_NAME, first_name)

    def enter_second_name(self, second_name):
        self.enter_text(self.LAST_NAME, second_name)

    def enter_zip(self, zip):
        self.enter_text(self.ZIP, zip)

    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)

    def click_finish(self):
        self.click_element(self.FINISH_BUTTON)

    def successfull_buy(self):
        return self.find_element(self.SUCCESSFULL_BUY).text