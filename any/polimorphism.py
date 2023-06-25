from abc import ABC, abstractclassmethod


class Vehicle(ABC):
    @abstractclassmethod
    def move(self):
        pass

    @abstractclassmethod
    def __str__(self) -> str:
        return "vehicle"

class Car(Vehicle):
    def move(self):
        print('vrumm')

    def __str__(self) -> str:
        return "car"

class Motorcycle(Vehicle):
    def move(self):
        print('yup')

    def __str__(self) -> str:
        return "motorcycle"

def move(vehicle: Vehicle):
    print(f'moving {vehicle}')
    vehicle.move()



move(Car())
move(Motorcycle())