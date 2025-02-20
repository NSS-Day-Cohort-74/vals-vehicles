from .vehicle import Vehicle

class Jetski(Vehicle):

    def __init__(self, max_count, cc, make, model, year, mileage, current_fuel, fuel_type):
        super().__init__(max_count, make, model, year, current_fuel, fuel_type)
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
