import random

class Hero:
    def __init__(self, loc_c, loc_r):
        self.character_image = '👾'
        self.loc_c = loc_c
        self.loc_r = loc_r

class Enemy:
    def __init__(self, loc_c, loc_r):
        self.character_image = random.choice(['👹','👿', '🐲','🐗','🦇','🦑'])
        self.loc_c = loc_c
        self.loc_r = loc_r


class SetUpBoard:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        board = list()
        enemy_list = []
        for row in range(self.height+1):
            board.append([])
            for col in range(self.width):
                if random.randint(1,15) == 1:
                    enemy = Enemy(row, col)
                    enemy_list.append(enemy)
                    board[row].append(enemy.character_image)
                else:
                    board[row].append("⬛")
        for l in range(len(board)):
            print("".join(board[l]))
        return '\n'

    def random_row_col(self, row, col):
        return randomint(0,self.height-1), randomint(0,self.width-1)

class Move:
    def __init__(self, move):
        self.move = move

    def movement(self, direction):
        self.direction = direction


class Attack:
    def __init__(self):
        self.attack_power = 1

boardsetup = SetUpBoard(10, 10)
print(boardsetup)

# for i in range(enemy_count):
#     row, col = boardsetup.random_row_col()
#     enemy = Enemy(row,col)


