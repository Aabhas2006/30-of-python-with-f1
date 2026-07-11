# Class variables, Class methods, and static methods in Python

class Driver:
    season = 2026
    total_drivers = 0

    def __init__(self, name, team, number):
        self.name = name
        self.team = team
        self.number = number
        Driver.total_drivers += 1

    def introduce(self):
        print(f"Driver: {self.name}")
        print(f"Team: {self.team}")
        print(f"Number: {self.number}")
        print(f"Season: {Driver.season}")

max = Driver("Max Verstappen", "Oracle Redbull Racing", 3)
charles = Driver("Charles Leclerc", "Scuderia Ferrari F1", 16)
oscar = Driver("Oscar Piastri", "Mclaren F1 Team", 81)

max.introduce()
charles.introduce()
oscar.introduce()

print(f"Total drivers: {Driver.total_drivers}")

# Today's Learning:
# 1. Class variables stores the data that is shared among all instances of a class.
# 2. Class variables do not use self().
# 3. Class methods are used to access and modify class variables.
# 4. Static methods are actions that apply to the class without accessing or modifying class variables.