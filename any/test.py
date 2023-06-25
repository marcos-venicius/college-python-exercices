from abc import ABC, abstractclassmethod


class Conta(ABC):
    def __init__(self):
        pass

    @abstractclassmethod
    def balance():
        pass


const = Conta()
