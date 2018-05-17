import random



class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class InanimateObject(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '')
        self.character = random.choice(['❀', '🎄'])


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '§')


class Star(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '*')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '☺')


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, j):
        return self.board[j]

    # def collision(player, enemies):

    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print('_|_', end='')
            print()



b = Board(20, 20)
list1 = ()
player_backpack = list1

pi, pj = b.random_location()

player = Player(19, pj)

# enemy = Enemy()

entities = [player]

enemies = []

star = []

for i in range(6):
     ei, ej = b.random_location()
     enemy = Enemy(0, ej)
     entities.append(enemy)
     enemies.append(enemy)

for i in range(2):
    si, sj = b.random_location()
    stars = Star(0, sj)
    entities.append(stars)


# enemy.location_j = ej
#
# enemy.location_i = ei

while True:

    b.print(entities)

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        if player.location_i > 15:
            player.location_i -= 1  # move up
        else:
            print('You can\'t move there: North Bound Limit Error!')
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down


    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)

    for star in star:
        if random.randint(0, 1) == 0:
            star.location_i += random.randint(-5, 0)
        else:
            star.location_j += random.randint(-1, 1)

    if random.randint(0, 3) == 0:
        s = Star(0, random.randint(0, 5))

    #     entities.append(s)
    #     stars.append(s)




    # if player.location_i and player.location_j == stars.location_i and stars.location_j:
    #     player_backpack.append(list(stars))
