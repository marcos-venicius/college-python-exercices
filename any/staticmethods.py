#!/usr/bin/env python3

from datetime import date


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birthdate_year(clazz, name: str, year: int):
        return clazz(name, date.today().year - year)

    @staticmethod
    def is_of_legal_age(age: int) -> bool:
        return age >= 18


person1 = Person("Maria", 26)
person2 = Person.from_birthdate_year('Ana', 2006)

print(person1.age)
print(person2.age)

print(Person.is_of_legal_age(18))

