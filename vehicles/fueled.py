class Fueled():
    def __init__(self, current_fuel, fuel_type):
        self.current_fuel = current_fuel
        self.fuel_type = fuel_type

    def fuel(self, chosen_type, quantity):
        if chosen_type == self.fuel_type:
            self.current_fuel = self.current_fuel + quantity
            return

        print("You didn't choosen the right kind of fuel for this vehicle")