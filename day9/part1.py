height_map = ["".join(["9", line.rstrip(), "9"]) for line in open("input.txt", "r")]
height_map.insert(0, len(height_map[0])*"9")
height_map.append(   len(height_map[0])*"9")
len_x, len_y = len(height_map), len(height_map[0])
risk_level_sum = 0
for x in range(1, len_x-1):
    for y in range(1, len_y-1):
        height = height_map[x][y]
        if  height_map[x-1][y  ] > height and \
            height_map[x  ][y+1] > height and \
            height_map[x+1][y  ] > height and \
            height_map[x  ][y-1] > height:
            risk_level_sum += (int(height) + 1)
print(risk_level_sum)