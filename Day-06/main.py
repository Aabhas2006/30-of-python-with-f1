lap_times=[]

# lap1 = float(input("Enter lap time: "))
# lap_times.append(lap1)

# print(lap_times)

for lap in range(1,4):
    lap_time = float(input("Enter lap time:"))
    lap_times.append(lap_time)

print("Race Analysis Report")
print(lap_times)
print(f"Total Laps: {len(lap_times)}")
print(f"Total Time: {sum(lap_times)}")
print(f"Average Lap time: {sum(lap_times)/len(lap_times):.2f}")
print(f"Fastest Lap: {min(lap_times)}")
print(f"Slowest Lap:{max(lap_times)}")

# Today's learnings:
# 1.Creating an empty list 
# 2.Adding data using append() method
# 3.Using a for Loop to get multiple inputs