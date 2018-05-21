import random
ran_list = []

def is_ordered(ran_list):
    for i in range(len(ran_list)-1):
        if ran_list[i] > ran_list[i + 1]:
            return False
    return True

def create_shuffle(ran_list):
   for i in range(len(ran_list)):
        j = random.randrange(0, len(ran_list)-1)
        t = ran_list[i]
        ran_list[i] = ran_list[j]
        ran_list[j] = t

def bogo_sorting(ran_list):
    i = 0
    while not is_ordered(ran_list):
        i += 1
        create_shuffle(ran_list)

    print(f'that took {i} tries')
    print(ran_list)


for i in range(10):
    ran_list.append(random.randrange(101))

bogo_sorting(ran_list)

