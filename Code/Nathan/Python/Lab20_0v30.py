import string
with open('goldencoin.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    contents = contents.lower()
    contents = contents.replace('\n', ' ')
    c2 = ''
    word_selected = input('Please enter a word')

    for current_char in contents:
        if current_char in (string.ascii_lowercase + ' '):
            c2 += current_char

    c3 = c2.split()
print(c3)

word_selected_list = []
for i in range(len(c3)-1):
    if word_selected is c3[i]:
        word_selected_list.append(c3[i]) + ' ' + c3[i + 1]
        print(i)

print(len(c3))
#word_selected_dict = {}
# for word_selected in word_selected_list:
#     if word_selected not in word_selected_dict:
#         word_selected_dict[word_selected] = 1
#     else:
#         word_selected_dict[word_selected] += 1
# print(word_selected_list)
