lap_times = [90.5, 90.4, 89.7, 89.9, 90.2]

average_lap_time = sum(lap_times) / len(lap_times)

print("🏁 Race Analysis Report 🏁")
print(f"Total Laps: {len(lap_times)}")
print(f"Total Time: {sum(lap_times)}")
print(f"Average Lap Time: {average_lap_time:.2f}")
print(f"Fastest Lap: {min(lap_times)}")
print(f"Slowest Lap: {max(lap_times)}")

# Day 5 learnings 
# sum()function ,len()function,min()function,max()function
# Number formatting with f-strings and :.2f for 2 decimal places