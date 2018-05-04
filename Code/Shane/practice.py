import random
lst = []
def make_lst(lst):
    for i in range(10):
        lst.append(random.choice([True, False]))
        # for j in range(10):
        #     lst[i].append(random.choice([True, False]))
    print(lst)

def print_out(lst):
    # for x in range(10):
    for y in range(10):
        if lst[y]:
            print("□", end = "")
        else:
            print("■", end = "")
    print()
lst0 = []
make_lst(lst0)
lst1 = []
make_lst(lst1)
lst2 = []
make_lst(lst2)
lst3 = []
make_lst(lst3)
lst4 = []
make_lst(lst4)
lst5 = []
make_lst(lst5)
lst6 = []
make_lst(lst6)
lst7 = []
make_lst(lst7)
lst8 = []
make_lst(lst8)
lst9 = []
make_lst(lst9)

print_out(lst0)
print_out(lst1)
print_out(lst2)
print_out(lst3)
print_out(lst4)
print_out(lst5)
print_out(lst6)
print_out(lst7)
print_out(lst8)
print_out(lst9)






