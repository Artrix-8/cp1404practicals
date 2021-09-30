"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Get the current fare."""
        return super().get_fare() + self.flagfall
