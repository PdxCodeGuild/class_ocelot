
import string


def strip_punct(word):
    for p in string.punctuation:
        t_word = word.replace(p, '')
    return t_word


with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read().lower()

words = contents.replace('\n',' ').split(' ')
words = [word.strip() for word in words if len(word.strip()) > 0]
dbl_dict = {}
for i in range(1, len(words)):
    t_dbl = strip_punct(words[i-1] + ' ' + words[i])
    if t_dbl not in dbl_dict:
        dbl_dict[t_dbl] = 1
    else:
        dbl_dict[t_dbl] += 1


words = list(dbl_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])

