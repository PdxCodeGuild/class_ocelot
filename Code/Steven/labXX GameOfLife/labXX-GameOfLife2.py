import random
import time

# Grid dims
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


def check_alive(grid, i, j):
    # return true if i. j is valid and alive
    if i < 0 or i >= width:
        return False
    elif j < 0 or j >= height:
        return False
    return grid[i][j]


def count_alive(grid, i, j):
    count = 0

   # Upper Row
    if check_alive(grid, i-1, j-1):
        count += 1
    if check_alive(grid, i, j-1):
        count += 1
    if check_alive(grid, i+1, j-1):
        count += 1

    # Middle Row
    if check_alive(grid, i-1, j):
        count += 1

    # You are here

    if check_alive(grid, i+1, j):
        count += 1

    # Bottom Row
    if check_alive(grid, i-1, j+1):
        count += 1
    if check_alive(grid, i, j+1):
        count += 1
    if check_alive(grid, i+1, j+1):
        count += 1

    return count


def next_state(old_grid):
    new_grid = []
    for j in range(height):
        new_grid.append([])
        for i in range(width):
            old_value = old_grid[j][i]
            n_alive = count_alive(grid, i, j)

            if old_value == True:
                new_value = False

                if count_alive(grid,i,j) < 2:
                    new_value = False

            # new_value = False

            # using the rules, figure out what new_value is


                new_grid[j].append(new_value)


    return new_grid




grid = []
for j in range(height):
    grid.append([])
    for i in range(width):
        grid[j].append(random.choice([True, False]))
        grid[j].append([True])


# The Grid writer
for i in range(1):
    print_grid(grid)

    grid = next_state(grid)
    #time.sleep(1)
    input()




# Randomizer 1
#     for j in range(10):
#         # print(height, width, '\t', random.randint(0, height-1), random.randint(0, width-1))  # TEMP TEST:
#         grid[j][i] = True # TEMP TEST
#         # random_j = random.randint(0, height-1)
#         # random_i = random.randint(0, width-1)
#         # grid[random_j][random_i] = True #random.choice([True, False])

    print()

    break

