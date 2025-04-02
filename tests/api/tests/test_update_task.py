import allure
import pytest

from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.create_task_endpoint import CreateTask
from tests.api.endpoints.update_task_endpoint import UpdateTask


@pytest.mark.parametrize(
    ("payload"), [
        ({"title":"Fresh New Task", "valid": True, "not_clear": True}), #refresh title
        ({"description":"The freshest description", "valid": True, "not_clear": True}), #refresh description
        ({"valid": False, "not_clear": True}), #empty payload
        ({"title":"Fresh new task", "description":"new desc", "completed": True,"valid": False, "not_clear": False}) #refresh all
    ]
)

@allure.story("Обновление задачи")
def test_get_task(payload, db_connection):
    try:
        cursor = db_connection.cursor()

        user_data = {"username": "Paravoz", "password": "password"}
        task = {"title":"NewTask", "description":"New task description", "completed": False}
        print(task['title'])
        auth_user = AuthUser()
        auth_user.login_user(user_data)
        new_task = CreateTask()
        new_task.create_task(task)
        task_id = new_task.get_id()
        upd_task = UpdateTask()
        upd_task.update_task(payload, task_id)
        task_code = upd_task.check_code()


        if not 'title' in payload:
            assert upd_task.get_title() == task['title']
        elif not 'description' in payload:
            assert upd_task.get_description() == task['description']
        elif not 'completed' in payload:
            assert upd_task.check_completed() == task['completed']
        elif not 'title'in payload and not 'description' in payload and not 'completed' in payload:
            assert upd_task.check_code() == 400
            assert upd_task.check_error_message() == "Данные не предоставлены"

        elif task_code == 200:
                assert upd_task.get_id() == task_id
                assert upd_task.get_title() == payload['title']
                assert upd_task.get_description() == payload['description']
                assert upd_task.check_completed() == payload['completed']
        else:
                assert task_code == 404




        cursor.execute('SELECT * FROM "task" WHERE id = %s',
                       (task_id,))


    finally:
        if not payload['not_clear']:
            cursor.execute('DELETE FROM "task" WHERE title = %s',
                           (payload["title"],))
            db_connection.commit()
        cursor.execute('SELECT * FROM "task"')
        print(cursor.fetchall())