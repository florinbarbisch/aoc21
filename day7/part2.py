with open("input.txt", "r") as file:
    crabs = list(map(int, file.readline().split(",")))
    min_fuel = -1
    distance = 0
    for i in range(min(crabs), max(crabs)+1):
        fuel = sum(map(lambda x: (x+1)*x//2, map(lambda x: abs(x-i),crabs)))
        if fuel < min_fuel or min_fuel == -1:
            min_fuel = fuel
            distance = i
    print(min_fuel)
    print(distance)