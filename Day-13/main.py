drivers = [
    {"name": "Max Verstappen", "wins": 65},
    {"name": "Charles Leclerc", "wins": 8},
    {"name": "Lewis Hamilton", "wins": 105}
]

def show_winning_drivers(drivers):
    for driver in drivers:
        if driver["wins"] > 10:
            print(f"{driver['name']} has {driver['wins']} wins")

show_winning_drivers(drivers)

def get_fastest_lap(laps):
    return min(laps)

lap_times = [88.7, 89.1, 88.4, 89.0]

print(get_fastest_lap(lap_times))

# Todaus's Learnings:
# 1.Functions can be used to receive data and also to search particular things from the given data.
# 2.Functions can also be used to return values.
# 3.loops and conditions can be used inside each other while both of them are inside a function.