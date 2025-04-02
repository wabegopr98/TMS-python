import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.create_task_endpoint import CreateTask
from tests.api.endpoints.get_task_byid_endpoint import GetTask


@pytest.mark.parametrize(
    ("payload"), [
        ({"title":"Task1", "description":"task 1 description", "completed": False, "valid": True, "not_clear": True}), #incompleted task
        ({"title":"Task2", "description":"task 2 description", "completed": True, "valid": True, "not_clear": True}), #completed task
        ({"title":"Task3", "description":"", "completed": False, "valid": False, "not_clear": False}), #empty description
        ({"title":"Task4", "description":"task without title", "valid": False, "not_clear": False}) #empty completed
    ]
)
@allure.story("Получение задачи по id")
def test_get_task(payload, db_connection):
    try:
        cursor = db_connection.cursor()

        user_data = {"username": "Paravoz", "password": "password"}
        auth_user = AuthUser()
        auth_user.login_user(user_data)
        new_task = CreateTask()
        new_task.create_task(payload)
        task_id = new_task.get_id()
        task_title = new_task.get_title()
        find_task = GetTask()
        find_task.get_task(task_id)
        task_code = find_task.get_code()
        find_task.validate_schema(find_task.get_data())
        if task_code == 200:
            assert find_task.get_id() == task_id
            assert find_task.get_title() == task_title
        else:
            assert task_code == 404



        cursor.execute('SELECT * FROM "task" WHERE id = %s',
                       (task_id,))


    finally:
        pass
        # if not payload['not_clear']:
        #     cursor.execute('DELETE FROM "task" WHERE title = %s',
        #                    (payload["title"],))
        #     db_connection.commit()
        # cursor.execute('SELECT * FROM "task"')
        # print(cursor.fetchall())