import string

with open('clue_golden_coin.txt', 'r', encoding='utf-8') as txt_src_in1:

    contents = txt_src_in1.read()  # read the contents

    contents = contents.lower()
    contents = contents.replace('\n', ' ')

    char_src1a = ''

    for char_current in contents:
        if char_current in (string.ascii_lowercase + ' '):
            char_src1a += char_current

    char_src1b = char_src1a.split()

with open('clue_golden_coin.txt', 'r', encoding='utf-8') as txt_src_in1:

    contents = txt_src_in1.read()  # read the contents

    contents = contents.lower()
    contents = contents.replace('\n', ' ')

    char_src1a = ''

    for char_current in contents:
        if char_current in (string.ascii_lowercase + ' '):
            char_src1a += char_current

    char_src1b = char_src1a.split()

word_pair_list = []
for i in range(len(char_src1b) - 1):
    word_pair_list.append(char_src1b[i] + ' ' + char_src1b[i + 1])


word_pair_dict = {}

for word_pair in word_pair_list:
    if word_pair not in word_pair_dict:
        word_pair_dict[word_pair] = 1
    else:
        word_pair_dict[word_pair] += 1

# print(word_pair_dict)

list_out1 = list(word_pair_dict.items())
list_out1.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(list_out1))):
    print(list_out1[i])



