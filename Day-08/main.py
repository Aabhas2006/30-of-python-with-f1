# def race_intro():
#     print("Race Analysis Report")
#     print("System Ready")
#     print("---------------------")

# race_intro()

def show_drivers(driver):
    print(driver)

show_drivers("Max")
show_drivers("Charles")
show_drivers("lando")

def lap_reports(time):
    print(f"Lap time : {time}")

lap_reports("1:28.675")
lap_reports("1:28.445")
lap_reports("1:28.100")    

# Store multiple drivers in a list and print them one by one using a function.

drivers = ["Max Verstappen", "Charles Leclerc", "Lando Norris", "Lewis Hamilton", "Sebastian Vettel"]

def show_grid(drivers):
    for i in range(len(drivers)):
        print(f"P{i+1}: {drivers[i]}")
    
    print(f"Total Drivers: {len(drivers)}")

show_grid(drivers)

# Today's learnings:
# 1. Functions to print driver names and lap times.
# 2. Using Lists to store multiple drivers and loop through them to display grid positions.
# 3. Accessing list elements using index and calculating total number of drivers using len() function.
