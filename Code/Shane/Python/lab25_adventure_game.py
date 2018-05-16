import random

''' need to dos:
start by placing enemies at random x,y coordinates
after that give the hero a random x,y coordinate so it overrides an enemy at that position
how to do coordinates?
    list of tuples for the positions, but how do I know whats the hero and whats an enemy?
    dictionary? - same keys...? enemy, enemy, enemy... How are instances of a class stored
'''

class Position:
    def __init__(self, loc_c, loc_r, character_image):
        self.loc_c = loc_c
        self.loc_r = loc_r
        self.character_image = character_image
        def random_row_col(self):
            return random.randint(0, self.height - 1), random.randint(0, self.width - 1)


class Hero(Position):
    def __init__(self, loc_c, loc_r):
        super().__init__(loc_c, loc_r, '🐲')


class Enemy(Position):
    def __init__(self, loc_c, loc_r):
        super().__init__(loc_c, loc_r, '')
        character = random.choice([('alien','👾'), ('demon','👹'),
                                   ('boar','🐗'), ('bat','🦇'), ('kraken','🦑')])
        self.character_image = character[1]     # Matthew
        self.name = character[0]                # Matthew

    def __repr__(self):     # Matthew
        return self.name    # Matthew


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        list_of_things = list()
        if random.randint(1,15) == 1:
            for row in range(height):
                for col in range(height):
                    enemy = Enemy(row, col)
                    list_of_things.append(enemy)
        else:
            list_of_things.append("⬛")

        hero = Hero(random.randint(1,height), random.randint(1,width))
        list_of_things.append(hero)
        self.list_of_things = list_of_things


    def __str__(self):



    # def __str__(self):
    #     board = list()
    #     enemy_list = []
    #     for row in range(self.height):
    #         board.append([])
    #         for col in range(self.width):
    #             if random.randint(1,15) == 1:
    #                 enemy = Enemy(row, col)
    #                 enemy_list.append(enemy)
    #                 board[row].append(enemy.character_image)
    #             else:
    #                 board[row].append("⬛")
    #     for l in range(len(board)):
    #         print("".join(board[l]))
    #     return '\n'


#
# class Move:
#     def __init__(self, move):
#         self.move = move
#
#     def movement(self, direction):
#         self.direction = direction
#
#
# class Attack:
#     def __init__(self):
#         self.attack_power = 1
#
# def position(loc_c, loc_r):
#     return



b = Board(10, 10)
print(b)

#hero = Hero.random_row_col


enemies = []
entities = []
def remove_from_lists(obj, list1, list2):
    for i in range(len(list1)):
        if obj is list1[i]:
            list1.pop(i)
            break
    for i in range(len(list2)):
        if obj is list2[i]:
            list2.pop(i)
            break

remove_from_lists(enemy, enemies, entities)



# for i in range(enemy_count):
#     row, col = boardsetup.random_row_col()
#     enemy = Enemy(row,col)



# import random
#
# class Grid:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.grid = []
#         for j in range(self.height):
#             self.grid.append([])
#             for i in range(self.width):
#                 self.grid[j].append(random.choice([True, False]))
#
#     def __str__(self):
#         r = ''
#         for j in range(self.height):
#             for i in range(self.width):
#                 if self.grid[j][i]:
#                     r += '⚪'
#                 else:
#                     r += '⬛'
#             r += '\n'
#         return r
#
#     def __len__(self):
#         return self.width * self.height
#
#     def check_alive(self, i, j):
#         if i < 0 or i >= self.width:
#             return False
#         elif j < 0 or j >= self.height:
#             return False
#         return self.grid[j][i]
#
#     def count_alive_around_cell(self, i, j):
#         n_alive = 0
#         for m in range(-1, 2):
#             for n in range(-1, 2):
#                 if m == 0 and n == 0:
#                     continue
#                 if self.check_alive(i + n, j + m):
#                     n_alive += 1
#         return n_alive
#
#     def next_state(self):
#         new_grid = Grid(self.width, self.height)
#         for j in range(self.height):
#             for i in range(self.width):
#                 old_value = self.grid[j][i]
#                 n_alive = self.count_alive_around_cell(i, j)
#                 new_value = False
#                 # apply the rules to find the new value
#                 if old_value:
#                     if n_alive < 2:
#                         new_value = False
#                     elif n_alive in [2, 3]:
#                         new_value = True
#                     elif n_alive > 3:
#                         new_value = False
#                 elif n_alive == 3:
#                     new_value = True
#                 else:
#                     new_value = False
#                 new_grid.grid[j][i] = new_value
#         return new_grid
#
# class Hero:
#     def __init__(self, j, i):
#         self.j = j
#         self.i = i
#         self.alive = True
#
#
# import time
#
# grid = Grid(50, 30)
# print(len(grid))
# print(str(grid))
# for i in range(100):
#     print(grid)
#     time.sleep(.2)
#     grid = grid.next_state()




