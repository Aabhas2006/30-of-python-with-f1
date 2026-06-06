#For loop
print("Race Started")
for lap in range(1, 7):
    print(f"Lap {lap}")

    if lap == 5:
        print("BOX! BOX! BOX!") #indentation is important in python, it defines the scope of the loop or condition

# print("Chequeered Flag!")

#BONUS CHALLENGE 
for lap in range(1, 7):

    if lap == 5:
        print(f"Lap {lap} - Fuel LOW")
    
    elif lap == 6:
        print(f"Lap {lap} - BOX! BOX! BOX!")
    
    else:
        print(f"Lap {lap} - Fuel OK")

for lap in range(3):
    print(f"Lap {lap}")