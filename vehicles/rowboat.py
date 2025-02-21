from .vehicle import Vehicle
from .marine_vehicles import MarineVehicle

class RowBoat(Vehicle, MarineVehicle):
    def __init__(self, max_count, make, model, year, water_speed):
        Vehicle.__init__(self, max_count, make, model, year)
        MarineVehicle.__init__(self, water_speed)

    def row(self, start_loc, end_loc, distance):
        self.trips.append(
            {
                'start_location': start_loc,
                'end_location': end_loc,
                'total_distance': distance
            }
        )
        print(f"The {self.make} {self.model} is currently row from {start_loc} to {end_loc}")
