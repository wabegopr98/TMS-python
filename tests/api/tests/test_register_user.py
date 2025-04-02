import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.register_endpoint import RegisterUser



@pytest.mark.parametrize(
    ("payload"), [
        ({"username":"Paravoz", "password":"password", "valid": True, "not_clear": True}),
        ({"username":"Zip",  "password":"password2", "valid": True, "not_clear": True}),
        ({"username":"Zip",  "password":"password3", "valid": False, "not_clear": False})
    ]
)
@allure.story("Регистрация пользователя")
def test_register_user(payload, db_connection):
    try:
        cursor = db_connection.cursor()

        new_user = RegisterUser()
        new_user.new_user(payload)
        new = new_user.get_code()
        new_user.validate_schema(new_user.get_data())
        if new == 201:
            assert new_user.get_message() == "Регистрация успешна"
        elif new == 401:
            assert new_user.get_message() == "Пользователь с таким именем уже существует"


        cursor.execute('SELECT id FROM "user" WHERE username = %s',
                       (payload["username"],))

    finally:
        if not payload['not_clear']:
            cursor.execute('DELETE FROM "user" WHERE username = %s',
                           (payload["username"],))
            db_connection.commit()
        cursor.execute('SELECT * FROM "user"')
        print(cursor.fetchall())




