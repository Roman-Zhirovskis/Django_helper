from typing import Dict, TypeVar

K = TypeVar("K")
V = TypeVar("V")


# Example N1
def get_item(key: K, container: Dict[K, V]) -> V:
    return container[key]


def get_first(container: Dict[K, V]) -> K:
    """Ошибки типов возникать не будет, так как возвращаеться один из ключей К"""
    return list(container.keys())[0]


def get_first_v1(container: Dict[K, V]) -> K:
    """Mypy будет вызывать ошибка, каждый раз, когда не будет возвращаться тайп К"""
    return list(
        container.keys()
    )  # mypy raises: Incompatible return value type (got "V", expected "K")


def get_first_v2(container: Dict[K, V]) -> K:
    """Mypy будет вызывать ошибка, каждый раз, когда не будет возвращаться тайп К"""
    return list(container.values())[
        0
    ]  # mypy raises: Incompatible return value type (got "V", expected "K")


if __name__ == "__main__":
    test: Dict[int, int] = {2: 1}
    print(get_item(2, test))
    print(get_first(test))
