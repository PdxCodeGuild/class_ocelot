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
    print(c3)

    print('\n')

    c4 = c3.sort()
    print(c4)

    # words_total = len(c4)




