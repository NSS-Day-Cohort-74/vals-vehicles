from .vehicle import Vehicle
from .fueled import Fueled

class Jetski(Vehicle):

    def __init__(self, max_count, cc, make, model, year, mileage, current_fuel, fuel_type):
        Vehicle.__init__(self, max_count, make, model, year)
        Fueled.__init__(self, current_fuel, fuel_type)
        self.mileage = mileage
        self.cc = cc

    def drive(self, start_loc, end_loc, distance):
        self.trips.append(
            {
                'start_location': start_loc,
                'end_location': end_loc,
                'total_distance': distance
            }
        )
        print(f"The {self.make} {self.model} is currently driving from {start_loc} to {end_loc}")
