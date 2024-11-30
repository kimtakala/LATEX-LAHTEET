from typing import Optional, TypeVar


T = TypeVar("T")


class UserInputError(Exception):
    pass


def try_parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def first_item(lst: list[T]) -> Optional[T]:
    if len(lst) == 0:
        return None

    return lst[0]
