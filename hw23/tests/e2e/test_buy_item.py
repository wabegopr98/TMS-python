import time
import pytest

from hw23.pages.add_to_cart_page import CartPage
from hw23.pages.info_buyer_page import BuyerInfo
from hw23.pages.login_page import LoginPage


@pytest.mark.parametrize(
    ("first_name", "second_name", "zip"), [
        ("Sergey", "Ivanov", "123456"),
        ("Andrey", "Vanyushov", "987654"),
        ("Anastasiya", "Korovina", "192837"),
    ]
)
def test_buy_item(driver,first_name, second_name, zip):
    good_login = LoginPage(driver)
    good_login.open_url("https://www.saucedemo.com/")
    good_login.enter_username("standard_user")
    good_login.enter_password("secret_sauce")
    good_login.click_login()


    my_item = CartPage(driver)
    my_item.move_to_item_cart()
    my_item.click_add()
    my_item.click_button_cart()
    time.sleep(3)
    my_item.click_checkout()
    time.sleep(3)


    continue_with_item = BuyerInfo(driver)
    continue_with_item.enter_first_name(first_name)
    continue_with_item.enter_second_name(second_name)
    continue_with_item.enter_zip(zip)
    time.sleep(3)
    continue_with_item.click_continue()
    time.sleep(3)
    continue_with_item.click_finish()
    time.sleep(3)
    assert "checkout-complete" in driver.current_url