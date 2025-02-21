class Vehicle():

    def __init__(self, max_count, make, model, year):
        self.max_count = max_count
        self.make = make
        self.model = model
        self.year = year
        self.location = None
        self.trips = []

    def store(self, location):
        self.location = location

    def stop(self, final_destination):
        self.location = final_destination
        print(f"I have arrived at {final_destination}")
