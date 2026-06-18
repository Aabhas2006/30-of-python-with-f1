drivers = [
    {"name": "Max Verstappen","team": "Oracle RedBull Racing","number": "3"},
    {"name": "Charles Leclerc","team": "Scuderia Ferrari F1","number": "16"},
    {"name": "Lando Norris","team": "Mclaren F1 Racing","number": "1"}
]

for driver in drivers:
    if driver["name"] == "Charles Leclerc":
        print("Driver Found!")
        print(f"Name: {driver['name']}")
        print(f"Team: {driver['team']}")
        print(f"Number: {driver['number']}")

drivers = [
    {"name": "Max Verstappen", "team": "Red Bull", "wins": 65},
    {"name": "Yuki Tsunoda", "team": "Red Bull", "wins": 0},
    {"name": "Charles Leclerc", "team": "Ferrari", "wins": 8},
    {"name": "Lewis Hamilton", "team": "Ferrari", "wins": 105}
]

for driver in drivers:
    if driver["wins"]> 10:
        print(f"{driver['name']} has {driver['wins']} wins")

# Todays's Learning:
# 1.Printing out one driver from the dictionary.
# 2.Printing data from match.
# 3.Filtering multiple driver using numbers and printing them based on the condition.
# 4.Combining everything that i know.