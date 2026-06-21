drivers = [
    {"name": "Max Verstappen", "team": "Red Bull", "number": 1},
    {"name": "Charles Leclerc", "team": "Ferrari", "number": 16},
    {"name": "Lando Norris", "team": "McLaren", "number": 4}
]

def find_driver(drivers, search_name):
    for driver in drivers:
        if driver["name"] == "Lando Norris":
            return driver

    return None

result = find_driver(drivers, "Lando Norris")

if result is None:
    print("No driver found!")
else:
    print("Driver Found!")
    print(f"Name: {result['name']}")
    print(f"Team: {result['team']}")
    print(f"Number: {result['number']}")

# Today's Learning:
# 1.Using return in a dictionary.
# 2.Using None to return nothing.
# 3.Using returned data to print desired output.
    