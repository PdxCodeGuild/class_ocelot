
import string


def strip_punct(word):
    for p in string.punctuation:
        t_word = word.replace(p, '')
    return t_word


with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read().lower()

lines = contents.split('\n')
word_dict = {}
for line in lines:
    word_list = line.split(' ')
    for word in word_list:
        t_word = strip_punct(word)
        if t_word != '':
            if t_word not in word_dict:
                word_dict[t_word] = 1
            else:
                word_dict[t_word] += 1

words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])

