import random
import time
# rules:
# false = Any live cell with fewer than two live neighbors dies, as if caused by under population.
# true = Any live cell with two or three live neighbors lives on to the next generation.
# false = Any live cell with more than three live neighbors dies, as if by overpopulation.
# true = Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


live_grid = []

height = 50

width = 100

def make_lst(lst, height, width ):
    for i in range(height):
        lst.append([])
        for j in range(width):
            lst[i].append(random.choice([True, False]))
    for f in range(len(lst)):
        lst[0][f] = False
        lst[-f][0] = False
        lst[f][-1] = False
        lst[-1][f] = False

def print_out(lst, height, width):
    for x in range(height):
        for y in range(width):
            if lst[x][y]:
                print("■", end = "")
            else:
                print("□", end = "")
        print()
    print()
    print()

def set_state(live_count):
    if live_count == 2:
        return random.choice([True, False])
    elif live_count == 3:
        return True
    elif live_count < 2 or live_count > 3:
        return False

def live_count(grid, x, y):
    live_count = 0
    if grid[x - 1][y - 1] == True:
        live_count += 1
    if grid[x - 1][y] == True:
        live_count += 1
    if grid[x - 1][y + 1] == True:
        live_count += 1
    if grid[x][y - 1] == True:
        live_count += 1
    if grid[x][y + 1] == True:
        live_count += 1
    if grid[x + 1][y - 1] == True:
        live_count += 1
    if grid[x + 1][y] == True:
        live_count += 1
    if grid[x + 1][y + 1] == True:
        live_count += 1
    return live_count

def counts(change_grid, height, width):
    for x in range(1, height -1):
        for y in range(1, width -1):
            change_grid[x][y] = (live_count(live_grid,x,y))
    return change_grid

def change_state(live_grid, height, width):
    for x in range(height):
        for y in range(width):
            live_grid[x][y] = set_state(live_grid[x][y])
    return live_grid

make_lst(live_grid, height, width)

while True:
    change_grid = live_grid.copy()

    counts(change_grid,height, width)

    live_grid = change_state(change_grid, height, width)

    print_out(live_grid, height, width)

    time.sleep(.00000000000000000001)


