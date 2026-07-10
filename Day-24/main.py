class Person:

    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def introduce(self):
        print(f"Name : {self.name}")
        print(f"Nationality : {self.nationality}")

class Driver(Person):

    def __init__(self, name, nationality, team, number):
        super().__init__(name, nationality)
        self.team = team
        self.number = number

    def introduce(self):
        print(f"Driver: {self.name}")
        print(f"Nationality: {self.nationality}")
        print(f"Team: {self.team}")
        print(f"Number: {self.number}")

class championdriver(Driver):

    def __init__(self, name, nationality, team, number, championships):
        super().__init__(name, nationality, team, number)
        self.championships = championships

    def introduce(self):
        print(f"Driver: {self.name}")
        print(f"Nationality: {self.nationality}")
        print(f"Team: {self.team}")
        print(f"Number: {self.number}")
        print(f"Championships: {self.championships}")


         

max_driver = Driver("Max Verstappen", "Dutch", "Oracle Redbull Racing", 3)
charles_driver = Driver("Charles Leclerc", "Monegasque", "Scuderia Ferrari F1", 16)
oscar_driver = Driver("Oscar Piastri", "Australian", "Mclaren F1 Team", 81)
max_champion = championdriver("Max Verstappen", "Dutch", "Oracle Redbull Racing", 3, 4)
lews_champion = championdriver("Lewis Hamilton", "British", "Mercedes AMG Petronas F1 Team", 44, 7)
senna_champion = championdriver("Ayrton Senna", "Brazilian", "McLaren F1 Team", 12, 3)

max_driver.introduce()
charles_driver.introduce()
oscar_driver.introduce()
max_champion.introduce()
lews_champion.introduce()
senna_champion.introduce()

# Today's Learning:
# 1. Inheritance is a way to use the data and properties of one class in another class.
# 2. The super() function is used to call the __init__ method of the parent class.
# 3. The child class can have the data from parent class and also have its own data.
# 4. Inheritance helps us to write the code neatly and avoid coce repetitions.