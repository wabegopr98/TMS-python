import pytest
from task_manager import TaskManager
import allure

@pytest.fixture
def task_manager():
    return TaskManager()

@allure.feature("Добавление задачи и установка приоритета")
@allure.story("Задачи и их приоритет")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_task_and_set_priority(task_manager):
    add_task_and_set_priority = TaskManager()
    add_task_and_set_priority.add_task('TASK1', 'normal')
    add_task_and_set_priority.add_task('task2', 'low')
    add_task_and_set_priority.add_task('Task3', 'high')
    assert len(add_task_and_set_priority.tasks) == 3

@allure.severity(allure.severity_level.NORMAL)
@allure.step("Установка неправильного приоритета для задачи")
def test_raising_error_for_invalid_priority(task_manager):
    raising_error_for_invalid_priority = TaskManager()
    with pytest.raises(ValueError, match="Приоритет должен быть 'low', 'normal' или 'high'"):
        raising_error_for_invalid_priority.add_task('Invalid Task', '12234')

@allure.feature("Отметка задачи как завершенной")
@allure.severity(allure.severity_level.CRITICAL)
def test_mark_task_completed(task_manager):
    task_completed = TaskManager()
    task_completed.add_task('Task4', 'low')
    updated_task = task_completed.mark_task_completed('Task4')

    assert updated_task['completed'] is True
    assert updated_task['name'] == 'Task4'

@allure.severity(allure.severity_level.NORMAL)
@allure.step("Отметка несуществующей задачи как выполненная")
def test_mark_task_completed_raises_error(task_manager):
    error_for_incomplete_task = TaskManager()
    with pytest.raises(ValueError, match="Задача с таким названием не найдена"):
        error_for_incomplete_task.mark_task_completed('NonExistentTask')

@allure.feature("Удаление задачи из списка")
@allure.severity(allure.severity_level.BLOCKER)
def test_remove_task(task_manager):
    deleted_task = TaskManager()
    deleted_task.add_task('Task5', 'low')
    removed_task = deleted_task.remove_task('Task5')
    assert removed_task['name'] == 'Task5'

@allure.severity(allure.severity_level.NORMAL)
@allure.step("Удаление несуществующей задачи из списка")
def test_remove_task_raises_error(task_manager):
    error_for_removed_task = TaskManager()
    with pytest.raises(ValueError, match="Задача с таким названием не найдена"):
        error_for_removed_task.remove_task('NonExistentTask')