#!/usr/bin/env python3

class Salary:
    def __init__(self, base: int, bonus: int) -> None:
        self.base = base
        self.bonus = bonus

    def annual_salary(self) -> float:
        return self.base * 12 + self.bonus


class Employee:
    def __init__(self, name: str, age: int, salary: Salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self) -> str:
        return f'{self.name}, {self.age} years old'

    def total_salary(self) -> float:
        return self.salary.annual_salary()


if __name__ == '__main__':
    salary = Salary(3500, 0)
    employee = Employee('Marcos', 21, salary)
    total_salary = employee.total_salary()

    print(employee)
    print(f'total salary: {total_salary}')
