from typing import Dict, TypeVar

T = TypeVar("T", str, int)  # T can only represent types of int and str
V = TypeVar("V", bound=int)  # T can only be an int or subtype of int


def get_first(container: Dict[T, V]) -> T:
    # Кроме того, что возвращаемый тип должен быть ключем ,также str, int
    return list(container.keys())[0]


def get_first_v1(container: Dict[T, V]) -> T:
    # Выдаст ошибку типов
    return tuple(list(container.keys())[0])


def get_first_v2(container: Dict[T, V]) -> T:
    # Выдаст ошибку типов, т.к возвращаем V
    return list(container.values())[0]


if __name__ == "__main__":
    # mypy выдает ошибку типа на уровне передачи значений в функцию
    # Value of type variable "T" of "get_first" cannot be "float"
    # Value of type variable "V" of "get_first" cannot be "str"
    test: Dict[float, str] = {1.0: "1"}
    print(get_first(test))

    # mypy не выдает ошибку
    test2: Dict[str, int] = {"1.0": 1}
    print(get_first(test2))

    # mypy не выдает ошибку
    test3: Dict[int, int] = {1: 1}
    print(get_first(test3))
