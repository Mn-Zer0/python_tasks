from storage import read_json
from models import validate, Vacancy

vacancies = []
file = "task.json"

if __name__ == "__main__":
    data = read_json(file)
    validate(data)

    for record in data:
        vacancies.append(Vacancy(record['id'], record['title'], record['salary'], record['status']))

    for vacansy in vacancies:
        print(vacansy.ID, vacansy.title, vacansy.salary, vacansy.status)
