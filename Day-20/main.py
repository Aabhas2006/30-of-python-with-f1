try:
    lap = float(input("Enter the Lap time:"))
    print(f"Lap Time: {lap}")

except ValueError:
    print("Invalid lap time!")

print("Session Ended")

# Today Learning's:

# 1. Try is used to attempt this code.
# 2. Except is used in case of error comes then it handles the error output.
# 3.Program will not crash and the except output will be produced. A more systematic output of an error.