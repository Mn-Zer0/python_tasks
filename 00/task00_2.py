
print("\n00.2 task 1-2\n")

class VacancyFormatError(Exception):
    pass


import json

def read_json():
    try:
        with open("task.json", "r") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as exception:
                raise VacancyFormatError("Json decode error") from exception
    except FileNotFoundError as exception:
        raise VacancyFormatError("File not found") from exception

    return data

data = read_json()

def validate(record):
    required = ["id", "title", "salary", "status"]
    missing = None
    for i in required:
        if i not in record:
            missing = i

    if missing:
        raise VacancyFormatError(f"Прощено поле {missing}")

for r in data:
    validate(r)


class Vacancy:
    def __init__(self, ID, title, salary, status):
        self.ID = ID
        self.title = title
        self.salary = salary
        self.status = status
        self.info = []

    def close(self):
        self.status = "closed"

    def open(self):
        self.status = "open"


vacancies = []

for i in data:
    vacancies.append(Vacancy(i['id'], i['title'], i['salary'], i['status']))

vc1 = vacancies[0]

print(vc1.ID)
print(vc1.title)
print(vc1.salary)
print(vc1.status)

vc1.close()

print(vc1.ID)
print(vc1.title)
print(vc1.salary)
print(vc1.status)

vc2 = vacancies[1]

vc1.info.append(1)
vc2.info.append(2)

print(vc1.info)
print(vc2.info)


print("\n00.2 task 3\n")


def generator(data):
    for record in data:
        if record["status"] == "closed":
            print(record)
            yield record

gen = generator(data)
next(gen)
next(gen)


print("\n00.2 task 4\n")


from contextlib import contextmanager
import time

@contextmanager
def timer():
    print("вход в блок")
    t1 = time.perf_counter()
    try:
        yield
    finally:
        t2 = time.perf_counter() - t1
        print(f"выход из блока время: {t2} сек")


with timer():
    time.sleep(0.5)
    print("Работа выполнена")
print("После блока with")


print("\n00.2 task 5\n")

import functools

def deco(func):
    @functools.wraps(func)
    def wrapper(*a, **kwargs):
        print("Начало")
        result = func(*a, **kwargs)
        print("Конец")
        return result
    return wrapper


@deco
def sm(*, a, b):
    """Возвращает сумму квадратов двух чисел."""
    return a**2 + b**2


print(sm(a=1, b=2))
print(sm.__name__)
print(sm.__doc__)