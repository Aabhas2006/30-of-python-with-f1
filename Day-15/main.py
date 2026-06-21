drivers = []

def add_driver(drivers, name, team, number):
    driver = {
        "name": name,
        "team": team,
        "number": number
    }

    drivers.append(driver)

add_driver(drivers,"Max Vertsappen", "Oracle Redbull Racing", 1)
add_driver(drivers,"Charles leclerc", "Scuderia Ferrari F1", 16)
add_driver(drivers,"Lando Norris", "Mclaren F1 Racing", 4)

def show_grid(drivers):
    for i in range(len(drivers)):
        driver = drivers[i]
        print(f"P{i+1} : {driver['name']} #{driver['number']}")


print(len(drivers))
show_grid(drivers)

# Today's learnings:
# 1.Create data.
# 2.Using append to store dictionary records in a list.
# 3.Counted the records present in the lists.
# 4.Displayed the records using functions in a driver's position manner.
# 5.Accessed more than 1 field in the output.  