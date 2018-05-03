
def move_right2(moves):
    shuffled_lst = list(string.ascii_lowercase)
    for i in range(moves):
        last_element = shuffled_lst[-1]
        for j in range(len(shuffled_lst)-1, 0, -1):
            shuffled_lst[j] = shuffled_lst[j-1]
        shuffled_lst[0] = last_element
    print(shuffled_lst)


print(move_right2(1))
exit()
