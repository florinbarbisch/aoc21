with open("input.txt", "r") as file:
    polymer = list(file.readline().rstrip())
    pair_count = {}
    for i in range(len(polymer)-1):
        pair = (polymer[i], polymer[i+1])
        pair_count[pair] = 1 if pair not in pair_count else pair_count[pair] + 1
    file.readline() # discard
    line = file.readline()
    insertion_rules = {}
    while line != "":
        pair, element = line.rstrip().split(" -> ")
        insertion_rules[(pair[:1], pair[1:])] = element
        line = file.readline()
    for i in range(40):
        new_pair_count = {}
        for pair, count in pair_count.items():
            inserted_element = insertion_rules[pair]
            for new_pair in [(pair[0], inserted_element), (inserted_element, pair[1])]:
                new_pair_count[new_pair] = count if new_pair not in new_pair_count else new_pair_count[new_pair] + count
        pair_count = new_pair_count
    polymer_by_element = {}
    for pair, count in pair_count.items():
        for element in pair:
            polymer_by_element[element] = count if element not in polymer_by_element else polymer_by_element[element] + count
    polymer_by_element[polymer[ 0]] = polymer_by_element[polymer[ 0]] + 1
    polymer_by_element[polymer[-1]] = polymer_by_element[polymer[-1]] + 1
    for key in polymer_by_element:
        polymer_by_element[key] = polymer_by_element[key] // 2
    quantities = sorted(polymer_by_element.values())
    print(quantities[-1] - quantities[0])
    