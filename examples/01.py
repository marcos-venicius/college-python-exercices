class Vehicle:
    def __init__(self, name: str, max_velocity: float, kilometer_per_liter: float):
        self.name = name
        self.max_velocity = max_velocity
        self.kilometer_per_liter = kilometer_per_liter

    def __str__(self) -> str:
        return f"""
Nome = {self.name}
Velocidade máxima = {self.max_velocity}
Quilômetro por litro = {self.kilometer_per_liter}
"""


class Bus(Vehicle):
    pass

car = Vehicle("Fusca", 180, 10)
bus = Bus("Fusca", 180, 10)

print(car)
print(bus)
