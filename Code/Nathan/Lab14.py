import random

ran_list = []

for i in range(2):
    ran_list.append(random.randrange(100))

print(ran_list)
random.shuffle(ran_list)



print(is_ordered(ran_list))

def is_ordered(ran_list):
    for i in range(len(ran_list)-1):
        if ran_list[i] > ran_list[i + 1]:
            return False
    return True
if is_ordered(ran_list):
    pass

def create_shuffle(ran_list):
   for i in range(len(ran_list)):
       j = random.randrange(0, len(ran_list))
       t = ran_list[j]
       ran_list[i] = ran_list[j]
       ran_list[j]= t

def bogo_sorting(ran_list):
    while is__ordered != True:
        i += 1
        create_shuffle(ran_list)

    print(f'that took{i} tries')