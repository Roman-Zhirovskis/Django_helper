from typing import Dict, Generic, TypeVar

T = TypeVar("T")


class Registry(Generic[T]):
    def __init__(self) -> None:
        self._store: Dict[str, T] = {}

    def set_item(self, k: str, v: T) -> None:
        self._store[k] = v

    def get_item(self, k: str) -> T:
        return self._store[k]


if __name__ == "__main__":
    # Определяем тип объека для классов
    family_name_reg = Registry[str]()
    family_age_reg = Registry[int]()

    family_name_reg.set_item("husband", "steve")
    family_name_reg.set_item("dad", "john")
    # Выдаст ошибку типов
    family_name_reg.set_item("boba", 1)

    family_age_reg.set_item("steve", 30)
    # Выдаст ошибку типов
    family_age_reg.set_item("steve", "30")
