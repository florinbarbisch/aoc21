path = "input.txt"
days = 80
with open(path, "r") as file:
    fish_list = list(map(int, file.readline().split(",")))
    for day in range(days):
        for i in range(len(fish_list)):
            fish_list[i] += -1
            if fish_list[i] == -1:
                fish_list[i] = 6
                fish_list.append(8)
    print(len(fish_list))