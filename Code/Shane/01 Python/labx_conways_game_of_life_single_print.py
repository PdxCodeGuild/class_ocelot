
import random

width = 11
height = 11


def print_grid(grids):
    for x in range(height):
        for y in range(width):
            if grids[x][y] == True:
                print('■', end='')
            else:
                print('□', end='')
        print()


def check_alive(cells, i, j):
    if i < 0 or i >= width:
        return False
    elif j < 0 or j >= height:
        return False
    return cells[j][i]


def count_alive_around_cell(cells, i, j):
    count_of_live = 0
    for m in range(-1,2):
        for n in range(-1,2):
            if m == 0 and n == 0:
                continue
            if check_alive(cells, j+m, i+n):
                count_of_live += 1

    return count_of_live



def next_state(old_cells):
    new_cells = []
    for j in range(height):
        new_cells.append([])
        for i in range(width):

            old_value = old_cells[j][i]
            n_alive = count_alive_around_cell(old_cells, i, j)

            new_value = not old_value

            # apply the rules to find the new value
            if n_alive == 2:
                return random.choice([True, False])
            elif n_alive == 3:
                return True
            elif n_alive < 2 or live_count > 3:
                return False

            new_cells[j].append(new_value)

    return new_cells



def rule1(count):
    if count > 3:
        return False


grid = []

for j in range(height):
    grid.append([])
    for i in range(width):
        grid[j].append(random.choice([True, False]))

# for f in range(len(grid)):
#     grid[0][f] = False
#     grid[-f][0] = False
#     grid[f][-1] = False
#     grid[-1][f] = False


# rules:
# Any live cell with fewer than two live neighbors dies, as if caused by under population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


# for j in range(1, height-1):
#     for i in range(1, width-1):
#         cell = grid[j][i]
#         if grid[j][i]:
#             count_alive_around_cell(cell)
#         else:
#             print("off")
#



for i in range(100):
    print_grid(grid)

    grid = next_state(grid)
    input()


