height_map = [[int(x) for x in line.rstrip()] for line in open("input.txt", "r")]
len_x, len_y = len(height_map), len(height_map[0])

def find_basin(x, y, basin_size):
    if x < 0 or x >= len_x or y < 0 or y >= len_y or height_map[x][y] == 9:
        return basin_size
    basin_size += 1
    height_map[x][y] = 9 # mark as visited
    basin_size = find_basin(x-1, y  , basin_size) # check top
    basin_size = find_basin(x  , y+1, basin_size) # check right
    basin_size = find_basin(x+1, y  , basin_size) # check bottom
    basin_size = find_basin(x  , y-1, basin_size) # check left
    return basin_size

basins = [find_basin(x, y, 0) for y in range(len_y) for x in range(len_x)]
basins.sort()
print(basins[-1]*basins[-2]*basins[-3])