import time

from hw23.pages.add_to_cart_page import CartPage
from hw23.pages.info_buyer_page import BuyerInfo
from hw23.pages.login_page import LoginPage


def test_buy_item(driver):
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
    continue_with_item.enter_first_name()
    continue_with_item.enter_second_name()
    continue_with_item.enter_zip()
    time.sleep(3)
    continue_with_item.click_continue()
    time.sleep(3)
    continue_with_item.click_finish()
    time.sleep(3)
    assert continue_with_item.successfull_buy() == "Thank you for your order!"