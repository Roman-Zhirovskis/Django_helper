from typing import NewType

from typevar_generic_init.base import Cat, Dog, Animal


Animals = NewType("Animals", Animal)  # экземляр должен быть подкласcом Анимался
DogType = NewType("DogType", Dog)  # экземляр должен быть подкласcом Dog

dog1 = Dog("pussa")
cat1 = Cat("byba")

dog2 = Dog("bobik")

# type1 and type2 не выдаст ошибок, так как dog1 и cat1 являются подтипами Animal
type1 = Animals(dog1)
type2 = Animals(cat1)
print(type(type1))

# type3 не выдаст ошибок, так как являются экземпляром Dog
type3 = DogType(dog2)
# type4 выдаст ошибку, так как не являюте экземпляром Dog
type4 = DogType(cat1)

print(type(type1))
