drivers = []

def add_driver(drivers, name, team, number):
    driver = {
        "name":name,
        "team": team,
        "number": number
    }

    drivers.append(driver)

add_driver(drivers,"Max Vertsappen", "Oracle Redbull Racing", 1)
add_driver(drivers,"Charles leclerc", "Scuderia Ferrari F1", 16)
add_driver(drivers,"Lando Norris", "Mclaren F1 Racing", 4)

def update_driver(drivers, search_name, new_number, new_name):
    for driver in drivers:
        if driver["name"] == search_name:
            driver["number"] = new_number,
            driver["name"] == new_name

update_driver(drivers, "Lando Norris", 81, "Oscar Piastri")

def show_grid(drivers):
    for i in range(len(drivers)):
        driver = drivers[i]
        print(f"P{i+1} : {driver['name']} #{driver['number']}")

show_grid(drivers)