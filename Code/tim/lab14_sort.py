import random


def random_list(n):
    lst = []
    for i in range(n - 1):
        lst.append(random.randrange(100))
    return lst


def shuffle(lst):
    for i in range(len(lst)):
        s = random.randrange(len(lst))
        t = lst[i]
        lst[i] = lst[s]
        lst[s] = t


def is_sorted(lst):
    for i in range(1, len(lst)):
        print(lst[i - 1], lst[i])
        if lst[i - 1] > lst[i]:
            return False
    return True


def accuracy(lst):
    y = 0
    for i in range(1, len(lst)):
        if lst[i - 1] <= lst[i]:
            y += 1
    return y / len(lst)


lst = random_list(20)
i = 0
b_acc = 0
b_lst = lst.copy()
while not is_sorted(b_lst):
    lst = b_lst.copy()
    r1 = random.randrange(len(b_lst))
    r2 = random.randrange(len(b_lst))

    t = lst[r1]
    lst[r1] = lst[r2]
    lst[r2] = t

    t_acc = accuracy(lst)
    if t_acc > b_acc:
        b_lst = lst.copy()
    i += 1

print(f'That took {i} tries')

