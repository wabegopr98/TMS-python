from hw23.conftest import driver
from hw23.pages.login_page import LoginPage
import pytest


@pytest.mark.parametrize(
    ("username", "password"), [
        ('standard_user', 'secret_sauce'),
        ('locked_out_user', 'secret_sauce'),
        ('problem_user', 'secret_sauce'),
    ]
)

def test_good_login(driver, username, password):
    good_login = LoginPage(driver)
    good_login.open_url("https://www.saucedemo.com/")
    good_login.enter_username(username)
    good_login.enter_password(password)
    good_login.click_login()
    if username == "locked_out_user":
        assert "https://www.saucedemo.com/" == driver.current_url, "Ошибка: логин удался"
    else:
        assert "inventory" in driver.current_url, "Ошибка: логин не удался"

