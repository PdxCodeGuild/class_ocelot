import random

length = 5

def random_list(length):
    r_lst = []
    for i in range(length):
        r_lst.append(random.randrange(100))
    return r_lst


def shuffle(lst):
    random.shuffle(lst)
    return lst


def sorted(n_list):
    for i in range(len(n_lst)-1):
        if n_lst[i] > n_lst[i+1]:
            return False
    return True


def bogo(n_lst):
    i = 0
    while not sorted:
        i += 1
        shuffle(n_lst)
    print (i)

n_lst = random_list(length)
print(n_lst)
shuffle(n_lst)
print(n_lst)
sorted(n_lst)
bogo(n_lst)