from core.user import User, Student, Moderator, Teacher
from core.classes import Task
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

class UserNotExistsError(Exception):
        #print("User not exists")
        pass

class ClassDB:
    def __init__(self):
        self.tasks = []
        self.teachers = []
        self.users = []
        self.moderators = []
        self.students = []
        self.db = get_db_connection()

    def insert_task(self, task: Task):
        self.tasks.append(task)

    def insert_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def insert_moderator(self, moderator: Moderator):
        self.moderators.append(moderator)

    def insert_student(self, student: Student):
        self.db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                        (student.get_username(), student.get_hash())
                        )

    def insert_user(self, user: User):
        self.users.append(user)

    def get_student_by_login(self, login: str):
        res = self.db.execute("SELECT id, username, hash  FROM users WHERE username=?",
                        (login,)
                        )
        row = res.fetchone()
        if (row == None):
            return None
        else:
            return Student(row[0], row[1], row[2])

    def get_user_by_login(self, login: str):
        for i in self.users:
            if i.get_username() == login:
                return i
        for i in self.students:
            if i.get_username() == login:
                return i
        for i in self.moderators:
            if i.get_username() == login:
                return i
        for i in self.teachers:
            if i.get_username() == login:
                return i
        return None

    def get_moderator_by_login(self, login: str):
        for i in self.moderators:
            if i.get_username() == login:
                return i
        return None

    def get_teacher_by_login(self, login: str):
        for i in self.teachers:
            if i.get_username() == login:
                return i
        return None

    def change_user_login(self, id: int, login: str):
        for i in self.users:
            if str(i.get_id()) == id:
                i.set_username(login)
                return True
        for i in self.students:
            if str(i.get_id()) == id:
                i.set_username(login)
                return True
        for i in self.moderators:
            if str(i.get_id()) == id:
                i.set_username(login)
                return True
        for i in self.teachers:
            if str(i.get_id()) == id:
                i.set_username(login)
                return True
        return False


    def change_user_password(self, id: int, password: str):
        for i in self.users:
            if str(i.get_id()) == id:
                i.set_password(password)
                return True
        for i in self.students:
            if str(i.get_id()) == id:
                i.set_password(password)
                return True
        for i in self.moderators:
            if str(i.get_id()) == id:
                i.set_password(password)
                return True
        for i in self.teachers:
            if str(i.get_id()) == id:
                i.set_password(password)
                return True
        return False


    def get_user_by_id(self, id: int):
        for i in self.users:
            if str(i.get_id()) == id:
                return i
        for i in self.students:
            if str(i.get_id()) == id:
                return i
        for i in self.moderators:
            if str(i.get_id()) == id:
                return i
        for i in self.teachers:
            if str(i.get_id()) == id:
                return i
        return None
    
    def StudentDeleted(self, id: str):
        for i in range(len(self.students)):
             if str(self.students[i].get_id()) == id:
                self.students[i].set_status(False)
                return True
        return None

    def get_tasks(self):
        return self.tasks

    def get_attempts_by_task(self, id):
        for i in self.tasks:
            if i.get_taskid() == id:
                return i.get_attempts()
        return None

    def index(self):
        return Task

