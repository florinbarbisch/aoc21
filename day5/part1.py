def get_hydrothermal_vents(path):
    with open(path, "r") as file:
        for line in file:
            A, B = line.strip().split(" -> ")
            x1, y1 = A.split(",")
            x2, y2 = B.split(",")
            if x1 == x2 or y1 == y2:
                yield (int(x1), int(y1), int(x2), int(y2))
    
sparse_matrix = {} # DOK (Dictionary of keys)
for x1, y1, x2, y2 in get_hydrothermal_vents("input.txt"):
    if x1 == x2:
        step = 1 if y1 < y2 else -1
        for i in range(y1, y2 + step, step):
            if (x1, i) in sparse_matrix:
                sparse_matrix[(x1, i)] += 1
            else:
                sparse_matrix[(x1, i)] = 1
    elif y1 == y2:
        step = 1 if x1 < x2 else -1
        for i in range(x1, x2 + step, step):
            if (i, y1) in sparse_matrix:
                sparse_matrix[(i, y1)] += 1
            else:
                sparse_matrix[(i, y1)] = 1



print(len(list(filter(lambda x: x >= 2, sparse_matrix.values()))))