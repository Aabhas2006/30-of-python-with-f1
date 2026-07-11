import json

with open("drivers.json", "r") as file:
    drivers = json.load(file)

print(drivers)

new_drivers = { "name": "Lewis Hamilton", "team": "Mercedes AMG Petronas F1 Team", "number": 44 }

drivers.append(new_drivers)

with open("drivers.json", "w") as file:
    json.dump(drivers, file, indent=4)


# Today's Learnings:
# 1. Json is used to store python data.
# 2. json.load() is used to read the data from json file.
# 3. json.dump() is used to write the data into json file.
# 4. indent=4 is used to format the json data in a readable way.
# 5. We use append() to add new data into the existing data.
# 6. we use "w" instead of "a" to append the data into existing data.
# 7. Unlike python, json data is stored even when the program is closed.
