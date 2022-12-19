from core.user import User, Moderator, Teacher, Student
from repo.user_repo import UserRepository
from uuid import uuid4
import bcrypt 
from jwt import encode, decode


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    '''регистрация(ученик) '''
    def signupStudent(self, id: str, login: str,password: str)->bool:
        user  = Student(id,login,bcrypt.hashpw(
                str(password).encode(), bcrypt.gensalt()).decode(),True)
        #проверка наличия пользователя с таким логином 
        if  (self.user_repository.get_student_by_login(login)):
        #raise UserExistsError
            return False
        else:    
            self.user_repository.create_student(user)
            return True
        
        

    '''авторизация'''
    def authorize(self,login: str,password: str) -> str:
        #проверка наличия пользователя в базе данных по логину и паролю 
        user = self.user_repository.get_user_by_login(login)
        if bcrypt.checkpw(password.encode(), str(user.get_hash()).encode()) is True:
            token = encode({"id": str(user.get_id())}, "a random, long, sequence of characters that only the server knows", algorithm="HS256") 
            print(user.get_id())
            return token
        else:
            return None

    '''удаление аккаунта '''
    def delete_account(self,token: str):
        #пометить аккаунт как удаленный в бд 
        userID = decode(token, "a random, long, sequence of characters that only the server knows", ["HS256"])['id']
        result = self.user_repository.set_status_false_student(userID)
        #вызов метода выхода из аккаунта 
        if result:
            self.logout(token)
            return result
        


    '''выход из аккаунта '''
    def logout(self, token: str):
        #закрытие доступа пользователя к сервисам (выкинуть на главную страницу)
        #закрытые соединения (куки?)
        #self.user_repository.close_connection()
        #закрытые соединения 
        #отправить апи запрос клиенту 
        return None
    """
        ''' редактирования профиля'''
        def update_profile(self):
            #какие изменения аккаунта могут быть (логин, пароль, имя, фамиилия, дата рождения)
    """
    '''регистрация(ученик) '''

    def signup_moderator(self, login: str, password: str):
        moderator = Moderator(uuid4(), login, bcrypt.hashpw(
            str(password).encode(), bcrypt.gensalt()).decode(), True, [])
        # проверка наличия пользователя с таким логином
        if self.user_repository.get_user_by_login(login):
            # raise ModeratorExistsError
            return False
        else:
            self.user_repository.create_moderator(moderator)
            return True, moderator.get_id()

    def signup_teacher(self, login: str, password: str):
        teacher = Teacher(uuid4(), login, bcrypt.hashpw(
            str(password).encode(), bcrypt.gensalt()).decode())
        # проверка наличия пользователя с таким логином
        if self.user_repository.get_user_by_login(login):
            # raise TeacherExistsError
            return False
        else:
            self.user_repository.create_teacher(teacher)
            return True, teacher.get_id()

    def edit_user_profile(self, id: int, login: str, password: str) -> bool:
        if self.user_repository.get_user_by_id(id):
            # raise UserExistsError
            return False

        if login is not None:
            self.user_repository.change_user_login(id, login)

        if password is not None:
            self.user_repository.change_user_password(id, bcrypt.hashpw(
                str(password).encode(), bcrypt.gensalt()).decode())

        return True
