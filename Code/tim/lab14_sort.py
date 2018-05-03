import random


def random_list(n):
    lst = []
    for i in range(n):
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
        if lst[i - 1] > lst[i]:
            return False
    return True


def accuracy(lst):
    y = 0
    for i in range(1, len(lst)):
        if lst[i - 1] <= lst[i]:
            y += 1
    return y / len(lst)


lst = random_list(14)
i = 0
b_acc = 0
b_lst = lst.copy()
while not is_sorted(b_lst):
    # make temp list 'lst' and swap 2 random places
    t_lst = b_lst.copy()
    r1 = random.randrange(len(t_lst))
    r2 = random.randrange(len(t_lst))

    t_lst[r1] = b_lst[r2]
    t_lst[r2] = b_lst[r1]

    print(t_lst)
    print(b_lst)

    # check accuracy of new temp list
    t_acc = accuracy(t_lst)
    print(r1, r2, t_acc)

    if t_acc >= b_acc:
        b_acc = t_acc
        b_lst = t_lst.copy()

    i += 1

print(f'That took {i} tries')

