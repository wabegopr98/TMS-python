import time
from hw23.pages.login_page import LoginPage



def test_empty_login(driver):
    bad_login = LoginPage(driver)
    bad_login.open_url("https://www.saucedemo.com/")
    time.sleep(10)
    bad_login.click_login()
    time.sleep(5)
    assert bad_login.displayed_error()
    assert bad_login.get_error_message() == "Epic sadface: Username is required"
