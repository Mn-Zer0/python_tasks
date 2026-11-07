import json


class StorageFormatError(Exception):
    pass


def read_json(file):
    try:
        with open(file, encoding="UTF-8") as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as exception:
                raise StorageFormatError("Json decode error") from exception
    except FileNotFoundError as exception:
        raise StorageFormatError("File not found") from exception

    return data
