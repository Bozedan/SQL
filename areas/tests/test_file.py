from classes import Task, TaskType,  Message, DirectionType, Alert
from user import User, Moderator, Teacher, Student
import time
import math

# Запуск тестов командой pytest -v test_file.py
# Оценить покрытие  pytest --cov=<Имя_файла> --cov-report html

# Сейчас файл с ошибками, нужно актуализировать тестовые данные, и актуализировать функции-тесты
# (каждая функция тестирует отдельный класс)
# Все тесты должны проходить 10 раз подряд и покрытие должно быть 100% обоих файлов

attempt_task = Task.Attempt(0, "select", False)
attempt_student = Student.Attempt(0, "select", False)
task = Task(0, "delete it", "delete", TaskType.SELECT)
trainingDB = Teacher.TrainingDB(0, "host", "postgresql", "Ilya", "qwerty", [[], task])
message = Message(10, "hi", DirectionType.FromUser)
alert = Alert(3, "oops")
user = User(1, "Artem", "rtyuijk")
subscription = Student.Subscription(1, True)
student = Student(1, "Artem", "rtyuijk", status=True)
teacher = Teacher(1, "Artem", "rtyuijk")
moderator = Moderator(1, "Artem", "rtyuijk", status=True, alerts=[])


def test_task():
    assert task.get_taskid() == 0, 'wrong id'
    assert task.get_text() == 'delete it', 'wrong text'
    assert task.get_solution() == "delete", 'wrong solution'
    assert task.get_type() == TaskType.SELECT, 'wrong type'
    task.set_taskid(1)
    assert task.get_taskid() == 1, 'Wrong id'
    task.set_text("update id")
    assert task.get_text() == "update id", 'Wrong text'
    task.set_type(TaskType.UPDATE)
    assert task.get_type() == TaskType.UPDATE, 'wrong type'
    task.set_solution("update")
    assert task.get_solution() == "update", 'wrong solution'
    task.set_attempt(1, "bla bla", True)
    list_of_attempt = task.attempt
    assert list_of_attempt[1].get_text() == "bla bla"
    assert not task.is_solution_correct("select"), 'wrong is_solution_correct'
    assert task.is_solution_correct("update"), 'wrong is_solution_correct'

    # attempt
    assert attempt_task.get_attemptid() == 0, 'Wrong id'
    assert attempt_task.get_solved() == False, 'Wrong solved'
    assert attempt_task.get_text() == "select", 'Wrong text'
    attempt_task.set_attemptid(1)
    assert attempt_task.get_attemptid() == 1, 'Wrong id'
    attempt_task.set_solved(True)
    assert attempt_task.get_solved() == True, 'Wrong solved'
    attempt_task.set_text("update")
    assert attempt_task.get_text() == "update", 'Wrong text'
    attempt_task.set_time(time.gmtime(1000))
    assert attempt_task.get_time() == time.gmtime(1000), 'Wrong time'
    assert attempt_task.getinfo() == dict(attemptid=1, solved=True, time=time.gmtime(1000), text="update")


def test_message():
    assert message.get_messageid() == 10, 'wrong messageid'
    assert message.getmessage() == 'hi', 'wrong text'
    assert message.get_direct() == DirectionType.FromUser, 'wrong direct'
    message.set_time(time.gmtime(1000000))
    assert message.get_time() == time.gmtime(1000000)
    message.set_text('bye')
    assert message.getmessage() == 'bye', 'wrong text'
    message.set_messageid(0)
    assert message.get_messageid() == 0, 'wrong messageid'
    message.set_direct(DirectionType.FromModerator)
    assert message.get_direct() == DirectionType.FromModerator, 'wrong direct'
    assert message.sendmessage(), 'wrong sendmessage'


def test_alert():
    assert alert.get_text() == 'oops', 'wrong text'
    assert alert.get_alertid() == 3, 'wrong alertid'
    alert.set_time(time.gmtime(2000000))
    assert alert.get_time() == time.gmtime(2000000), 'wrong time'
    alert.set_text("ok")
    assert alert.get_text() == 'ok', 'wrong text'
    alert.set_alertid(4)
    assert alert.get_alertid() == 4, 'wrong alertid'
    assert alert.create(), 'wrong create'


def test_user():
    assert user.get_id() == 1, 'wrong id'
    user.set_id(2)
    assert user.get_id() == 2, 'wrong id'
    assert user.get_username() == 'Artem', 'wrong username'
    user.set_username('Ilya')
    assert user.get_username() == 'Ilya', 'wrong username'
    assert user.get_hash() == 'rtyuijk', 'wrong hash'
    user.set_hash('qwerty')
    assert user.get_hash() == 'qwerty', 'wrong hash'


def test_teacher():
    assert teacher.get_id() == 1, 'wrong id'
    teacher.set_id(2)
    assert teacher.get_id() == 2, 'wrong id'
    assert teacher.get_username() == 'Artem', 'wrong username'
    teacher.set_username('Ilya')
    assert teacher.get_username() == 'Ilya', 'wrong username'
    assert teacher.get_hash() == 'rtyuijk', 'wrong hash'
    teacher.set_hash('qwerty')
    assert teacher.get_hash() == 'qwerty', 'wrong hash'
    assert trainingDB.get_dbid() == 0, 'wrong bdid'
    assert trainingDB.get_host() == 'host', 'wrong host'
    assert trainingDB.get_database() == 'postgresql', 'wrong db'
    assert trainingDB.get_user() == 'Ilya', 'wrong user'
    assert trainingDB.get_password() == 'qwerty', 'wrong password'
    assert trainingDB.get_tasks() == [[], task], 'wrong tasks'
    trainingDB.set_tasks([])
    assert trainingDB.get_tasks() == [], 'wrong tasks'
    trainingDB.set_bdid(2)
    assert trainingDB.get_dbid() == 2, 'wrong bdid'
    trainingDB.set_host("server")
    assert trainingDB.get_host() == 'server', 'wrong host'
    trainingDB.set_user("Artem")
    assert trainingDB.get_user() == 'Artem', 'wrong user'
    trainingDB.set_database("mysql")
    assert trainingDB.get_database() == 'mysql', 'wrong db'
    trainingDB.set_password("12345")
    assert trainingDB.get_password() == '12345', 'wrong db'
    assert trainingDB.query() == True, 'wrong query'


def test_moderator():
    assert moderator.get_id() == 1, 'wrong id'
    moderator.set_id(2)
    assert moderator.get_id() == 2, 'wrong id'
    assert moderator.get_username() == 'Artem', 'wrong username'
    moderator.set_username('Ilya')
    assert moderator.get_username() == 'Ilya', 'wrong username'
    assert moderator.get_hash() == 'rtyuijk', 'wrong hash'
    moderator.set_hash('qwerty')
    assert moderator.get_hash() == 'qwerty', 'wrong hash'
    assert moderator.get_status() is True, 'wrong status'
    moderator.set_status(False)
    assert moderator.get_status() is False, 'wrong status'
    alert_2 = Alert(6, "oops")
    list_of_alerts = [alert, alert_2]
    moderator.set_alerts(list_of_alerts)
    assert moderator.get_alerts()[1].get_alertid() == 6, 'wrong alert id'


def test_student():
    assert student.get_id() == 1, 'wrong id'
    student.set_id(2)
    assert student.get_id() == 2, 'wrong id'
    assert student.get_username() == 'Artem', 'wrong username'
    student.set_username('Ilya')
    assert student.get_username() == 'Ilya', 'wrong username'
    assert student.get_hash() == 'rtyuijk', 'wrong hash'
    student.set_hash('qwerty')
    assert student.get_hash() == 'qwerty', 'wrong hash'
    assert student.get_status() is True, 'wrong status'
    student.set_status(False)
    assert student.get_status() is False, 'wrong status'
    student.set_attempt(1, "bla bla", True)
    list_of_attempt = student.attempt
    assert list_of_attempt[1].get_text() == "bla bla"

    # subscription
    assert subscription.get_subscription_id() == 1, 'wrong id'
    subscription.set_subscription_id(2)
    assert subscription.get_subscription_id() == 2, 'wrong id'
    assert math.isclose(subscription.get_date_start(), (subscription.get_date_end() - 365 * 24 * 3600))
    assert subscription.get_status() is True, 'wrong status'
    subscription.set_status(False)
    assert subscription.get_status() is False, 'wrong status'

    # attempt
    assert attempt_student.get_attemptid() == 0, 'Wrong id'
    assert attempt_student.get_solved() == False, 'Wrong solved'
    assert attempt_student.get_text() == "select", 'Wrong text'
    attempt_student.set_attemptid(1)
    assert attempt_student.get_attemptid() == 1, 'Wrong id'
    attempt_student.set_solved(True)
    assert attempt_student.get_solved() == True, 'Wrong solved'
    attempt_student.set_text("update")
    assert attempt_student.get_text() == "update", 'Wrong text'
    attempt_student.set_time(time.gmtime(1000))
    assert attempt_student.get_time() == time.gmtime(1000), 'Wrong time'
    assert attempt_student.getinfo() == dict(attemptid=1, solved=True, time=time.gmtime(1000), text="update")


