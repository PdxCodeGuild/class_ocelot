import random
import time


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character

class Bee(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🐝')
        self.target_flower = None
        self.last_flower = None

class Pollution(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '')
        f = random.choice([(1, '🐻'), (2, '🛢'), (3, '🏭')])
        # self.character = random.choice(['🌼', '🌸', '🌺'])
        self.character = f[1]
        self.health = f[0]

class Flower(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '')
        f = random.choice([(1, '🌼'), (2, '🌸'), (3, '🌸')])
        # self.character = random.choice(['🌼', '🌸', '🌺'])
        self.character = f[1]
        self.health = f[0]

# class BoardHigh:
#     def __init__(self, width, height):
#         # define high-level board
#         self.width = board_width
#         self.height = board_height
#
#         # populates high-level board with entities and blanks
#
#     def random_location(self):
#         # return a random location on the high-level board
#         return random.randint(0, self.height - 1), random.randint(0, self.width - 1)
#
#     def __getitem__(self, j):
#         return self.boardhigh[j]
#
#     # populates board with entities and blanks
#     def print(self, entities):
#         for i in range(self.height):
#             # counts through all rows
#             for j in range(self.width):
#                 # counts through all columns
#                 for k in range(len(entities)):
#                     # finds entities from list that match current coordinates.
#                     if entities[k].location_i == i and entities[k].location_j == j:
#                         print(entities[k].character, end='')
#                         break
#                 else:
#                     # If no entities match, print blank (random leaves).
#                     # print(random.choice(['⬛️']), end='')
#                     print(random.choice(['🌲', '🌳', '🌲']), end='')
#             print()
#

class BoardLow:
    def __init__(self, width, height):
        # define low-level map
        self.width = board_width
        self.height = board_height

        # build entities - enemies and flowers

        # populates board with entities and blanks

        # return a random location on the board
    def random_location(self):
        return random.randint(0, self.height - 1), random.randint(0, self.width - 1)

    def __getitem__(self, j):
        return self.boardlow[j]

    # populates board low with entities and blanks
    def print(self, entities):
        for i in range(self.height):
            # counts through all rows
            for j in range(self.width):
                # counts through all columns
                for k in range(len(entities)):
                    # finds entities from list that match current coordinates.
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    # If no entities match, print blank (random leaves).
                    # print(random.choice(['⬛️']), end='')
                    # print(random.choice(['🌿️', '🌱', '🍀']), end='')
                    print(random.choice(['⬜️']), end='')

            print()


def collision(bee, entities):
    # test if bee is on same square as ANY entity (flower, scent or factory)
    for entity in entities:
        if entity != bee:
            if bee.location_i == entity.location_i and \
                    bee.location_j == entity.location_j:
                return entity
    return None

def check_boundries():
    for entity in entities:
        if random.randint(0, 1) == 0:
            if entity.location_i > b.height - 1:
                entity.location_i -= b.height
            elif entity.location_i < 0:
                entity.location_i += b.height
        else:
            if entity.location_j > b.width - 1:
                entity.location_j -= b.width
            elif entity.location_j < 0:
                entity.location_j += b.width

def move_bee_randomly(bee):
    # manual control
    # command = input('command? ')  # get the command from the user
    # if command == 'done':
    #     break  # exit the game
    #
    # elif command in ['u', 'up', 'n', 'north']:
    #     bee.location_i -= (1 * move_mult)  # move up
    # elif command in ['d', 'down', 's', 'south']:
    #     bee.location_i += (1 * move_mult)  # move down
    # elif command in ['l', 'left', 'w', 'west']:
    #     bee.location_j -= (1 * move_mult)  # move left
    # elif command in ['r', 'right', 'e', 'east']:
    #     bee.location_j += (1 * move_mult)  # move right

    # random bee path
    path_rand = random.choice(['u', 'd', 'l', 'r'])
    if path_rand == 'u':
        bee.location_i += 1  # move up
    if path_rand == 'd':
        bee.location_i -= 1  # move down
    if path_rand == 'l':
        bee.location_j -= 1  # move left
    if path_rand == 'r':
        bee.location_j += 1  # move right
    return bee



# set parameters
board_width = 30
board_height = 15

bd_l = BoardLow(board_width, board_height)
# bd_h = BoardHigh(board_width, board_height)

move_mult = 1
pollution_count = 15
flower_count = 12
health = 3
flower_awareness_range = 4


bi, bj = bd_l.random_location()
bee = Bee(bi, bj)           # set player start position, random

entities = [bee]            # make entity lists (bee, pollutions and flowers)
pollutions = []
flowers = []

# add pollutions to entity list and to pollution list
for i in range(pollution_count):
    pi, pj = bd_l.random_location()
    pollution = Pollution(pi, pj)
    entities.append(pollution)
    pollutions.append(pollution)

# add flower to entity list and to flowers list
for i in range(flower_count):
    fi, fj = bd_l.random_location()
    flower = Flower(fi, fj)
    entities.append(flower)
    flowers.append(flower)


while True:                                 # THE GAME LOOP
    bd_l.print(entities)                    # print all entities to the board
    time.sleep(1)                           # delay

    vect_flowers = []                       # define flower vectors
    for flower in flowers:                  # iterate through all placed flowers
        if flower is bee.last_flower \
                or flower is bee.last_flower2:  # prevent revisit
            continue
        vect_flower = [ flower.location_i - bee.location_i , flower.location_j - bee.location_j , flower ]
        vect_flowers.append ( vect_flower )
        # print(f'vect_flowers {flower} = {type(vect_flowers)}')

    # calc axis of bee movement toward flower
    vect_closest = min(vect_flowers, key=lambda v: abs(v[0]) + abs(v[1]))

    # BEE MOVER 🐝
    if abs(vect_closest[0]) + abs(vect_closest[1]) < flower_awareness_range:

        # specify bee flight direction based on vector of target flower
        if abs(vect_closest[0]) > abs(vect_closest[1]):
            # vertical
            if vect_closest[0] < 0:
                # up
                bee.location_i -= 1
            else:
                # down
                bee.location_i += 1
        else:
            # horizontal
            if vect_closest[1] < 0:
                # left
                bee.location_j -= 1
            else:
                # right
                bee.location_j += 1
    else:
        move_bee_randomly(bee)

    print(f'Target Flower: {vect_closest[2]}\t \t Health: {health}')

    # move pollutions 1 square in a random direction
    for pollution in pollutions:
        if random.randint(0, 1) == 0:
            pollution.location_i += random.randint(-1, 1)
        else:
            pollution.location_j += random.randint(-1, 1)

    # detect bee touching an entity (either pollution, flower or flower scent)
    entity_touch = collision(bee, entities)

    if entity_touch is not None:
        if type(entity_touch) is Pollution:
            health -= 1
            print(f'Ouch! (health = {health})')
            # TEST print(type(entity_touch))

        if type(entity_touch) is Flower:
            health += entity_touch.health
            print(f'Yum! (health = {health})')
            # TEST print(type(entity_touch))
            bee.last_flower2 = bee.last_flower
            bee.last_flower = entity_touch

    if health <= 1:
        print('You\'re dead!')
        exit()
