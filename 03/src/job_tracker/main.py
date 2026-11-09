from pathlib import Path

from pydantic import ValidationError

from .models import Vacancy, ValidatedVacancy, filter_records, is_rule, to_vacancy
from .storage import read_json

file = Path(__file__).parent.parent.parent / "task.json"


def main():
    vacancies: list[Vacancy] = []
    raw_vacancies: list[ValidatedVacancy] = []

    data = read_json(file)
    # validate(data)

    try:
        raw_vacancies = [ValidatedVacancy(**record) for record in data]
    except ValidationError as e:
        print(e)

    filtered = filter_records(raw_vacancies, is_rule, key="status", value="open", limit=10)

    if filtered:
        vacancies = [to_vacancy(raw) for raw in filtered]

        for vacansy in vacancies:
            print(vacansy.ID, vacansy.title, vacansy.salary, vacansy.status)
    else:
        print("Записи не найдены")


if __name__ == "__main__":
    main()
