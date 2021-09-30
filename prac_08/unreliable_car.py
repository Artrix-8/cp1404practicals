"""
CP1404/CP5632 Practical
Unreliable Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes random chance of not driving"""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but have a chance on whether to drive or not."""
        random_chance = randint(1, 100)
        if random_chance >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
