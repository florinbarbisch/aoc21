height_map = [[int(x) for x in list(line.rstrip())]for line in open("input.txt", "r")]
len_y, len_x = len(height_map), len(height_map[0])
risk_level_sum = 0
for y in range(len_x):
    for x in range(len_y):
        height = height_map[x][y]
        if x-1 >= 0    and height_map[x-1][y] <= height: continue # check top
        if y+1 < len_x and height_map[x][y+1] <= height: continue # check right
        if x+1 < len_y and height_map[x+1][y] <= height: continue # check bottom
        if y-1 >= 0    and height_map[x][y-1] <= height: continue # check left
        risk_level_sum += (height + 1)
print(risk_level_sum)