from dataclasses import field
from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


class Status(StrEnum):
    OPEN = "open"
    CLOSED = "closed"


class VacancyFormatError(Exception):
    pass


class ValidatedVacancy(BaseModel):
    id: int = Field(gt=0, description="Положительный ID вакансии")
    title: str = Field(min_length=1, max_length=200, description="Название вакансии")
    salary: int = Field(ge=0, description="Зарплата, не может быть отрицательной")
    status: Status = Field(description="Статус: open или closed")

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("title не может быть пустым (только пробелы)")
        return v.strip()


def filter_records(
    records: list[ValidatedVacancy], rule, *, key: str, value: str, limit=None
) -> list[ValidatedVacancy]:
    # print(records)
    filtered = []
    # filtered = [record for record in records if rule(record[key], value)]
    for record in records:
        attr = getattr(record, key)
        if rule(attr, value):
            filtered.append(record)
    if limit is None:
        return filtered
    else:
        return filtered[:limit]


def is_rule(record_key: str, value: str) -> bool:
    return record_key == value


def validate(data: list):
    for record in data:
        # print(record, "\n")
        required = ["id", "title", "salary", "status"]
        missing = None
        for i in required:
            if i not in record:
                missing = i

        if missing:
            raise VacancyFormatError(f"Прощено поле {missing}")


# 03.1.2 dataclass
# @dataclass
class VacancyDataClass:
    ID: int
    title: str
    salary: int
    status: str
    info: list[str] = field(default_factory=list)

    def close(self) -> None:
        self.status = Status.CLOSED

    def open(self) -> None:
        self.status = Status.OPEN


class Vacancy:
    def __init__(self, ID, title, salary, status):
        self.ID = ID
        self.title = title
        self.salary = salary
        self.status = status
        self.info = []

    def close(self):
        self.status = Status.CLOSED

    def open(self):
        self.status = Status.OPEN


def to_vacancy(raw: ValidatedVacancy) -> Vacancy:
    """Преобразует валидированную внешнюю модель в доменную сущность."""
    return Vacancy(
        ID=raw.id,
        title=raw.title,
        salary=raw.salary,
        status=raw.status,
    )
