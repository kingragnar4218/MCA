# bus.py → Contains a class Bus that inherits from Vehicle.
# Override the get_fuel_needed method to apply extra fuel usage (multiply the base value by 1.5).
# Add another method bus_info() that returns "Bus consumes more fuel for same distance.".

from vehicle import Vehicle

class Bus(Vehicle):
    def get_fuel_needed(self , distance, vehicle_type):
        print("bus class")
        get_fuel = super().get_fuel_needed(distance , vehicle_type)
        add_fuel = get_fuel * 1.5
        return add_fuel


#
# bb = Bus()
# bb.get_fuel_needed(33 , 'bus')