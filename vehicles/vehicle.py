class Vehicle():

    def __init__(self, max_count, make, model, year, current_fuel, fuel_type):
        self.max_count = max_count
        self.make = make
        self.model = model
        self.year = year
        self.fuel_type = fuel_type
        self.current_fuel = current_fuel
        self.location = None
        self.trips = []

    def fuel(self, chosen_type, quantity):
        if chosen_type == self.fuel_type:
            self.current_fuel = self.current_fuel + quantity
            return

        print("You didn't choosen the right kind of fuel for this vehicle")

    def store(self, location):
        self.location = location

    def stop(self, final_destination):
        self.location = final_destination
        print(f"I have arrived at {final_destination}")
