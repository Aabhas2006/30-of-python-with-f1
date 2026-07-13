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

    @classmethod
    def get_total_drivers(cls):
        return cls.total_drivers

    @staticmethod
    def is_number_valid(number):
        return 1 <= number <= 99

    @staticmethod
    def number_exists(drivers, number):
        for driver in drivers:
            if driver.number == number:
                return True

        return False