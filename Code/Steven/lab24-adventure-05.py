import random
import time

class Entity:
    def __init__ ( self , location_i , location_j , character ):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

    def __str__ ( self ):
        return self.character

    def __repr__ ( self ):
        return self.character

class Bee ( Entity ):
    def __init__ ( self , location_i , location_j ):
        super ( ).__init__ ( location_i , location_j , '🐝' )
        self.target_flower = None
        self.last_flower = None

class Pollution ( Entity ):
    def __init__ ( self , location_i , location_j ):
        super ( ).__init__ ( location_i , location_j , '' )
        f = random.choice ( [ (1 , '🐻') , (2 , '🐻') , (3 , '🐻') ] )
        # other enemy emoji: 🏭 🛢 🐻
        self.character = f[ 1 ]
        self.health = f[ 0 ]

class Flower ( Entity ):
    def __init__ ( self , location_i , location_j ):
        super ( ).__init__ ( location_i , location_j , '' )
        f = random.choice ( [ (1 , '🌼') , (2 , '🌸') , (3 , '🌸') ] )
        self.character = f[ 1 ]
        self.health = f[ 0 ]


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
    def __init__ ( self , width , height ):                 # define low-level map
        self.width = board_width
        self.height = board_height

        # build entities - enemies and flowers
        # populates board with entities and blanks
        # return a random location on the board

    def random_location ( self ):
        return random.randint ( 0 , self.height - 1 ) , random.randint ( 0 , self.width - 1 )

    def __getitem__ ( self , j ):
        return self.boardlow[ j ]

    def print ( self , entities ):                                      # populate board
        for i in range ( self.height ):
            for j in range ( self.width ):                              # counts through all rows
                for k in range ( len ( entities ) ):                    # counts through all columns
                    if entities[ k ].location_i == i and entities[ k ].location_j == j: # match entities
                        print ( entities[ k ].character , end='' )
                        break
                else:
                    print ( random.choice ( bkgd_white ) , end='' )

            print ( )


def collision ( bee , entities ):               # test if bee is on same square as ANY entity

    for entity in entities:
        if entity != bee:
            if bee.location_i == entity.location_i and \
                    bee.location_j == entity.location_j:
                return entity
    return None


def check_boundries ( ):
    for entity in entities:
        if random.randint ( 0 , 1 ) == 0:
            if entity.location_i > b.height - 1:
                entity.location_i -= b.height
            elif entity.location_i < 0:
                entity.location_i += b.height
        else:
            if entity.location_j > b.width - 1:
                entity.location_j -= b.width
            elif entity.location_j < 0:
                entity.location_j += b.width


def move_bee_randomly ( bee ):                                      # change bee x/y location +/-1
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
    path_rand = random.choice ( [ 'u' , 'd' , 'l' , 'r' ] )
    if path_rand == 'u':
        bee.location_i += 1  # move up
    if path_rand == 'd':
        bee.location_i -= 1  # move down
    if path_rand == 'l':
        bee.location_j -= 1  # move left
    if path_rand == 'r':
        bee.location_j += 1  # move right
    return bee


# SET PARAMETERS
frame_delay = .8
board_width, board_height = 20, 15                                  # global parameters
bkgd_leaves1 = [ '🌿️' , '🌱' , '🍀' ]
bkgd_trees1 = ['🌲', '🌳', '🌲']
bkgd_white = [ '⬜️' ]

bd_l = BoardLow ( board_width , board_height )                      # board (low) parameters
bkgd_low = bkgd_white

# bd_h = BoardHigh(board_width, board_height)                         # board (high) parameters
# bkgd_high = bkgd_trees1

health = 3                                                          # bee parameters
flower_awareness_range = 4
move_mult = 1

flower_count = 12                                                   # flower parameters

pollution_count = 15                                                # pollution parameters

# CREATE AND PLACE ENTITIES
bi , bj = bd_l.random_location ( )                                  # pick random start position for bee
bee = Bee ( bi , bj )

entities = [ bee ]                                                  # define entity lists
pollutions = [ ]
flowers = [ ]

for i in range ( pollution_count ):                                 # create n pollution entities
    pi , pj = bd_l.random_location ( )
    pollution = Pollution ( pi , pj )
    entities.append ( pollution )                                   # put pollutions in ENTITIES list
    pollutions.append ( pollution )                                 # put pollutions in POLLUTIONS list

# add flower to entity list and to flowers list
for i in range ( flower_count ):                                    # create n flower entities
    fi , fj = bd_l.random_location ( )
    flower = Flower ( fi , fj )
    entities.append ( flower )                                      # put flowers in ENTITIES list
    flowers.append ( flower )                                       # put flowers in FLOWERS list

bee.last_flower2 = None                                              # revisit prevention

# THE GAME LOOP
while True:
    bd_l.print ( entities )                                         # print all entities to the board
    time.sleep ( frame_delay )                                      # display delay

    vect_flowers = [ ]                                              # define flower vectors
    for flower in flowers:                                          # iterate through all placed flowers
        if flower is bee.last_flower \
                or flower is bee.last_flower2:                      # prevent flower revisit
            continue
        vect_flower = [ flower.location_i - bee.location_i , flower.location_j - bee.location_j , flower ]
        vect_flowers.append ( vect_flower )

    # calc axis of bee movement toward flower
    vect_closest = min ( vect_flowers , key=lambda v: abs ( v[ 0 ] ) + abs ( v[ 1 ] ) )

    # BEE MOVEMENT (toward flower if close enough, else random +/- x/y)
    if abs ( vect_closest[ 0 ] ) + abs ( vect_closest[ 1 ] ) < flower_awareness_range:

        if abs ( vect_closest[ 0 ] ) > abs ( vect_closest[ 1 ] ):   # select motion axis y
            if vect_closest[ 0 ] < 0:                               # select direction
                bee.location_i -= 1                                     # up
            else:
                bee.location_i += 1                                     # down
        else:                                                       # select motion axis y
            if vect_closest[ 1 ] < 0:
                bee.location_j -= 1                                     # left
            else:
                bee.location_j += 1                                     # right
    else:
        move_bee_randomly ( bee )

    print ( f'Target Flower: {vect_closest[2]}\t \t Health: {health}' )  # display next target & health

    # ENEMY MOVEMENT
    for pollution in pollutions:                                        # move pollution x/y +/- 1
            pollution.location_i += random.randint ( -1 , 1 )
        else:
            pollution.location_j += random.randint ( -1 , 1 )

    # TOUCH DETECTION
    entity_touch = collision ( bee , entities )                         # detect bee touching an entity

    if entity_touch is not None:                        # calc NEG HEALTH if bee touches pollution
        if type ( entity_touch ) is Pollution:
            health -= 1
            print ( f'Ouch! (health = {health})' )
            # TEST print(type(entity_touch))

        if type ( entity_touch ) is Flower:             # calc POS HEALTH if bee touches flower
            health += entity_touch.health
            print ( f'Yum! (health = {health})' )
            # TEST print(type(entity_touch))
            bee.last_flower2 = bee.last_flower          # set 'flower-before-last' val to 'last flower'
            bee.last_flower = entity_touch              # set 'last flower' to current touch

    if health <= 1:
        print ( 'You\'re dead!' )
        exit ( )
