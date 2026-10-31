

class VacancyFormatError(Exception):
    pass


def validate(data):
    for record in data:
        # print(record, "\n")
        required = ["id", "title", "salary", "status"]
        missing = None
        for i in required:
            if i not in record:
                missing = i

        if missing:
            raise VacancyFormatError(f"Прощено поле {missing}")


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