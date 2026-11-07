class VacancyFormatError(Exception):
    pass


def filter_records(records, rule, *, key, value, limit=None):
    # print(records)
    filtered = [record for record in records if rule(record[key], value)]
    if limit is None:
        return filtered
    else:
        return filtered[:limit]


def is_rule(record_key, value):
    return record_key == value


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
