


import random


i = 0
while i < 100:
    print(random.randint(0, 100))
    i += 1



#              0        1          2
choices = ['apples', 'bananas', 'pears']
print(random.choice(choices))

def random_choice(list):
    random_index = random.randint(0, len(choices)-1)
    return list[random_index]







