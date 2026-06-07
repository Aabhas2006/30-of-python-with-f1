#input function 

lap1 = float(input("Enter lap 1 time: "))
lap2 = float(input("Enter lap 2 time: "))
lap3 = float(input("Enter lap 3 time:"))

# print(f" Lap 1 time: {lap1} seconds")
# print(f" Lap 2 time: {lap2} seconds")
# print(f" Lap 3 time: {lap3} seconds")

if lap1 < lap2 and lap1 < lap3:
    print("Lap 1 was the fastest")

elif lap2 < lap1 and lap2 < lap3:
    print("Lap 2 was the fastest")

else :
    print("Lap 3 was the fastest")