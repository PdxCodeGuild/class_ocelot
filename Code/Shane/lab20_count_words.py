import string


def word_count(lines):
    first_loop_count = 0
    second_loop_count = 0
    for word in lines:
        if word not in words:
            words.update({word: 1})
            first_loop_count += 1
        elif word in words:
            words[word] = words[word]+1
            second_loop_count += 1
    print(f'{first_loop_count} - Original words')
    print(f'{second_loop_count} - Duplicate words')
    return words


words = {}

with open('the_battle_of_talavera.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

for p in string.punctuation:
    contents = contents.replace(p, ' ')

contents = contents.lower()

lines = contents.split()

top_ten = sorted((word_count(lines)).items(), key=lambda x: x[1], reverse = True)

for i in range(min(10, len(top_ten))):
    print(top_ten[i])