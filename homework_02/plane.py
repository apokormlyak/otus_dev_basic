"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, kg: int):
        new_cargo = self.cargo + kg
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise exceptions.CargoOverload('Перегруз')

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
