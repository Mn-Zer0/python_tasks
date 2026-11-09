import json
from pathlib import Path


class StorageFormatError(Exception):
    pass


def read_json(file: Path) -> list[dict]:
    try:
        with open(file, encoding="UTF-8") as f:
            try:
                data: list[dict] = json.load(f)
            except json.decoder.JSONDecodeError as exception:
                raise StorageFormatError("Json decode error") from exception
    except FileNotFoundError as exception:
        raise StorageFormatError("File not found") from exception

    return data
