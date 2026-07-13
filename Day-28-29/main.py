# F1-Driver-Management-System

import json
from driver import Driver

# Load JSON
with open("driver.json", "r") as file:
    drivers_data = json.load(file)

# Convert dictionaries into Driver objects
drivers = []

for driver_data in drivers_data:
    driver = Driver(
        driver_data["name"],
        driver_data["team"],
        driver_data["number"]
    )

    drivers.append(driver)

# Display drivers
for driver in drivers:
    driver.introduce()

print(f"Total Drivers: {Driver.get_total_drivers()}")

# User Input
driver_name = input("Enter the name of the driver: ")
team_name = input("Enter the team name: ")

# Day-29  
try:
    number = int(input("Enter the driver number: "))

except ValueError:
    print("Invalid driver number. Please enter a valid integer.")
    exit()

finally:
    print("Driver number validation complete.")

# Validation
if not Driver.is_number_valid(number):

    print("Invalid driver number.")

elif Driver.number_exists(drivers, number):

    print("Driver number already exists.")

else:

    new_driver = Driver(driver_name, team_name, number)

    drivers.append(new_driver)

    new_driver_data = {
        "name": driver_name,
        "team": team_name,
        "number": number
    }

    drivers_data.append(new_driver_data)

    with open("driver.json", "w") as file:
        json.dump(drivers_data, file, indent=4)

    print("Driver added successfully!")

print(f"Total Drivers: {Driver.get_total_drivers()}")

# Wrote my 1st ever python program using OOPs concept. Learned about class, instance variables, class variables, instance methods, class methods and static methods.