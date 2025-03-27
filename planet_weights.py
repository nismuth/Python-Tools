# Weight on other planets calculator

print("Find how much you'd weight on other planets.")
while True:
    weight = float(input("Enter your weight: "))
    unit = input("Which unit are you using? (lb/kg): ").lower()

    # Convert pounds to kilograms if needed
    if unit == "lb":
        weight = weight * 0.453592  # 1 lb = 0.453592 kg
    elif unit != "kg":
        print("Invalid unit. Please enter 'lb' or 'kg'.")
        exit()

    print("\nWhich planet do you want to see your weight on?")
    print("Mercury\nVenus\nMars\nJupiter\nSaturn\nUranus\nNeptune")
    planet_choice = input("Enter planet name here: ").title()

    planet_convert = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.14
    }

    if planet_choice in planet_convert:
        new_weight = weight * planet_convert[planet_choice]
        print(f"\nYour weight on {planet_choice} would be: {new_weight:.2f} kg")
    else:
        print("\nPlanet not in database. Please enter a valid planet.")

    restart = input("Would you like to try another planet? (Y/N)").upper()
    if restart == "Y":
        continue
    if restart == "N":
        break

