from uuid import uuid4
from core.classes import Task
from services.task_service import TaskService

class TaskController:
    def __init__(self):
        self.task_service = TaskService()

    def update_bd(self,command: str):
        return self.task_service.update_bd(command)

    def test_task(self,task: Task,text: str):
        task.set_attempt(uuid4(), text, False)
        return self.task_service.test_task(task) 

    def task_create(self, command: str, task: Task):
        return self.task_service.task_create(command, task)

    def update_task(self, command: str, task: Task):
        return self.task_service.update_task(command, task)

    def task(self, command: str, solution: str):
        return self.task_service.task(command, solution)

    def get_tasks(self):
        return self.task_service.get_tasks()


    def get_attempts_by_task(self, task: Task ):
        return self.task_service.get_attempts_by_task(task.get_taskid())
