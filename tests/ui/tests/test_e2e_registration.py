from tests.settings import url_ui, cabinet_url
import pytest
import allure
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.register_page import RegisterPage
from tests.ui.pages.task_page import CabinetPage


@pytest.mark.parametrize(
    ("name", "password"), [
        ('Jackson', 'Wisdom1'),
        ('Prohor', 'Super1'),
        ('Prohor', 'Super1')

    ]
)
@allure.story("E2E Сценарий регистрации, авторизации и выхода из ЛК")
@allure.feature("E2E Тест")
def test_reg_auth(db_connection, driver, name, password):
    with allure.step("Ввод логина пользователем"):
        login_page = LoginPage(driver)
        login_page.open_url(url_ui)
        login_page.click_register()
    with allure.step("Подключение к БД для получения пользователя там"):
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM "user" WHERE username = %s',
        (name,))
        user = cursor.fetchone()
        cursor.close()
    with allure.step("Переход к регистрации"):
        reg_page = RegisterPage(driver)
        reg_page.enter_username(name)
        reg_page.enter_password(password)
        reg_page.click_register()
        if user:
            assert reg_page.check_bad_reg() == ("Пользователь с таким "
                                                "именем уже существует")

            reg_page.back_to_log()
            assert login_page.check_url() == url_ui
            login_page.enter_username(name)
            login_page.enter_pass(password)
            login_page.click_login()
            login_page.load_info()
        else:
            assert login_page.check_good_reg_message() == ("Регистрация "
                                        "успешна! Теперь вы можете войти")
            assert login_page.check_url() == url_ui
            login_page.enter_username(name)
            login_page.enter_pass(password)
            login_page.click_login()
    with allure.step("Действия в кабинете"):
        cabinet_page = CabinetPage(driver)
        assert cabinet_page.check_good_login() == "Вы успешно вошли в систему"
        author_name = cabinet_page.check_cab_author()
        assert author_name == f"Выйти ({name})"
        assert cabinet_page.check_url() == cabinet_url
        cabinet_page.click_quit()
    with allure.step("Возврат на страницу логина"):
        assert login_page.check_url() == url_ui
        assert login_page.check_quit_message() == "Вы вышли из системы"
