import random
import chalk

height = 30
width = 100


def print_grid(grid):
    p_grid = ''
    for i in range(height):
        for j in range(width):
            if grid[i][j]:
                p_grid += chalk.red('■')
            else:
                p_grid += '□'
        p_grid += '\n'
    print(p_grid)


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
        grid[i].append(random.choice([True, False]))
# grid[height // 2 + 0][width // 2 + 0] = True
# grid[height // 2 + 0][width // 2 + 1] = True
# grid[height // 2 + 1][width // 2 + 0] = True
# grid[height // 2 + 1][width // 2 + 1] = True


n_alive = 1
while n_alive != 0:
    print_grid(grid)
    print('')
    n_alive = 0
    t_grid = []
    for i in range(height):
        t_grid.append([])
        for j in range(width):
            t_grid[i].append(alive(grid, i, j))
            n_alive += t_grid[i][j]
    grid = deep_copy(t_grid)

print_grid(grid)
