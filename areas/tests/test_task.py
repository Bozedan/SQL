import pytest
from controller.task_controller import TaskController
from core.classes import Task, TaskType

@pytest.fixture()
def task_controller():
    return TaskController()

class TestTask:
	
    def test_update_bd_insert(self):
        task_controller = TaskController()
        result = task_controller.update_bd('INSERT command')
        assert result == True

    def test_update_db_drop(self):
        task_controller = TaskController()
        result = task_controller.update_bd('DROP command')
        assert result == True

    def test_test_task_select(self):
        task_controller = TaskController()
        task = Task(0, 'Test task', 'Test solution', TaskType.SELECT)
        result = task_controller.test_task(task, 'solution')
        assert result == True

    def test_test_task_update(self):
        task_controller = TaskController()
        task = Task(0, 'Test task', 'Test solution', TaskType.UPDATE)
        result = task_controller.test_task(task, 'solution')
        assert result == True

    def test_task_create(self, task_controller):
        task = Task(0, 'Test task', 'Test solution', TaskType.UPDATE)
        result = task_controller.task_create('update', task)
        assert result.getmessage() == 'Done!'

        result = task_controller.task_create('delete', task)
        assert result.get_text() == "Something went wrong..."

    def test_update_task(self, task_controller):
        task = Task(0, 'Test task', 'Test solution', TaskType.UPDATE)
        result = task_controller.update_task('update', task)
        assert result.getmessage() == 'Изменения отменены'

        result = task_controller.update_task('Да', task)
        assert result.getmessage() == "Данные успешно сохранены"

    def test_task(self, task_controller):
        task_k = Task(0, 'Test task', 'Test solution', TaskType.UPDATE)
        solution = task_k.get_solution()
        result = task_controller.task('Просмотр предыдущих попыток решения', solution)
        assert result.getmessage() == 'Выбирите действие'

        result = task_controller.task('Решение задания', solution)
        assert result.getmessage() == 'Задание решено'

        result = task_controller.task('Пробное решение задания', solution)
        assert result.getmessage() == 'Задание решено'

    def test_get_tasks(self):
        task_controller = TaskController()
        res = task_controller.get_tasks()
        assert res == []

    def test_get_attempts_by_task(self):
        task_controller = TaskController()
        task_k = Task(0, 'Test task', 'Test solution', TaskType.UPDATE)
        res = task_controller.get_attempts_by_task(task_k)
        assert res == None
