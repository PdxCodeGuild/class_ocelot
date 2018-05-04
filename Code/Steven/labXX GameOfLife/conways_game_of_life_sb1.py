
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
    if check_alive(grid, i, j-1):
        count += 1
    if check_alive(grid, i+1, j-1):
        count += 1

    if check_alive(grid, i-1, j):
        count += 1

  # You are here

    if check_alive(grid, i+1, j):
        count += 1

    if check_alive(grid, i-1, j+1):
        count += 1
    if check_alive(grid, i, j+1):
        count += 1
    if check_alive(grid, i+1, j+1):
        count += 1




    # ...

    return count


def next_state(old_grid):
    new_grid = []
    for j in range(height):
        new_grid.append([])
        for i in range(width):
            old_value = old_grid[j][i]

            if old_value == True:
                if count_alive(grid, i, j) < 2:
                    new_value = False


           # new_value = not old_value

            n_alive = count_alive(grid, i, j)
            #new_value = False
            # using the rules, figure out what new_value is


            new_grid[j].append(new_value)


    return new_grid




grid = []
for j in range(height):
    grid.append([])
    for i in range(width):
        grid[j].append(random.choice([True, False]))
        # grid[j].append([True])



import time

# The Grid writer
for i in range(10):



    print_grid(grid)

    grid = next_state(grid)
    #time.sleep(1)
    input()

    # for j in range(50):
    #     random_j = random.randint(0, height-1)
    #     random_i = random.randint(0, width-1)
    #     grid[random_j][random_i] = True #random.choice([True, False])

    print()



#rules:
#rule 1 - Any live cell with fewer than two live neighbors dies, as if caused by under population.
#rule 2 - Any live cell with two or three live neighbors lives on to the next generation.
#rule 3 - Any live cell with more than three live neighbors dies, as if by overpopulation.
#rule 4 - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

