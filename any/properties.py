#!/usr/bin/env python3

class Bank:
    def __init__(self):
        self.__balance = 0.0

    def withdrawal_value(self, value: float) -> bool:
        if self.__balance >= value:
            self.__balance -= value
            return True

        return False

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> bool:
        if value < 0:
            return False

        self.__balance += value

        return True


bank = Bank()

bank.balance = 100
bank.balance = 100

bank.withdrawal_value(50)

print(bank.balance)
