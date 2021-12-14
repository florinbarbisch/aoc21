with open("input.txt", "r") as file:
    polymer = list(file.readline().rstrip())
    file.readline() # discard
    line = file.readline()
    insertion_rules = {}
    while line != "":
        pair, element = line.rstrip().split(" -> ")
        insertion_rules[(pair[:1], pair[1:])] = element
        line = file.readline()
    for i in range(10):
        new_polymer = [polymer[0]]
        for i in range(1, len(polymer)):
            new_polymer.append(insertion_rules[(polymer[i-1], polymer[i])])
            new_polymer.append(polymer[i])
        polymer = new_polymer
    polymer_by_element = {}
    for element in polymer:
        polymer_by_element[element] = 1 if element not in polymer_by_element else polymer_by_element[element] + 1
    quantities = sorted(polymer_by_element.values())
    print(quantities[-1] - quantities[0])
    