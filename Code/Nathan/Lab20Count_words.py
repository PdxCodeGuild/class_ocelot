import string
with open('goldencoin.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    contents = contents.lower()
    contents = contents.replace('\n', ' ')
    c2 = ''


    for current_char in contents:
        if current_char in (string.ascii_lowercase + ' '):
            c2 += current_char


    c3 = c2.split()
word_pair_list= []
for i in range(len(c3)-1):
    word_pair_list.append((c3[i]) + ' ' + c3[i+1])
word_pair_dict = {}
for word_pair in word_pair_list:
    if word_pair not in word_pair_dict:
        word_pair_dict[word_pair] = 1
    else:
        word_pair_dict[word_pair] += 1
print(word_pair_dict)

    # for word in c3:
    #     if word not in c4:
    #         c4[word] = 1
    #     else:
    #         c4[word] += 1

d5 = list(word_pair_dict.items())
d5.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(d5))):
    print(d5[i])

