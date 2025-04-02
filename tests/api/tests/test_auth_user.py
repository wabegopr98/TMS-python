import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.register_endpoint import RegisterUser

@pytest.mark.parametrize(
    ("payload"), [
        ({"username":"Paravoz", "password":"password", "valid": True, "not_clear": True}), #existing user and pass
        ({"username":"Zip",  "password":"password123", "valid": True, "not_clear": True}), # not-existing pass
        ({"username":"Wip",  "password":"password3", "valid": False, "not_clear": False}), #not-existing user
        ({"username":"Zlatan",  "password":"Ibra", "valid": False, "not_clear": False}) #not-existing user and pass
    ]
)

@allure.story("Сценарий: Авторизация пользователя")


def test_auth_user(payload, db_connection):
    with allure.step("Авторизация пользователя с соединением с БД "):
        try:
            cursor = db_connection.cursor()
            auth_user = AuthUser()
            auth_user.login_user(payload)
            auth = auth_user.get_code()
            auth_user.validate_schema(auth_user.get_data())
            if auth == 200:
                assert auth_user.get_message() == "Вы успешно вошли в систему"
                assert auth_user.get_username() == payload["username"]
            elif auth == 401:
                assert auth_user.get_error() == "Неверное имя пользователя или пароль"


            cursor.execute('SELECT id FROM "user" WHERE username = %s',
                       (payload["username"],))

        finally:
            if not payload['not_clear']:
                cursor.execute('DELETE FROM "user" WHERE username = %s',
                               (payload["username"],))
                db_connection.commit()
            cursor.execute('SELECT * FROM "user"')
            print(cursor.fetchall())
