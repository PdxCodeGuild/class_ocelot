import string


def word_count(lines):
    first_loop_count = 0
    second_loop_count = 0
    for word in lines:
        if word not in words:
            words[word] = 1
            first_loop_count += 1
        elif word in words:
            words[word] += 1
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

paired_word = []

for i in range(len(lines)-1):
    paired_word.append((lines[i], lines[i+1]))
print(paired_word)
# check_for_pairs = lines #This is for using in version 2


top_paired_word = sorted((word_count(paired_word)).items(), key=lambda x: x[1], reverse=True)
for i in range(min(10, len(top_paired_word))):
    print(top_paired_word[i])



top_ten_single_word = sorted((word_count(lines)).items(), key=lambda x: x[1], reverse=True)

for i in range(min(10, len(top_ten_single_word))):
    print(top_ten_single_word[i])


### trying the input to start an automatic madlib ###

#start_word = input('write a word\n')



# for i in range(len(top_paired_word)):
#     for j in range(len(top_paired_word[i])):
#         if start_word == top_paired_word
#         print(f"{top_paired_word[0][1]} second for loop")
#



