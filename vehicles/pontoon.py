from .vehicle import Vehicle
from .marine_vehicles import MarineVehicle
from .fueled import Fueled

class Pontoon(Vehicle, Fueled, MarineVehicle):
    def __init__(self, max_count, make, model, year, current_fuel, fuel_type, water_speed):
        Vehicle.__init__(self, max_count, make, model, year)
        Fueled.__init__(self, current_fuel, fuel_type)
        MarineVehicle.__init__(self, water_speed)

    def drive(self, start_loc, end_loc, distance):
        self.trips.append(
            {
                'start_location': start_loc,
                'end_location': end_loc,
                'total_distance': distance
            }
        )
        print(f"The {self.make} {self.model} is currently driving from {start_loc} to {end_loc}")
