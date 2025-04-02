import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.create_task_endpoint import CreateTask
from tests.api.endpoints.switch_status_endpoint import SwitchStatusTask



@pytest.mark.parametrize(
    ("payload"), [
        ({"title": "Task1", "description": "task 1 description", "completed": False, "valid": True, "not_clear": True}),# incompleted task
        ({"title": "Task2", "description": "task 2 description", "completed": True, "valid": True,"not_clear": True})  # completed task
]
)
@allure.story("Переключение статуса задачи")
def test_switch_status_task(payload, db_connection):
    try:
        cursor = db_connection.cursor()

        user_data = {"username": "Paravoz", "password": "password"}
        auth_user = AuthUser()
        auth_user.login_user(user_data)
        new_task = CreateTask()
        new_task.create_task(payload)
        task_id = new_task.get_id()
        task_status = new_task.check_completed()
        switch_task = SwitchStatusTask()
        switch_task.switch_status_task(task_id)
        switch_task.validate_schema(switch_task.get_data())
        switch_code = switch_task.check_code()
        if switch_code == 200:
            assert switch_task.check_completed() != task_status
            assert switch_task.get_id() == task_id
        else:
                assert switch_code != 200

        cursor.execute('SELECT * FROM "task" WHERE id = %s',
                       (task_id,))


    finally:
        if not payload['not_clear']:
            cursor.execute('DELETE FROM "task" WHERE title = %s',
                           (payload["title"],))
            db_connection.commit()
        cursor.execute('SELECT * FROM "task"')
        print(cursor.fetchall())