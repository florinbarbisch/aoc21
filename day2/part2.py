file = open("input.txt", "r")

depth = 0
forward = 0
aim = 0

for line in file:
    command, x = line.split(" ");
    x = int(x)
    if command == "forward":
        forward += x
        depth += aim * x
    elif command == "down":
        aim += x
    elif command == "up":
        aim -= x

print(f"forward * depth = {forward * depth}")

file.close()