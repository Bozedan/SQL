from repo.class_db import ClassDB
from core.user import Student
from core.user import Moderator
from core.user import Teacher

class UserRepository:
    def __init__(self):
        self.db = ClassDB()

    def create_student(self, new_user: Student):

        self.db.insert_student(new_user)

    def get_student_by_login(self, login: str):
        return self.db.get_student_by_login(login)
    
    def get_user_by_login(self, login: str):
        return self.db.get_user_by_login(login)
    
    def set_status_false_student(self, userID: str):
        #получить текущего юзера
        return self.db.StudentDeleted(userID)

    def create_moderator(self, new_user: Moderator):
        self.db.insert_moderator(new_user)

    def get_moderator_by_login(self, login: str):
        return self.db.get_moderator_by_login(login)

    def create_teacher(self, new_user: Teacher):
        self.db.insert_teacher(new_user)

    def get_teacher_by_login(self, login: str):
        return self.db.get_teacher_by_login(login)

    def get_user_by_id(self, id: int):
        return self.db.get_user_by_id(id)

    def change_user_login(self, id: int, login: str):
        return self.db.change_user_login(id,login)

    def change_user_password(self, id: int, password: str):
        return self.db.change_user_password(id, password)
