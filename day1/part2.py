
def movingSum(path):
    file = open(path, "r")
    a = int(file.readline())
    b = int(file.readline())
    
    line = file.readline()

    while line.strip().isdigit():
        c = int(line)
        yield a + b + c
        a = b
        b = c
        line = file.readline()

    file.close()


increases = 0

last_depth = -1
for depth in movingSum("input.txt"):
    current_depth = int(depth)
    
    if last_depth == -1:
        last_depth = current_depth
        continue

    if current_depth > last_depth:
        increases += 1
    
    last_depth = current_depth

print(increases)
