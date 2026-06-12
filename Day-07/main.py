Lap_times = []

for lap in range(1,6):
    Lap_time = float(input("Enter Lap time: "))
    Lap_times.append(Lap_time)
    fastest_lap_time = min(Lap_times)
    fastest_lap_Number = Lap_times.index(fastest_lap_time) + 1

print(f"Fastest lap time: {fastest_lap_time:.2f}")
print(f"FastestLap {fastest_lap_Number} time: {fastest_lap_time:.2f}")

# Today's learnings:
# 1.min() function for fastest lap 
# 2. index() function to find the index(position) of the fastest lap time
# 3. Adding 1 to the index to get lap number(Default inex starts from 0)
# 4. Combinig loops,Inputs and lists functions .