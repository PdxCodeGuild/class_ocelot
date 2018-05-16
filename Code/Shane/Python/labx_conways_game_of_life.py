
import random


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = []
        for j in range(self.height):
            self.grid.append([])
            for i in range(self.width):
                self.grid[j].append(random.choice([True, False]))

    def __str__(self):
        r = ''
        for j in range(self.height):
            for i in range(self.width):
                if self.grid[j][i]:
                    r += '⚪'
                else:
                    r += '⬛'
            r += '\n'
        return r

    def __len__(self):
        return self.width * self.height

    def check_alive(self, i, j):
        if i < 0 or i >= self.width:
            return False
        elif j < 0 or j >= self.height:
            return False
        return self.grid[j][i]

    def count_alive_around_cell(self, i, j):
        n_alive = 0
        for m in range(-1, 2):
            for n in range(-1, 2):
                if m == 0 and n == 0:
                    continue
                if self.check_alive(i + n, j + m):
                    n_alive += 1
        return n_alive

    def next_state(self):
        new_grid = Grid(self.width, self.height)
        for j in range(self.height):
            for i in range(self.width):

                old_value = self.grid[j][i]
                n_alive = self.count_alive_around_cell(i, j)

                new_value = False
                # apply the rules to find the new value

                if old_value:
                    if n_alive < 2:
                        new_value = False
                    elif n_alive in [2, 3]:
                        new_value = True
                    elif n_alive > 3:
                        new_value = False
                elif n_alive == 3:
                    new_value = True
                else:
                    new_value = False

                new_grid.grid[j][i] = new_value

        return new_grid


import time

grid = Grid(50, 30)
print(len(grid))
print(str(grid))
for i in range(100):
    print(grid)
    time.sleep(.2)
    grid = grid.next_state()




