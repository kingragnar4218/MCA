# Problem
# We want to model a transport system with different vehicle types.
# Requirements
# Create a base class Vehicle with methods:
# start() → prints "Vehicle started"
# stop() → prints "Vehicle stopped"
# Create subclasses:
# Bus
# method: passenger_capacity(capacity) → prints "This bus can carry X passengers"
# Truck
# method: load(weight) → prints "This truck can carry X tons of load"
# Bike
# method: type_of_bike(bike_type) → prints "This is a <bike_type> bike"
# Create objects of each subclass and call their methods.
# ✅ Key Changes
# Added fuel consumption parameter to start( ) in Vehicle.
# Each subclass passes fuel consumed divided by 5 (fuel_consumed/5) when calling super().start().
# Bus, Truck, Bike methods now accept fuel_consumed as parameter.
# Add class ElectricBus which inherit bus - also uses super().start(fuel_consumed/5) before its custom start message.
from more_itertools.more import permutation_index


class vehicle :

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

class bus(vehicle):
    def passenger_capacity(self , capacity):
        print(f"This bus can carry {capacity} passengers")

class truck(vehicle):
    def load(self , weight):
        print(f"This truck can carry {weight} tons of load")

class bike(vehicle):
    def type_of_bike(self , bike_type):
        print(f"This is a {bike_type} bike")

print("----- bus class ------")
b1 = bus()
b1.start()
b1.passenger_capacity(50)
b1.stop()

print("\n----- truck class ------")
t1 = truck()
t1.start()
t1.load(200)
t1.stop()

print("\n----- bike class ------")
bike = bike()
bike.start()
bike.type_of_bike("gt650")
bike.stop()



class vehicle1:

    def start(self, fuel_consumed):
        print(f"Vehicle started. Fuel consumed: {fuel_consumed} liters")

    def stop(self):
        print("Vehicle stopped")


class bus1(vehicle1):
    def passenger_capacity1(self, capacity):
        print(f"This bus can carry {capacity} passengers")

    def start(self , fuel_bus):
        super().start(fuel_bus / 5)

class electricbus(bus1):
    def start(self , fuel_bus):
        print("this is electricbus so it not required fuel")
        super().start(fuel_bus / 5)


class truck1(vehicle1):
    def load(self, weight):
        print(f"This truck can carry {weight} tons of load")


    def start(self, fuel_truck ):
        super().start(fuel_truck / 5)

class bike1(vehicle1):
    def type_of_bike(self , bike_type):
        print(f"This is a {bike_type} bike")

    def start(self, fuel_bike):
        super().start(fuel_bike / 5)

print("\n----- updated bus class ------")
bus_update = bus1()
bus_update.start(100)
bus_update.passenger_capacity1(50)
bus_update.stop()

print("\n----- updatedel ectricbus class ------")
ev = electricbus()
ev.start(20)
ev.passenger_capacity1(1000)
ev.stop()


print("\n----- updated truck class ------")
truck_update = truck1()
truck_update.start(200)
truck_update.load(1000)
truck_update.stop()


print("\n----- updated bike class ------")
bike_update = bike1()
bike_update.start(50)
bike_update.type_of_bike("gt650")
bike_update.stop()


