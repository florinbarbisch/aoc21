file = open("input.txt", "r")

width = len(file.readline().strip()) # get the width of one line

zeros = [0 for i in range(width)]
total = 0

for line in file:
    total += 1
    bits = list(line)
    for i in range(width):
        if bits[i] == "0":
            zeros[i] += 1

gamma   = ""
epsilon = ""
for zero in zeros:
    gamma   += "0" if zero > total / 2 else "1"
    epsilon += "0" if zero < total / 2 else "1"

print(int(gamma, base=2) * int(epsilon, base=2))

file.close()