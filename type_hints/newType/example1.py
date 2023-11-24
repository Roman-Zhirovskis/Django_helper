from typing import NewType


DogId = NewType("DogId", int)
UserId = NewType("UserId", int)

# Пример использования
some_dog_id = DogId(12345)
some_user_id = UserId(524313)


# Проверка типов
def get_dog_name(dog_id: DogId) -> str:
    return f"Dog with ID {dog_id}"


def get_user_name(user_id: UserId) -> str:
    return f"User with ID {user_id}"


# Проверка вызовов функций
print(get_dog_name(some_dog_id))  # Выведет "Dog with ID 12345"
print(get_user_name(some_user_id))  # Выведет "User with ID 524313"

# Попытка передать неверный тип
# Ниже строки вызовут ошибку статического анализатора типов
user_a = get_user_name(12345)  # Не типизированный int не является UserId
# user_b = get_user_name(UserId("invalid"))  # Не типизированная строка не является UserId
