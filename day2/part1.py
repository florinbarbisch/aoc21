file = open("input.txt", "r")

depth = 0
forward = 0

for line in file:
    command, x = line.split(" ");
    x = int(x)
    if command == "forward":
        forward += x
    elif command == "down":
        depth += x
    elif command == "up":
        depth -= x

print(f"forward = {forward}")
print(f"depth = {depth}")
print(f"forward * depth = {forward * depth}")

file.close()