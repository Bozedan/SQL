from core.classes import Alert, Task
import time


class User:
    __id: int
    __username: str
    __hash: str

    def __init__(self, id: int, username: str, hash: str):
        self.__id = id
        self.__username = username
        self.__hash = hash

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_hash(self):
        return self.__hash

    def set_id(self, id: int):
        self.__id = id

    def set_username(self, username: str):
        self.__username = username

    def set_hash(self, hash: str):
        self.__hash = hash


class Moderator(User):
    __status: bool
    __alerts: list[Alert]

    def __init__(self, id: int, username: str, hash: str, status: bool, alerts: list[Alert]):
        User.__init__(self, id, username, hash)
        self.__status = status
        self.__alerts = alerts

    def get_status(self):
        return self.__status

    def get_alerts(self):
        return self.__alerts

    def set_status(self, status: bool):
        self.__status = status

    def set_alerts(self, alerts: list[Alert]):
        self.__alerts = alerts


class Teacher(User):

    def __init__(self, id: int, username: str, hash: str):
        User.__init__(self, id, username, hash)
        self.db = self.TrainingDB(dbid=id, host="", database="", user="", password="", tasks=[])

    class TrainingDB:
        __dbid: int
        __host: str
        __database: str
        __user: str
        __password: str
        __tasks: list[Task]

        def __init__(self, dbid: int, host: str, database: str, user: str, password: str, tasks: list[Task]):
            self.__host = host
            self.__database = database
            self.__user = user
            self.__password = password
            self.__tasks = tasks
            self.__dbid = dbid

        def get_dbid(self):
            return self.__dbid

        def set_bdid(self, new_bdid: int):
            self.__dbid = new_bdid

        def get_host(self):
            return self.__host

        def set_host(self, new_host: str):
            self.__host = new_host

        def get_database(self):
            return self.__database

        def set_database(self, new_database: str):
            self.__database = new_database

        def get_user(self):
            return self.__user

        def set_user(self, new_user: str):
            self.__user = new_user

        def get_password(self):
            return self.__password

        def set_password(self, new_password: str):
            self.__password = new_password

        def get_tasks(self):
            return self.__tasks

        def set_tasks(self, new_tasks: list[Task]):
            self.__tasks = new_tasks

        def query(self):
            #
            return True


class Student(User):
    __status: bool

    def __init__(self, id: int, username: str, hash: str, status=False):
        User.__init__(self, id, username, hash)
        self.__status = status
        self.subscription = self.Subscription(id, status=False)
        self.attempt = [self.Attempt(attemptid=0, text="", solved=False)]

    class Subscription:
        __subscription_id: int
        __status: bool
        __date_start: time
        __date_end: time

        def __init__(self, subscription_id: int, status: bool):
            self.__subscription_id = subscription_id
            self.__status = status
            self.__date_start = time.time()
            self.__date_end = time.time() + 365 * 24 * 3600

        def get_subscription_id(self):
            return self.__subscription_id

        def get_status(self):
            return self.__status

        def get_date_start(self):
            return self.__date_start

        def get_date_end(self):
            return self.__date_end

        def set_subscription_id(self, subscription_id: int):
            self.__subscription_id = subscription_id

        def set_status(self, status: bool):
            self.__status = status

    class Attempt:
        __attemptid: int
        __solved: bool
        __time: time
        __text: str

        def __init__(self, attemptid: int, text: str, solved: bool):
            self.__solved = solved
            self.__time = time.time()
            self.__text = text
            self.__attemptid = attemptid

        def get_attemptid(self):
            return self.__attemptid

        def set_attemptid(self, new_attemptid: int):
            self.__attemptid = new_attemptid

        def get_solved(self):
            return self.__solved

        def set_solved(self, is_solved):
            self.__solved = is_solved

        def get_text(self):
            return self.__text

        def set_text(self, new_text: str):
            self.__text = new_text

        def get_time(self):
            return self.__time

        def set_time(self, new_time: time):
            self.__time = new_time

        def getinfo(self):
            return dict(attemptid=self.__attemptid,
                        solved=self.__solved,
                        time=self.__time,
                        text=self.__text)

    def set_attempt(self, temp_attemptid: int, temp_text: str, temp_solved: bool):
        temp = self.Attempt(attemptid=temp_attemptid, text=temp_text, solved=temp_solved)
        self.attempt.append(temp)

    def get_status(self):
        return self.__status

    def set_status(self, status: bool):
        self.__status = status
