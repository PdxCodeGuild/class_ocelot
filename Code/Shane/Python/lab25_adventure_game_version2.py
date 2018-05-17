import random
from labx_conways_game_of_life import b, run


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, random.choice(['👾', '👹',
                                                                '🐗', '🦇',
                                                                '🦑', '😈']))


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🐐')





def collision(hero_loc, list1, list2):
    for e in range(len(list2)):
        enemy_loc = (list2[e].location_i, list2[e].location_j)
        if hero_loc == enemy_loc:

            list2.pop(e)
            list1.pop(e+1)
            print("nom nom")
            run()
            break


def board_looper(obj):
    if random.randint(0, 1) == 0:
        obj.location_i += random.randint(-1, 1)
        if obj.location_i > b.height-1:
            obj.location_i -= b.height
        elif obj.location_i < 0:
            obj.location_i += b.height
    else:
        obj.location_j += random.randint(-1, 1)
        if obj.location_j > b.width-1:
            obj.location_j -= b.width
        elif obj.location_j < 0:
            obj.location_j += b.width





pi, pj = b.random_location()
player = Player(pi, pj)


entities = [player]
enemies = []

for i in range(b.height):
    ei, ej = b.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)


while True:

    b.print(entities)

    command = input('Move\n')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down

    for enemy in enemies:
        board_looper(enemy)

    collision((player.location_i, player.location_j), entities, enemies)
