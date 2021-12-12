with open("input.txt", "r") as file:
    fish_dict = {i: 0 for i in range(9)}
    for fish in file.readline().split(","):
        fish_dict[int(fish)] += 1
    for day in range(256):
        fish_0 = fish_dict[0]
        for i in range(1, 9):
            fish_dict[i-1] = fish_dict[i]
        fish_dict[8] = fish_0
        fish_dict[6] += fish_0
    print(sum(fish_dict.values()))