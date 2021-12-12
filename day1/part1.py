file = open("input.txt", "r")

increases = 0

last_depth = -1
for depth in file:
    current_depth = int(depth)
    
    if last_depth == -1:
        last_depth = current_depth
        continue

    if current_depth > last_depth:
        increases += 1
    
    last_depth = current_depth

print(increases)
file.close()
