from enum import Enum
import time


class DirectionType(Enum):
    FromModerator = 1
    FromUser = 2


class TaskType(Enum):
    SELECT = 1
    UPDATE = 2


class Message:
    __messageid: int
    __text: str
    __time: time
    __direct: DirectionType

    def __init__(self, messageid: int, text: str, direct: DirectionType):
        self.__text = text
        self.__time = time.time()
        self.__direct = direct
        self.__messageid = messageid

    def get_messageid(self):
        return self.__messageid

    def set_messageid(self, new_messageid: int):
        self.__messageid = new_messageid

    def getmessage(self):
        return self.__text

    def set_text(self, new_text: str):
        self.__text = new_text

    def get_time(self):
        return self.__time

    def set_time(self, new_time: time):
        self.__time = new_time

    def get_direct(self):
        return self.__direct

    def set_direct(self, new_direct):
        self.__direct = new_direct

    def sendmessage(self):
        # to BD
        return True


class Alert:
    __alertid: int
    __text: str
    __time: time

    def __init__(self, alertid: int, text: str):
        self.__text = text
        self.__time = time.time()
        self.__alertid = alertid

    def get_alertid(self):
        return self.__alertid

    def set_alertid(self, new_alertid: int):
        self.__alertid = new_alertid

    def get_text(self):
        return self.__text

    def set_text(self, new_text: str):
        self.__text = new_text

    def get_time(self):
        return self.__time

    def set_time(self, new_time: time):
        self.__time = new_time

    def create(self):
        # to BD
        return True


class Task:
    __taskid: int
    __text: str
    __solution: str
    __type: TaskType

    def __init__(self, __taskid: int, text: str, solution: str, tasktype: TaskType):
        self.__text = text
        self.__solution = solution
        self.__type = tasktype
        self.__taskid = __taskid
        self.attempt = [self.Attempt(attemptid=0, text="", solved=False)]

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

    def get_taskid(self):
        return self.__taskid

    def set_taskid(self, new_taskid: int):
        self.__taskid = new_taskid

    def get_text(self):
        return self.__text

    def set_text(self, new_text: str):
        self.__text = new_text

    def get_solution(self):
        return self.__solution

    def set_solution(self, new_solution: str):
        self.__solution = new_solution

    def get_type(self):
        return self.__type

    def set_type(self, new_type: TaskType):
        self.__type = new_type

    def is_solution_correct(self, solution):
        if solution == self.__solution:
            return True
        return False

    def get_attempts(self):
        return self.attempt
