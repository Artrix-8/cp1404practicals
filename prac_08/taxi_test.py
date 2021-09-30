"""
Code for testing 'taxi' class
"""

from prac_08.taxi import Taxi

new_taxi = Taxi("Prius 1", 100, 1.23)  # Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
new_taxi.drive(40)  # Drive the taxi 40 km
print(new_taxi)  # Print the taxi's details and the current fare
print(new_taxi.get_fare())

new_taxi.start_fare()  # Restart the meter (start a new fare) and then drive the car 100 km
new_taxi.drive(100)  # NOTE: taxi doesn't have enough fuel to drive 100km
print(new_taxi)  # Print the details and the current fare
print(new_taxi.get_fare())
