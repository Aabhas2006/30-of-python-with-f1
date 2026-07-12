# Instance methods, Class methods, and Static methods.

class Driver :
    season = 2026
    total_drivers = 0

    def __init__(self, name, team, number) :
        self.name = name
        self.team = team
        self.number = number
        Driver.total_drivers += 1

    def introduce(self) :
        print(f"Driver: {self.name}")
        print(f"Team: {self.team}")
        print(f"Season: {Driver.season}")
        print(f"Number: {self.number}")

    @classmethod
    def get_total_drivers(cls) :
        return cls.total_drivers

    @staticmethod
    def is_valid_number(number) :
       return 1 <= number <= 99
        

max = Driver("Max Verstappen", "Oracle Redbull Racing", 3)
charles = Driver("Charles Leclerc", "Scuderia Ferrari F1", 16)
oscar = Driver("Oscar Piastri", "Mclaren F1 Team", 81)

max.introduce()
charles.introduce()
oscar.introduce()

print(f"Total Drivers: {Driver.get_total_drivers()}")
print(f"Is 3 a valid number? {Driver.is_valid_number(3)}")
print(f"Is 100 a valid number? {Driver.is_valid_number(100)}")
        
# Today's Learning:
# 1. Instance methods are used to access and modify instance variables.
# 2. Class methods are used to access and modify class variables.
# 3. Static methods is used to help the class without disturbing the class variables or instance variables.
# 4. Class methods are defined using @classmethod and static methods are defined using @staticmethod.