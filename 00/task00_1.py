import json

print("\n00.1 task 1\n")

'''
1. Сохраните входные данные в JSON с кириллицей. Прочитайте их через pathlib и with , явно
задав UTF-8.
'''


def read_json():
    with open("task.json", "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


print("\n00.1 task 2\n")

'''
2. Сравните поиск записи перебором списка и по ключу словаря. Объясните, почему второй вариант
не перебирает все записи при обычном поиске; формальные доказательства не нужны.
'''


# Поиск записи перебором
def read_data(data):
    for record in data:
        if record["title"] == "Data Scientist":
            return record


data = read_json()
print(read_data(data))

# Поиск записи по ключу
index = {record["id"]: record for record in data}
found = index[4]
print(found)


print("\n00.1 task 3\n")

'''
3. Покажите на двух переменных разницу между ссылкой на один список и копией списка, между
is и == . Объясните, почему изменяемый список нельзя использовать как ключ словаря.
'''


a = [1, 2, 3]
b1 = a
b2 = a.copy()

b1.append(4)

print(a, b1, b2) # [1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3]
print(a == b1) # True
print(a == b2) # False
print(a is b1) # True
print(a is b2) # False


print("\n00.1 task 4\n")

"""
4. Вынесите выбор записей в функцию, принимающую другую функцию — правило фильтрации.
Используйте именованный аргумент с ограничением количества результатов.
"""


def filter_records(records, rule, *, limit=None):
    # print(records)
    filtered = [record for record in records if rule(record["status"])]
    if limit is None:
        return "limit is None"
    elif limit > len(records):
        return "len limit > len records"
    else:
        return filtered[:limit]

def is_open(status):
    return status == "open"

data = read_json()

print(filter_records(data, is_open, limit=3))


print("\n00.1 task 5\n")

"""
5. Разберите дату с часовым поясом, приведите её к UTC и обратно к местному времени. Не
принимайте дату без пояса молча: явно отклоните её или документируйте правило интерпретации.
Достаточно фиксированного смещения через datetime.timezone . Для ZoneInfo нужны системные
данные часовых поясов; если их нет, пакет tzdata добавите через uv на шаге 1.
"""


from datetime import datetime, timedelta, timezone

moment = datetime.fromisoformat("2026-03-01T10:00:00+03:00")

if moment.tzinfo is None:
    print("Часовой пояс не указан")

moment_utc = moment.astimezone(timezone.utc)
moment2 = moment_utc.astimezone(timezone(timedelta(hours=3)))
print(moment)
print(moment_utc)
print(moment2)