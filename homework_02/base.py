from abc import ABC
from homework_02 import exceptions
import logging


LOGGER = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight | 0
        self.started = False
        self.fuel = fuel | 0
        self.fuel_consumption = fuel_consumption | 0

    def start(self):
        if self.started is False:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError('Не хватает топлива для завода')
        LOGGER.info('Машина заведена')

    def move(self, km: int):
        used_fuel = self.fuel_consumption * km
        if used_fuel <= self.fuel:
            self.fuel -= used_fuel
        else:
            raise exceptions.NotEnoughFuel('Не хватает топлива для преодоления дистанции')
