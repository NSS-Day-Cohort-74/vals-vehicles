from .vehicle import Vehicle
from .marine_vehicles import MarineVehicle
from .ground_vehicle import GroundVehicle
from .fueled import Fueled


class DuckBoat(Vehicle, Fueled, GroundVehicle, MarineVehicle):
    def __init__(self, max_count, make, model, year, current_fuel, fuel_type, water_speed, ground_speed):
        Vehicle.__init__(self, max_count, make, model, year)
        Fueled.__init__(self, current_fuel, fuel_type)
        MarineVehicle.__init__(self, water_speed)
        GroundVehicle.__init__(self, ground_speed)

