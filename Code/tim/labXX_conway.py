import random
import chalk
import time

height = 20
width = 100

r_sq = chalk.red('■')

def print_grid(grid):
    p_grid = ''
    for i in range(height):
        for j in range(width):
            if grid[i][j] == '':
                p_grid += r_sq
                grid[i][j] = True
            elif grid[i][j]:
                p_grid += '■'
            else:
                p_grid += '□'
        p_grid += '\n'
    print(p_grid)


def draw_rand_sq(grid):
    i = random.randrange(len(grid) - 4)
    j = random.randrange(len(grid[1]) - 4)
    #Top
    grid[i][j] = ''
    grid[i][j + 1] = ''
    grid[i][j + 2] = ''
    grid[i][j + 3] = ''
    grid[i][j + 4] = ''
    #Sides
    grid[i + 1][j] = ''
    grid[i + 1][j + 4] = ''
    grid[i + 2][j] = ''
    grid[i + 2][j + 4] = ''
    grid[i + 3][j] = ''
    grid[i + 3][j + 4] = ''
    #Bottom
    grid[i + 4][j] = ''
    grid[i + 4][j + 1] = ''
    grid[i + 4][j + 2] = ''
    grid[i + 4][j + 3] = ''
    grid[i + 4][j + 4] = ''
    #Insides
    grid[i + 1][j + 1] = ''
    grid[i + 1][j + 3] = ''
    grid[i + 2][j + 1] = ''
    grid[i + 2][j + 3] = ''
    grid[i + 3][j + 1] = ''
    grid[i + 3][j + 3] = ''
    grid[i + 1][j + 2] = ''
    grid[i + 3][j + 2] = ''
    grid[i + 3][j + 3] = False

def draw_rand_streak(grid):
    vh = random.randrange(2)
    if vh == 0:
        v = random.randrange(len(grid))
        for j in range(len(grid[1])):
            grid[v][j] = ''
    else:
        h = random.randrange(len(grid[1]))
        for i in range(len(grid)):
            grid[i][h] = ''


def alive(grid, i, j):
    n_alive = 0
    # above left
    if i > 0 and j > 0:
        if grid[i - 1][j - 1]:
            n_alive += 1
    # above right
    if i < len(grid) - 1 and j > 0:
        if grid[i + 1][j - 1]:
            n_alive += 1
    # below left
    if i > 0 and j < len(grid[1]) - 1:
        if grid[i - 1][j + 1]:
            n_alive += 1
    # below right
    if i < len(grid) - 1 and j < len(grid[1]) - 1:
        if grid[i + 1][j + 1]:
            n_alive += 1
    # above
    if j > 0:
        if grid[i][j - 1]:
            n_alive += 1
    # left
    if i > 0:
        if grid[i - 1][j]:
            n_alive += 1
    # below
    if j < len(grid[1]) - 1:
        if grid[i][j + 1]:
            n_alive += 1
    # right
    if i < len(grid) - 1:
        if grid[i + 1][j]:
            n_alive += 1
    # check results
    if n_alive == 3:
        return True
    elif n_alive == 2 and grid[i][j]:
        return True
    else:
        return False


def deep_copy(grid):
    new_grid = []
    for i in range(height):
        new_grid.append([])
        for j in range(width):
            new_grid[i].append(grid[i][j])
    return new_grid


grid = []
for i in range(height):
    grid.append([])
    for j in range(width):
        grid[i].append(False)
draw_rand_sq(grid)
draw_rand_sq(grid)
draw_rand_streak(grid)
draw_rand_streak(grid)
print_grid(grid)
time.sleep(2)

n_alive = 1
r_ct = 1

while n_alive != 0:
    n_alive = 0
    t_grid = []
    for i in range(height):
        t_grid.append([])
        for j in range(width):
            t_grid[i].append(alive(grid, i, j))
            n_alive += t_grid[i][j]
    grid = deep_copy(t_grid)
    r_ct += 1
    if r_ct == 25:
        draw_rand_sq(grid)
        print_grid(grid)
        time.sleep(1)
    elif r_ct == 50:
        r_ct = 0
        draw_rand_streak(grid)
        print_grid(grid)
        time.sleep(1)
    else:
        print_grid(grid)
        time.sleep(.3)
    print('')
