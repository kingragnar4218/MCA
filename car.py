# car.py → Contains a class Car that inherits from Vehicle.
# Override the get_fuel_needed method to apply fuel efficiency improvement (divide the base value by 2).
# Add another method car_info() that returns "Car is more fuel efficient.".
from vehicle import Vehicle

class Car(Vehicle) :
    def get_fual_needed(self ,  distance, vehicle_type):
        print("car class ")
        update_fual = super().get_fuel_needed(distance , vehicle_type)

        return update_fual / 2

    def car_info(self):
        return"Car is more fuel efficient."
# aa = Car()
# aa.get_fual_needed(100 , "car")
# print(aa.car_info())

