from .fueled import Fueled
from .vehicle import Vehicle
from .ground_vehicle import GroundVehicle

class PassengerVehicle(Vehicle, Fueled, GroundVehicle):

    def __init__(self, max_count, make, model, year, mileage, current_fuel, fuel_type, ground_speed):
        Vehicle.__init__(self, max_count, make, model, year)
        Fueled.__init__(self, current_fuel, fuel_type)
        GroundVehicle.__init__(self, ground_speed)
        self.mileage = mileage

    def drive(self, start_loc, end_loc, distance):
        self.trips.append(
            {
                'start_location': start_loc,
                'end_location': end_loc,
                'total_distance': distance
            }
        )
        print(f"The {self.make} {self.model} is currently driving from {start_loc} to {end_loc}")
