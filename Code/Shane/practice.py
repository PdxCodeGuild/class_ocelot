import random
lst = []
lstTF = ["T", "F"]
for i in range(10):
    lst.append([])
    for j in range(10):
        lst[i].append(random.choice([True, False]))

def print_out(lst):
    for x in range(10):
        for y in range(10):
            if lst[x][y] == True:
                print("□", end = "")
            else:
                print("■", end = "")
        print()

print_out(lst)