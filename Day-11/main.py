drivers = [
    {"name": "Max Verstappen", "team": "Oracle RedBull Racing"},
    {"name": "Charles Leclerc", "team": "Scuderia Ferrari F1"},
    {"name": "Lando Norris", "team": "Mclaren Racing"},    
]

for driver in drivers:
    print(f"Driver: {driver['name']}")
    print(f"Team: {driver['team']}")

def show_grid(drivers):
    for i in range(len(drivers)):
        driver = drivers[i]
        print(f"P{i+1} : {driver['name']}")

show_grid(drivers)

# Today's Learning:
# 1. List can contain dictionaries.
# 2. A desired output can be accessed using loops through dictionary.
# 3. Functions,loops,indexes and dictionaries can be combined to get a more structured output. Like the grid positions output.