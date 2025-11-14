# vehicle.py → Contains a base class Vehicle with:
# A class-level dictionary fuel_data = {"car": 10, "bus": 25} (fuel consumption per 100km).
# A method get_fuel_needed(distance, vehicle_type) that calculates and returns fuel usage.

class Vehicle :
    fuel_data = {
        "car" :10, # fuel consumption per 100km it use 10 liter
        "bus" :25
    }

    def get_fuel_needed(self, distance, vehicle_type):

        if vehicle_type in self.fuel_data:
            fuel_use = self.fuel_data[vehicle_type]
            consumption = (distance * 100) / fuel_use
            print(consumption)
            return consumption
        else:
            print(f"vahicle {vehicle_type} Not found ")

#
# demo = Vehicle()
# demo.get_fuel_needed(200 , "car")