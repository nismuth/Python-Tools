
# Scientific information on the planets using Britannica Encyclopedia and NASA database

def planet_dict():
    planets = {
        "mercury": {
            "name": "Formerly Apollo the messenger god, later named Mercury, the Roman equivalent.",
            "distance to sun": "57,909,227 km (0.39 AU)",
            "year to Earth standard": "87.97 Earth days",
            "orbit velocity": "47.36 km/sec",
            "radius": "2,439.7 km",
            "mass": "3.30 × 10^23 kg",
            "gravity": "370 cm/sec^2",
            "escape velocity": "4.25 km/sec",
            "inclination to ecliptic": "7.0°",
            "magnetic field strength": "0.003 gauss",
            "Number of moons": "0"
        },
        "venus": {
            "name": "Named Ishtar by ancient Babylonians, now named Venus, Roman goddess of love and beauty.",
            "distance to sun": "108,209,475 km (0.72 AU)",
            "year to Earth standard": "224.7 Earth days",
            "orbit velocity": "35 km/sec",
            "radius": "6,051.8 km",
            "mass": "4.87 × 10^24 kg",
            "gravity": "887 cm/sec^2",
            "escape velocity": "10.4 km/sec",
            "inclination to ecliptic": "3.4°",
            "magnetic field strength": "n/a",
            "Number of moons": "0"
        },
        "earth": {
            "name": "In many cultures comes from the word for ground. English name is from Old English \"Eorthe.\"",
            "distance to sun": "149,598,262 km (1.0 AU)",
            "year to Earth standard": "365.256 days",
            "orbit velocity": "29.78 km/sec",
            "equatorial radius": "6,378.14 km",
            "mass": "5.972 × 10^24 kg",
            "gravity": "980 cm/sec^2",
            "escape velocity": "11.2 km/sec",
            "inclination to ecliptic": "0.00°",
            "magnetic field strength": "0.3 gauss",
            "Number of moons": "1"
        },
        "mars": {
            "name": "Red color lends to violent names: Nergal in Babylonian and Mars in Roman, both gods of war.",
            "distance to sun": "227,943,824 km (1.5 AU)",
            "year to Earth standard": "686.98 Earth days",
            "orbit velocity": "24.1 km/sec",
            "equatorial radius": "3,396.2 km",
            "mass": "6.417 × 10^23 kg",
            "gravity": "371 cm/sec^2",
            "escape velocity": "5.03 km/sec",
            "inclination to ecliptic": "1.85°",
            "magnetic field strength": "n/a",
            "Number of moons": "2"
        },
        "jupiter": {
            "name": "From Roman version of Zeus, Jupiter, the ruler of gods.",
            "distance to sun": "778,340,821 km (5.2 AU)",
            "year to Earth standard": "11.86 Earth years",
            "orbit velocity": "13.1 km/sec",
            "equatorial radius": "71,492 km",
            "mass": "18.98 × 10^26 kg",
            "gravity": "2,479 cm/sec^2",
            "escape velocity": "60.2 km/sec",
            "inclination to ecliptic": "1.3°",
            "magnetic field strength": "4.3 gauss",
            "Number of moons": "66"
        },
        "saturn": {
            "name": "From the Roman god of agriculture Saturn.",
            "distance to sun": "1,426,666,000 km (9.5 AU)",
            "year to Earth standard": "29.45 Earth years",
            "orbit velocity": "9.6 km/sec",
            "equatorial radius": "60,268 km",
            "mass": "5.683 × 10^26 kg",
            "gravity": "896 cm/sec^2",
            "escape velocity": "35.5 km/sec",
            "inclination to ecliptic": "2.49°",
            "magnetic field strength": "0.21 gauss",
            "Number of moons": "62"
        },
        "uranus": {
            "name": "The only planet that retained its Greek name, from Uranus, the personification of heaven.",
            "distance to sun": "2,870,658,000 km (19.2 AU)",
            "year to Earth standard": "84.02 Earth years",
            "orbit velocity": "6.80 km/sec",
            "equatorial radius": "25,559 km",
            "mass": "8.681 × 10^25 kg",
            "gravity": "887 cm/sec^2",
            "escape velocity": "21.3 km/sec",
            "inclination to ecliptic": "0.77°",
            "magnetic field strength": "0.23 gauss",
            "Number of moons": "27"
        },
        "neptune": {
            "name": "From the Roman equivalent of Poseidon, Neptune, the god of the sea.",
            "distance to sun": "4,498,396,000 km (30.1 AU)",
            "year to Earth standard": "164.79 Earth years",
            "orbit velocity": "5.43 km/sec",
            "equatorial radius": "24,764 km",
            "mass": "1.02 × 10^26 kg",
            "gravity": "1,115 cm/sec^2",
            "escape velocity": "23.6 km/sec",
            "inclination to ecliptic": "1.77°",
            "magnetic field strength": "0.14 gauss",
            "Number of moons": "14"
        }
    }
    return planets

def from_sun():
    planet_chart = {
        "mercury": "🔭 2 3 4 5 6 7 8",
        "venus": "1 🔭 3 4 5 6 7 8",
        "earth": "1 2 🔭 4 5 6 7 8",
        "mars": "1 2 3 🔭 5 6 7 8",
        "jupiter": "1 2 3 4 🔭 6 7 8",
        "saturn": "1 2 3 4 5 🔭 7 8",
        "uranus": "1 2 3 4 5 6 🔭 8",
        "neptune": "1 2 3 4 5 6 7 🔭",
    }
    return planet_chart

def main():
    while True:
        use_dict = planet_dict()
        chart = from_sun()

        print("🌍 Welcome to the Planetary Database! 🚀")
        print("\nWhich planet would you like to study?")

        choice = input("Enter here: ").strip().lower()

        if choice in use_dict:
            print(f"\n\t| " + choice.capitalize(), "|", chart[choice])
            for key, value in use_dict[choice].items():
                print(f"  {key.capitalize()}: {value}")
        else:
            print("\n❌ Invalid choice! Please select from:")
            print(", ".join(use_dict.keys()))

        print("\nWould you like more info on the planets? (Y/N)")
        contd = input("Enter here: ").lower()

        if contd == "y":
            continue
        if contd == "n":
            break


main()

