import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.create_task_endpoint import CreateTask
from tests.api.endpoints.delete_task_endpoint import DeleteTask




@pytest.mark.parametrize(
    ("payload"), [
        ({"title": "Task1", "description": "task 1 description", "completed": False, "valid": True, "not_clear": True}),# incompleted task
        ({"title": "Task2", "description": "task 2 description", "completed": True, "valid": True,"not_clear": True})  # completed task
]
)
@allure.story("Удаление задачи")
def test_delete_task(payload, db_connection):
    try:
        cursor = db_connection.cursor()

        user_data = {"username": "Paravoz", "password": "password"}
        auth_user = AuthUser()
        auth_user.login_user(user_data)
        new_task = CreateTask()
        new_task.create_task(payload)
        task_id = new_task.get_id()
        delete_task = DeleteTask()
        delete_task.delete_task(task_id)
        delete_code = delete_task.check_code()
        assert delete_code == 204


        cursor.execute('SELECT * FROM "task" WHERE id = %s',
                       (task_id,))


    finally:
        if not payload['not_clear']:
            cursor.execute('DELETE FROM "task" WHERE title = %s',
                          (payload["title"],))
            db_connection.commit()
        cursor.execute('SELECT * FROM "task"')
        print(cursor.fetchall())