from repo.class_db import ClassDB
from core.classes import Task

class TaskRepo:
    def __init__(self):
        self.db = ClassDB()

    def change_db_1(self, command: str):
        return True

    def change_db_2(self, command: str):
        return True

    def create_db_3(self):
        return 'DB3'
	
    def create_db_4(self):
        return 'DB4'
    
    def result_of_command_1(self, commamd: str):
        return 'Result 1'
    
    def result_of_command_2(self, command: str):
        return 'Result 2'

    def result_of_command_3(self, db: str, command: str, table: str):
        return 'Result 3'

    def get_tasks(self):
        return self.db.get_tasks()

    def get_attempts_by_task(self, id):
        return self.db.get_attempts_by_task(id)

    def task_create(self, task: Task):
        self.db.insert_task(task)

    def select_task(self):
        return self.db.index()
	


