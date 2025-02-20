
# 3. Small boats
# 4. Small planes
# 5. Motorocycles

from vehicles import PassengerVehicle, Jetski

minivan = PassengerVehicle( 8, "Chrysler", "Pacifica", 2025, 0, 20, "Regular" )
crossover = PassengerVehicle( 5, "Chrysler", "PT Cruiser", 1995, 100, 5, "Regular" )
jetski = Jetski(
        max_count= 2,
        cc=1000,
        fuel_type="Premium",
        make="Ford",
        mileage=300,
        year=2012,
        current_fuel=8,
        model="Water Rat",
    )

minivan.drive("Tokyo", "Baltimore", 1800)
crossover.drive("Nashville", "Memphis", 200)
jetski.drive("Corolla", "Charleston", 60)

