from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


class CabinetPage(BasePage):
    AUTHOR_CHECK = (By.CSS_SELECTOR, "[data-testid='nav-logout']")
    AUTHORIZATION_MESSAGE = (By.CSS_SELECTOR, "[data-testid='flash-message-success']")


    def check_good_login(self):
        return self.find_element(self.AUTHORIZATION_MESSAGE).text

    def check_cab_author(self):
        return self.find_element(self.AUTHOR_CHECK).text

    def check_url(self):
        return self.driver.current_url

    def click_quit(self):
        self.click_element(self.AUTHOR_CHECK)
