import json
from driver import Driver

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

print("\n============================")
print("🏎️ F1 DRIVER MANAGER")
print("============================")

while True:

    print("1. Show Drivers")
    print("2. Add Driver")
    print("3. Search Driver")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Showing all drivers...")

        for driver in drivers:
            driver.introduce()

    elif choice == "2":

        driver_name = input("Enter the name of the driver: ")
        team_name = input("Enter the team name: ")

        # Day-29 Exception Handling
        try:
            number = int(input("Enter the driver number: "))

        except ValueError:
            print("Invalid driver number. Please enter a valid integer.")
            continue   # Go back to menu

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

    elif choice == "3":
        print("Search Driver")

        name_to_search = input("Enter the name of the driver to search: ")

        found_driver = False

        for driver in drivers:
            if driver.name.lower() == name_to_search.lower():
                print("\nDriver Found!!\n")
                driver.introduce()
                found_driver = True
                break
            
        if found_driver == False:
            print("No driver found!!")
            break


    elif choice == "4":
        print("Goodbye Race Engineer!")
        break

    else:
        print("Invalid choice! Please choose between 1 and 4.")