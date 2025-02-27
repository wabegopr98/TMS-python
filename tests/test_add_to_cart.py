from pages.add_to_cart_page import CartPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize(
    ("username", "password"), [
        ("standard_user", "secret_sauce")
    ]
)

def test_add_to_cart(driver, username, password):
    login = LoginPage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    add_to_cart = CartPage(driver)
    add_to_cart.move_to_item_cart()
    add_to_cart.click_add()
    add_to_cart.move_to_shop_cart()
    add_to_cart.click_button_cart()
    assert add_to_cart.find_quantity() == "1"
    add_to_cart.click_button_cart()
    assert add_to_cart.find_name() == "Sauce Labs Backpack"
    driver.quit()