source_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

max_val = max(source_data)
# print('max val = ', max_val)

for i in range(max_val, 0, -1):
    for j in range(len(source_data)):
        if source_data[j] >= i:
            print('⚪️', end=' ')
        else:
            print('  ', end=' ')
    print()






