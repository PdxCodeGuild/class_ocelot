import random


def random_list(n):
    lst = []
    for i in range(n - 1):
        lst.append(random.randrange(0, 20))
    return lst


def shuffle(lst):
    for i in range(len(lst)):
        s = random.randrange(len(lst))
        t = lst[i]
        lst[i] = lst[s]
        lst[s] = t


def is_sorted(lst):
    for i in range(1, len(lst)):
        #print(lst[i - 1], lst[i])
        if lst[i - 1] > lst[i]:
            return False
    return True


lst = random_list(20)
saved_list = lst.copy()

shuffle(lst)

print(saved_list)
print(lst)

i = 0
while not is_sorted(lst):
    i += 1
    shuffle(lst)

    if i%100 == 0:
        print(i)

print(f' That took {i} tries')


