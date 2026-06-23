drivers = []

def add_driver(drivers,name):
    driver = {
        "name": name
    }

    drivers.append(driver)

add_driver(drivers, "Max Verstappen")
add_driver(drivers, "Lando Norris")
add_driver(drivers, "Charles Leclerc")

def show_grid(drivers):
    for i in range(len(drivers)):
        driver = drivers[i]
        print(f"P{i+1} : {driver['name']} ")

show_grid(drivers)


def delete_driver(drivers, search_name):
    for driver in drivers:
        if driver["name"] == search_name:
            drivers.remove(driver)
            return driver

    return None

result = delete_driver(drivers, "Lando Norris")

print("After deleting a driver")

if result is None:
    print("No driver Found!")
else:
    print("Driver Found!")

print(len(drivers))

# Today's Learning:
# 1.CRUD completed by learning to CREATE dictionary, READ dictionary, UPDATE dictionary , DELETE dictionary.
