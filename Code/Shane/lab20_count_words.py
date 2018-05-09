import string

words = {}

with open('the_battle_of_talavera.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

for p in string.punctuation:
    contents = contents.replace(p, ' ')
contents = contents.replace("\n", ' ')

contents = contents.lower()

lines = contents.split()

#print(lines)

for word in lines:
    if word not in words:
        words.update({word: 1})
        if word in words:
            print('I\'m here')

print(words)