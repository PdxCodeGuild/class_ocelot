
import string

with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read().lower()

for p in string.punctuation:
    contents = contents.replace(p, '')
words = contents.replace('\n',' ').split(' ')
words = [word.strip() for word in words if len(word.strip()) > 0]
lr_dict = {}
for i in range(1, len(words) - 1):
    if words[i] not in lr_dict:
        lr_dict[words[i]] = [{}, {}]
    l_word = words[i - 1]
    if l_word not in lr_dict[words[i]][0]:
        lr_dict[words[i]][0][l_word] = 1
    else:
        lr_dict[words[i]][0][l_word] += 1
    r_word = words[i + 1]
    if r_word not in lr_dict[words[i]][1]:
        lr_dict[words[i]][1][r_word] = 1
    else:
        lr_dict[words[i]][1][r_word] += 1

l_word = 'zzzzz'
while l_word not in lr_dict:
    l_word = input('I can has word?\n > ')

r_word = l_word

used_words = [l_word]
p_str = l_word
for i in range(5):
    l_words = list(lr_dict[l_word][0].items())
    l_words.sort(key=lambda tup: tup[1], reverse=True)
    r_words = list(lr_dict[r_word][1].items())
    r_words.sort(key=lambda tup: tup[1], reverse=True)
    t_ind = 0
    while l_words[t_ind][0] in used_words:
        t_ind += 1
    p_str = l_words[t_ind][0] + ' ' + p_str
    l_word = l_words[t_ind][0]

    t_ind = 0
    while r_words[t_ind][0] in used_words:
        t_ind += 1
    p_str = p_str + ' ' + r_words[t_ind][0]
    r_word = r_words[t_ind][0]

    used_words.append(l_word)
    used_words.append(r_word)
print(p_str)
