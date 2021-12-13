with open("input.txt", "r") as file:
    line = file.readline()
    dots = set({})
    while line != "\n":
        x, y = line.rstrip().split(",")
        dots.add((int(x), int(y)))
        line = file.readline()
    fold_instructions = []
    line = file.readline()
    while line != "":
        axis, pos = line.rstrip()[11:].split("=")
        fold_instructions.append((axis, int(pos)))
        line = file.readline()
    for fold_instruction in fold_instructions:
        new_dots = set({})
        axis = fold_instruction[0]
        pos = fold_instruction[1]
        for dot in dots:
            if axis == "x":
                new_dots.add((dot[0] - (dot[0]-pos)*2 if dot[0] > pos else dot[0], dot[1]))
            else:
                new_dots.add((dot[0], dot[1] - (dot[1]-pos)*2 if dot[1] > pos else dot[1]))
        dots = new_dots
        break
    print(len(dots))