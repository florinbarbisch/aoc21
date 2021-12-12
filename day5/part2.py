def get_hydrothermal_vents(path):
    with open(path, "r") as file:
        for line in file:
            P1, P2 = line.strip().split(" -> ")
            x1, y1 = map(int, P1.split(","))
            x2, y2 = map(int, P2.split(","))
            yield x1, y1, x2, y2

sparse_matrix = {} # DOK (Dictionary of keys)
for x1, y1, x2, y2 in get_hydrothermal_vents("input.txt"):
    step_x = 0 if x1==x2 else (1 if x1 < x2 else -1)
    step_y = 0 if y1==y2 else (1 if y1 < y2 else -1)
    distance = abs(x2-x1) if x1!=x2 else abs(y2-y1)
    for i in range(distance+1):
        key = (i*step_x + x1, i*step_y + y1)
        sparse_matrix[key] = sparse_matrix[key] + 1 if key in sparse_matrix else 1

print(len(list(filter(lambda x: x >= 2, sparse_matrix.values()))))