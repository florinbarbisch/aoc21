height_map = [[int(x) for x in list(line.rstrip())] for line in open("input.txt", "r")]
len_y, len_x = len(height_map), len(height_map[0])

def find_basin(x, y, basin_size):
        basin_size += 1
        height_map[x][y] = 9 # mark as visited
        if x-1 >= 0     and height_map[x-1][y  ] != 9: basin_size = find_basin(x-1, y  , basin_size) # check top
        if y+1 <  len_x and height_map[x  ][y+1] != 9: basin_size = find_basin(x  , y+1, basin_size) # check right
        if x+1 <  len_y and height_map[x+1][y  ] != 9: basin_size = find_basin(x+1, y  , basin_size) # check bottom
        if y-1 >= 0     and height_map[x  ][y-1] != 9: basin_size = find_basin(x  , y-1, basin_size) # check left
        return basin_size

basins = []
for y in range(len_x):
    for x in range(len_y):
        if height_map[x][y] != 9:
            basins.append(find_basin(x, y, 0))
basins.sort(reverse=True)
print(basins[0]*basins[1]*basins[2])