"""
Code for testing 'SilverServiceTaxi' class
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi('SSTaxi', 100, 2)
taxi.drive(18)
print(taxi)
print(taxi.get_fare())
