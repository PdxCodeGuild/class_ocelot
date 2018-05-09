import string

with open('clue_golden_coin.txt', 'r', encoding='utf-8') as f:

    contents = f.read()  # read the contents

    contents = contents.lower()
    contents = contents.replace('\n', ' ')

    c2 = ''

    for char_current in contents:
        if char_current in (string.ascii_lowercase + ' '):
            c2 += char_current

    c3 = c2.split()

    c4 = {}
    for word in c3:
        if word not in c4:
            c4[word] = 1
        else:
            c4[word] += 1

print(c4)

# c5 = list(c4.items())
# c5.sort(key=lambda tup: tup[1], reverse=True)
# for i in range(min(10, len(c5))):
#     print(c5[i])




