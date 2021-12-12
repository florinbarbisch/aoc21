energy_level_map = [[int(n) for n in line.rstrip()] for line in open("input.txt", "r")]
flashed = [[False for j in range(10)] for j in range(10)]

def flash(x, y):
    flashed[x][y] = True
    # increase adjacent fields
    for x_adj in range(x-1, x+2):
        for y_adj in range(y-1, y+2):
            if x_adj >= 0 and x_adj < 10 and y_adj >= 0 and y_adj < 10:
                energy_level_map[x_adj][y_adj] += 1
                # flash them if possible
                if energy_level_map[x_adj][y_adj] > 9 and not flashed[x_adj][y_adj]:
                    flash(x_adj, y_adj)

flash_count = 0
for step in range(100):
    for x in range(10):
        for y in range(10):
            energy_level_map[x][y] += 1
    for x in range(10):
        for y in range(10):
            if energy_level_map[x][y] > 9 and not flashed[x][y]:
                flash(x, y)
    for x in range(10):
        for y in range(10):
            if flashed[x][y]:
                flash_count += 1
                energy_level_map[x][y] = 0
                flashed[x][y] = False
print(flash_count)