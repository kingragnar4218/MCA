# Task Requirement
# Create three files:
# vehicle.py → Contains a base class Vehicle with:
# A class-level dictionary fuel_data = {"car": 10, "bus": 25} (fuel consumption per 100km).
# A method get_fuel_needed(distance, vehicle_type) that calculates and returns fuel usage.
# car.py → Contains a class Car that inherits from Vehicle.
# Override the get_fuel_needed method to apply fuel efficiency improvement (divide the base value by 2).
# Add another method car_info() that returns "Car is more fuel efficient.".
# bus.py → Contains a class Bus that inherits from Vehicle.
# Override the get_fuel_needed method to apply extra fuel usage (multiply the base value by 1.5).
# Add another method bus_info() that returns "Bus consumes more fuel for same distance.".
# Create a main file main.py that:
# Imports Vehicle from vehicle.py, Car from car.py, and Bus from bus.py.
# Creates objects for Car and Bus.
# Calls get_fuel_needed(200, "car") and get_fuel_needed(200, "bus").
# Prints out the results.
# Shows the difference between calling the base class method via super() and the overridden method.
# Updates the fuel_data dictionary dynamically (e.g., change car from 10 to 8) and shows how it affects results.

from vehicle import Vehicle
from car import  Car
from bus import Bus

# print("------- Vehicle class -------")
# v1 = Vehicle
# v1.get_fuel_needed(200 , "car")


print("\n ------- Car class -------")
c1 = Car()
c1.get_fual_needed(200 , "car")
c1.car_info()

print("\n------- Bus class -------")
b1 = Bus()
b1.get_fuel_needed(100, "bus")

