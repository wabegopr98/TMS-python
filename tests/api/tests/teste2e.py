from tests.api.endpoints.auth_user_endpoint import AuthUser
from tests.api.endpoints.register_endpoint import RegisterUser
from tests.api.endpoints.create_task_endpoint import CreateTask
from tests.api.endpoints.delete_task_endpoint import DeleteTask
from tests.api.endpoints.get_task_byid_endpoint import GetTask
from tests.api.endpoints.switch_status_endpoint import SwitchStatusTask
from tests.api.endpoints.update_task_endpoint import UpdateTask
import pytest
import allure


from tests.api.payload.payload import (valid_new_task_payload,
                                       update_task_payload)


@pytest.mark.parametrize(
    ("payload"), [
        ({"username": "Paravoz", "password": "password", "valid": True,
          "not_clear": True}),
        ({"username": "Andrey",  "password": "password2", "valid": True,
          "not_clear": True}),
        ({"username": "Viktor",  "password": "password3", "valid": False,
          "not_clear": False})
    ]
)
@allure.story("Сценарий1: Полный цикл задачи")
@allure.feature("E2E Test")
def test_e2e_case(db_connection, payload):
    with allure.step("Создание пользователя"):
        new_user = RegisterUser()
        new_user.new_user(payload)
        new_user.get_code()
        new_user.validate_schema(new_user.get_data())
    with allure.step("Проверка пользователя в БД"):
        cursor = db_connection.cursor()
        cursor.execute('SELECT * FROM "user" WHERE username = %s',
                       (payload['username'],))
        user = cursor.fetchone()
        cursor.close()
        print(f"---------Пользователь {user}")
        user_id = user[0]
        assert user is not None, f" Пользователь с ID {user_id} не найден в БД"
        print(f" Пользователь найден в БД: ID {user_id}")
    with allure.step("Проверка, что данные API соответствуют данным в БД"):
        print(type(user))
        assert payload["username"] == user[1], (f'Expected '
        f'{payload["username"]},got {user[1]}')
    with allure.step("Аутентификация юзера"):
        auth_user = AuthUser()
        auth_user.login_user(payload)
        auth_user.validate_schema(auth_user.get_data())
    with allure.step("Создание задачи"):
        new_task = CreateTask()
        new_task.create_task(valid_new_task_payload)
        new_task.get_code()
        new_task.validate_schema(new_task.get_data())
        task_id = new_task.get_id()
    with allure.step("Получение задачи по ID"):
        find_task = GetTask()
        find_task.get_task(task_id)
        find_task.get_code()
        find_task.validate_schema(find_task.get_data())
    with allure.step("Проверка о записи задачи в БД"):
        print(f"🔍 Проверка задачи {task_id} в БД...")
        cursor = db_connection.cursor()
        cursor.execute('SELECT id, title, description, completed FROM "task" '
                       'WHERE id = %s', (task_id,))
        task = cursor.fetchone()
        cursor.close()
        print(f"---------Задача {task}")
        assert task is not None, f"❌ Задача {task_id} не найдена в БД!"
        print(f"✅ Задача найдена в БД: ID {task_id}")
    with (allure.step("Проверка, что данные API соответствуют данным в БД")):
        print(type(task))
        assert valid_new_task_payload["title"] == task[1], (f''
        f'Expected {valid_new_task_payload["title"]}, got {task[1]}')
        assert valid_new_task_payload["description"] == task[2], (f''
        f'Expected {valid_new_task_payload["description"]}, got {task[2]}')
        assert valid_new_task_payload["completed"] == task[3], (f''
        f'Expected {valid_new_task_payload["completed"]},got {task[3]}')
    with allure.step("Обновление задачи"):
        upd_task = UpdateTask()
        upd_task.update_task(update_task_payload, task_id)
        upd_task.check_code()
    with allure.step("Изменение статуса задачи"):
        switch_task = SwitchStatusTask()
        switch_task.switch_status_task(task_id)
        switch_task.check_code()
        switch_task.validate_schema(switch_task.get_data())
    with allure.step("Удаление задачи"):
        delete_task = DeleteTask()
        delete_task.delete_task(task_id)
        delete_task.check_code()
    with allure.step("Проверка, что задача удалена из БД"):
        print(f"🔍 Проверка УДАЛЕНИЯ задачи {task_id} из БД...")
        cursor = db_connection.cursor()
        cursor.execute('SELECT id, title, description, completed FROM "task"'
                       ' WHERE id = %s', (task_id,))
        task = cursor.fetchone()
        cursor.close()
        print(f"---------Была удалена задача: {task}")
        assert task is None, f" ❌ Удаленная задача найдена в БД: ID {task_id}"
        print(f"✅ Удаленная задача {task_id} не найдена в БД! ")
