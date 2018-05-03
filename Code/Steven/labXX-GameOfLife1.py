
import random


width = 10
height = 10

def print_grid(grid):
    for j in range(height):
        for i in range(width):
            if grid[j][i]:
                print('■', end='')
            else:
                print('□', end='')
        print()

def deep_copy(grid):
    new_grid = []
    for j in range(height):
        new_grid.append([])
        for i in range(width):
            new_grid[j].append(grid[j][i])
    return new_grid

# def grid_test1(x,y):
#

grid = []
for j in range(height):
    grid.append([])
    for i in range(width):
        grid[j].append(random.choice([True, False]))
        # grid[j].append([True])



# The Grid writer
for i in range(10):
    print_grid(grid)

    # for j in range(50):
    #     random_j = random.randint(0, height-1)
    #     random_i = random.randint(0, width-1)
    #     grid[random_j][random_i] = True #random.choice([True, False])

    print()





def check_alive(grid, i, j):
    # return true if i. j is valid and alive
    if i < 0 or i >= width:
        return False
    elif j < 0 or j >= height:
        return False
    return grid[i][j]


def count_alive(grid, i, j):
    count = 0
    if check_alive(grid, i-1, j-1):
        count += 1
    if check_alive(grid, i-1, j):
        count += 1
    # ...
    return count


def next_state(old_grid):
    new_grid = []
    for j in range(height):
        new_grid.append([])
        for i in range(width):
            # what is the new value for i, j?
            n_alive = count_alive(grid, i, j)
            # write the rules
            # set the new value for i, j



