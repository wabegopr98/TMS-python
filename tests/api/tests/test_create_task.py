import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.create_task_endpoint import CreateTask


@pytest.mark.parametrize(
    ("payload"), [
        ({"title":"Task1", "description":"task 1 description", "completed": False, "valid": True, "not_clear": True}), #incompleted task
        ({"title":"Task2", "description":"task 2 description", "completed": True, "valid": True, "not_clear": True}), #completed task
        ({"title":"Task3", "description":"", "completed": False, "valid": False, "not_clear": False}), #empty description
        ({"title":"Task4", "description":"task without title", "valid": False, "not_clear": False}) #empty completed
    ]
)
@allure.story("Создание задачи")
def test_create_task(payload, db_connection):
    try:
        cursor = db_connection.cursor()


        user_data = {"username": "Paravoz", "password": "password"}
        auth_user = AuthUser()
        auth_user.login_user(user_data)
        new_task = CreateTask()
        new_task.create_task(payload)
        task_request_code = new_task.get_code()
        new_task.validate_schema(new_task.get_data())
        if not 'completed' in payload:
            assert new_task.check_completed() == False
        elif task_request_code == 201:
            assert new_task.get_title() == payload["title"]
            assert new_task.check_completed() == payload["completed"]

        elif task_request_code == 401:
            assert auth_user.get_error() == "Неверное имя пользователя или пароль"
        if not payload['description']:
            assert new_task.get_description() == ""


        cursor.execute('SELECT * FROM "task" WHERE title = %s',
                       (payload["title"],))

    finally:
        if not payload['not_clear']:
            cursor.execute('DELETE FROM "task" WHERE title = %s',
                           (payload["title"],))
            db_connection.commit()
        cursor.execute('SELECT * FROM "task"')
        print(cursor.fetchall())




