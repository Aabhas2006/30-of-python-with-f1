with open("lap.txt", "r") as file:
    lap_number = 1

    for lap in file:
        print(f"Lap {lap_number}: {lap.strip()}")
        lap_number += 1