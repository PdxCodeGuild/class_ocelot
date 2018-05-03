import random

ran_list = []

for i in range(2):
    ran_list.append(random.randrange(100))

print(ran_list)
random.shuffle(ran_list)
def is_ordered(ran_list):
    for i in range(len(ran_list)-1):
        if ran_list[i] > ran_list[i + 1]:
            print('not ordered')
            return False
    return True


print(is_ordered(ran_list))


if is_ordered(ran_list):
    pass