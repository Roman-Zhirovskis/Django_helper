from typing import Generic, TypeVar

from base import Cat, Dog, Person, Animal


Residents = TypeVar("Residents")


class House(Generic[Residents]):
    residents: list[Residents] = []


if __name__ == "__main__":
    animals_house = House[Animal]()
    humans_house = House[Person]()

    dog = Dog("Rex")
    cat = Cat("Tom")
    person = Person("John")

    animals_house.residents.append(dog)
    animals_house.residents.append(cat)
    # animals_house.residents.append(person) - выдает ошибку типов, т.к person не являеться дочерним классом Animals

    humans_house.residents.append(person)
    # humans_house.residents.append(cat) - выдает ошибку типов, т.к person не являеться дочерним классом Person
