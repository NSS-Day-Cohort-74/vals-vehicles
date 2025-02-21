from vehicles import PassengerVehicle, Jetski, Pontoon, RowBoat

minivan   = PassengerVehicle( 8, "Chrysler", "Pacifica", 2025, 0, 20, "Regular", 110 )
crossover = PassengerVehicle( 5, "Chrysler", "PT Cruiser", 1995, 100, 5, "Regular", 120 )
floater = Pontoon(4, "Brigade", "Zoomer", 1991, 1, "Regular", 1.5)
dinghy = RowBoat(3, "Kizana", "Glarg", 2025, 0.3)
jetski = Jetski(
        max_count=2,
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
floater.drive("Pier West", "Pier East", 4)
dinghy.row("Camp", "Rope Swing", 0.3)

