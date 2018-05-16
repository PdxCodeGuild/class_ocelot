import random


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Food(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '')
        self.character = random.choice(['🧀', '🥜'])


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🐱')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🐭')


class Board:
    def __init__(self, width, height):
        self.width = 20
        self.height = 10

    def random_location(self):
        return random.randint(0, self.height - 1), random.randint(0, self.width - 1)

    def __getitem__(self, j):
        return self.board[j]

    # populates board with blanks and entities
    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print('⬜︎', end='')
            print()




def collision(player, entities):
    # test if player is on same square as any entity (food or enemy)
    for entity in entities:
        if entity != player:
            if player.location_i == entity.location_i and \
                    player.location_j == entity.location_j:
                return entity
    return None





# set parameters
b = Board(20, 10)
move_mult = 1
enemy_count = 4
food_count = 4
health = 3

# set player start position, random
pi, pj = b.random_location()
player = Player(pi, pj)

# make entity list (player, enemies, and food), make enemies list, make foods list
entities = [player]
enemies = []
foods = []

# add enemies to entity list and to enemy list
for i in range(enemy_count):
    ei, ej = b.random_location()
    enemy = Enemy(ei, ej)
    # TESTING: print(enemy)

    entities.append(enemy)
    enemies.append(enemy)

# add food to entity list and to foods list
for i in range(food_count):
    fi, fj = b.random_location()
    food_touch = Food(fi, fj)

    entities.append(food_touch)
    foods.append(food_touch)


fi, fj = b.random_location()
food = Food(fi, fj)
entities.append(food)

# TESTING: prints all entities
# for entity in entities:
#     print(entity)

while True:

    # print all entities
    b.print(entities)                           # tells board to print


    command = input('what is your command? ')  # get the command from the user


    # player control
    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= (1 * move_mult)  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += (1 * move_mult)  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= (1 * move_mult)  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += (1 * move_mult)  # move down

    # move enemies 1 square in a random direction
    for enemy in enemies:
        if random.randint(0, 1) == 0:
            enemy.location_i += random.randint(-1, 1)
        else:
            enemy.location_j += random.randint(-1, 1)

    # detect player touching an entity (either food or enemy)
    entity_touch = collision(player, entities)

    if entity_touch is not None:
        if type(entity_touch) is Enemy:
            health -= 1
            print(f'Ouch! (health = {health})')
            # TEST print(type(entity_touch))

        if type(entity_touch) is Food:
            health += 1
            print(f'Yum! (health = {health})')
            # TEST print(type(entity_touch))

    if health <= 1:
        print('You\'re dead!')
        exit()
