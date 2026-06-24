file = open("race_report.txt", "r")

context = file.read()

file.close()

print(context)
 
with open("team.txt", "a") as file:
    file.write("\nMclaren")

with open("team.txt", "r") as file:
    data = file.read()

print(data)

# Today's Learnings:
# 1. Now the data can be saved permanently.
# 2. A data can be read(r), write(w) or can be added using append(a) .