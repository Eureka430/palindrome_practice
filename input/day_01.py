#Part 1
with open('day_01.txt', 'r') as file_object:
    instructions = file_object.read()
floor = 0
for char in instructions:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

print(floor)

#Part 2
with open('day_01.txt', 'r') as file_object:
    instructions = file_object.read()
floor = 0
for i, char in enumerate(instructions):
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

    if floor == -1:
        print(i + 1)
        break


