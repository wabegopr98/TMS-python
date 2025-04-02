from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


class RegisterPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASS_INPUT = (By.ID, "password")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[data-testid='register-button']")
    BAD_REGISTRATION = (By.CSS_SELECTOR, "[data-testid='flash-message-danger']")
    ALREADY_REG = (By.CSS_SELECTOR, "[data-testid='login-link']")


    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASS_INPUT, password)

    def click_register(self):
        self.click_element(self.REGISTER_BUTTON)

    def check_bad_reg(self):
        return self.find_element(self.BAD_REGISTRATION).text

    def back_to_log(self):
        self.click_element(self.ALREADY_REG)
