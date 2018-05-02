import string

def move_right(moves):
    shuffled_lst = list(string.ascii_lowercase)
    for i in range(n_rot):
        shuffled_lst.insert(0, shuffled_lst[-1])
        del shuffled_lst[-1]
    return shuffled_lst


n_rot = int(input("What n ROT Cypher do you want?\n:"))

encode = input("input something to encode")

alpha = move_right(n_rot)

reg_lst = list(string.ascii_lowercase)

out = []

for l in encode:
    out.append(reg_lst[alpha.index(l)])
print(''.join(out))


