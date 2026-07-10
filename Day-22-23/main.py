class Driver:
    def __init__(self,name,team,number,wins):
        self.name = name
        self.team = team
        self.number = number
        self.wins = wins

    def introduce(self):
        print(f"Driver: {self.name}")
        print(f"Team: {self.team}")
        print(f"Number: {self.number}")
        
    def drive(self):
        print(f"{self.name} is driving.")

    def pit_stop(self):
        print(f"{self.name} enters the pit lane.")

    def show_wins(self):
        print(f"{self.name} has {self.wins} wins.")

max_driver = Driver("Max Verstappen", "Oracle Redbull Racing", 3, 65)
charles_driver = Driver("Charles Leclerc", "Scuderia Ferrari", 16, 8)
oscar_driver = Driver("Oscar Piastri", "Mcalren F1 Team", 81, 8)

max_driver.introduce()
charles_driver.introduce()
oscar_driver.introduce()
max_driver.drive()
charles_driver.drive()
oscar_driver.drive()
max_driver.pit_stop()
charles_driver.pit_stop()
oscar_driver.pit_stop()
max_driver.show_wins()
charles_driver.show_wins()
oscar_driver.show_wins()

# Today's Learning:

# 1. Classes are the blueprint fro creating objects.
# 2. Objects stores the data of the class and can perform certain actions.
# 3. Methods are function defined inside a class that can perform actions on the objects of that class.
# 4. The __init__ method is a special method that is called when an object is created. 
# 5. Self is a reference to te current object of thr class and is used to access the attributes and methods of the class.git 