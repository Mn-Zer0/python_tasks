from .storage import read_json
from .models import validate, Vacancy, filter_records, is_rule
from pathlib import Path


file = Path(__file__).parent.parent.parent / "task.json"
vacancies = []

def main():
    data = read_json(file)
    validate(data)

    filtered = filter_records(data, is_rule, key="status", value="open", limit=10)

    if filtered:
        for record in filtered:
            vacancies.append(Vacancy(record['id'], record['title'], record['salary'], record['status']))

        for vacansy in vacancies:
            print(vacansy.ID, vacansy.title, vacansy.salary, vacansy.status)
    else:
        print("Записи не найдены")