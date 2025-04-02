from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage

class LoginPage(BasePage):
        LOGIN_USERNAME = (By.CSS_SELECTOR, "[data-testid='username-input']")
        LOGIN_PASS = (By.CSS_SELECTOR, "[data-testid='password-input']")
        LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-testid='login-button']")
        REDIRECT_REGISTER = (By.CSS_SELECTOR, "[data-testid='register-link']")
        SUCCESSFULL_REGISTRATION = (By.CSS_SELECTOR, "[data-testid='flash-message-success']")
        QUIT_MESSAGE = (By.CSS_SELECTOR, "[data-testid='flash-message-info']")
        # Регистрация успешна! Теперь вы можете войти


        def enter_username(self, username):
            self.enter_text(self.LOGIN_USERNAME, username)

        def enter_pass(self, password):
            self.enter_text(self.LOGIN_PASS, password)

        def click_login(self):
            self.click_element(self.LOGIN_BUTTON)

        def click_register(self):
            self.click_element(self.REDIRECT_REGISTER)

        def check_good_reg_message(self):
            return self.find_element(self.SUCCESSFULL_REGISTRATION).text

        def check_quit_message(self):
            return self.find_element(self.QUIT_MESSAGE).text

        def check_url(self):
            return self.driver.current_url
