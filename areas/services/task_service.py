from core.user import Student
from core.classes import Task, TaskType, Message, Alert, DirectionType
from repo.task_repo import TaskRepo

class TaskService:
    def __init__(self):
        self.task_repo = TaskRepo()

    def update_bd(self, command: str):
        if not (self.task_repo.change_db_1(command)):
            return False
        if self.check_type(command):
            command = self.modify_command(command)
        if not (self.task_repo.change_db_2(command)):
            return False
        return True

    def test_task(self,task: Task):
        if self.check_task_resolve(task.get_attempts()[len(task.get_attempts())-1], task.get_solution(), task.get_type()):
            return True
        else: 
            return False

    def check_type(self, command: str):
        if ("INSERT" in command.upper()) or ("DELETE" in command.upper()):
            return True
        else:
            return False

    def modify_command(self, command: str):
        return command
    
    def check_task_resolve(self, attempt: Student.Attempt, solution: str, task_type: TaskType):
        text = attempt.get_text()
        if task_type == TaskType.SELECT:
            result = self.task_repo.result_of_command_1(text)
            if result != self.task_repo.result_of_command_1(solution):
                return False
            result = self.task_repo.result_of_command_2(text)
            if result != self.task_repo.result_of_command_2(solution):
                return False
            return True
        else:
            db_3 = self.task_repo.create_db_3()
            db_4 = self.task_repo.create_db_4()
            table = solution.partition("/*")[2].partition("*/")[0]
            result = self.task_repo.result_of_command_3(db_3, text, table)
            if result != self.task_repo.result_of_command_3(db_4, solution, table):
                return False
            return True

    @staticmethod
    def check_command(command):
        command = command.lower()
        if command not in ('select', 'update'):
            return False
        return True

    def task_create(self, command, task: Task):
        if self.check_command(command) and command.lower() == 'update' and self.test_task(task):
            self.task_repo.task_create(task)
            return Message(text="Done!", direct=DirectionType.FromUser, messageid=1)
        return Alert(alertid=1, text='Something went wrong...')

    def update_task(self, command: str, task: Task):
        if command == 'Да' and self.test_task(task):
            self.task_repo.task_create(task)
            return Message(text="Данные успешно сохранены", direct=DirectionType.FromUser, messageid=3)
        return Message(text="Изменения отменены", direct=DirectionType.FromUser, messageid=2)

    def task(self, command: str, solution: str):
        # task_bd = self.task_repo.select_task()
        task_bd = Task(0, 'Test task', 'Test solution', TaskType.UPDATE)
        if command == 'Пробное решение задания':
            if self.check_task_resolve(task_bd.get_attempts()[len(task_bd.get_attempts()) - 1], task_bd.get_solution(),
                                       task_bd.get_type()):
                return Message(text="Задание решено", direct=DirectionType.FromUser, messageid=3)
            return Message(text="Задание не решено", direct=DirectionType.FromUser, messageid=3)
        if command == 'Решение задания':
            if self.check_task_resolve(task_bd.get_attempts()[len(task_bd.get_attempts()) - 1], task_bd.get_solution(),
                                       task_bd.get_type()):
                return Message(text="Задание решено", direct=DirectionType.FromUser, messageid=3)
            return Message(text="Задание не решено", direct=DirectionType.FromUser, messageid=3)
        if command == 'Просмотр предыдущих попыток решения':
            pass
        return Message(text="Выбирите действие", direct=DirectionType.FromUser, messageid=2)

            
    def get_tasks(self):
        return self.task_repo.get_tasks()

    def get_attempts_by_task(self, id):
        return self.task_repo.get_attempts_by_task(id)
    
            
