
test_string = 'TESTSTRING'
output = ''
n_pos = 0
for i in range(len(test_string)):
    for j in range(len(test_string)):
        if j == n_pos:
            output += 'n'
        else:
            output += test_string[j]
    n_pos += 1
    print(output)
    output = ''