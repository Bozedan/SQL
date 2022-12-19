from services.user_service import UserService
#from core.user import User, Student
from uuid import uuid4
from exceptions.exceptions import AlreadyExistsError

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def signupStudent(self, login: str, password: str):
        res = self.user_service.signupStudent(uuid4(),login, password)
        if not res:
            raise AlreadyExistsError
        return res


    #authentication
    def authorize(self, login: str, password: str) -> str:
        return self.user_service.authorize(login, password)
    
    def delete_account(self,token: str):
        return self.user_service.delete_account(token)

    def logout(self):
        return self.user_service.logout()

    def signup_moderator(self, login: str, password: str):
        return self.user_service.signup_moderator(login, password)

    def signup_teacher(self, login: str, password: str):
        return self.user_service.signup_teacher(login, password)

    def edit_user_profile(self, id, login: str, password: str):
        return self.user_service.edit_user_profile(id, login, password)


