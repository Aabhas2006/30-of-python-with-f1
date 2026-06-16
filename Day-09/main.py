lap_times = [90.5,89.8,90.1,89.7,90.2]

def lap_count(lap_times):
    return len(lap_times)

def fastest_lap(lap_times):
    return min(lap_times)

def slowest_lap(lap_times):
    return max(lap_times)

def average_lap(lap_times):
    return sum(lap_times)/len(lap_times)

print('RACE ANALYSIS')
print(f"Total Lap : {lap_count(lap_times)}")
print(f"Fastest lap : {fastest_lap(lap_times)}")
print(f"Slowest lap : {slowest_lap(lap_times)}")
print(f"Average lap : {average_lap(lap_times):.2f}")


# Today's Learning :

# 1. Using function for calculations.
# 2. Functions can take entire lists as an outputs
# 3. Using return to get results back   