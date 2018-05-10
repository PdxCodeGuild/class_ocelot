import string, re

# get book contents
bk_name = 'clue_golden_coin.txt'
with open(bk_name, 'r', encoding='utf-8') as bk_contents:
    bk_contents = bk_contents.read()  # read the contents

# make word list of book contents
# wds_all = bk_contents.split()

characters = len(re.findall(r'\w', bk_contents))

words = len(re.findall(r'\w+', bk_contents))

sentences = len(re.findall(r'[^.!?]+', bk_contents))


print(characters, 'characters')
print(words, 'words')
print(sentences, 'sentences')

score = round((4.71 * (characters/words) + 0.5 * (words/sentences) - 21.43)+.5)
print(score)




ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


print('--------------------------------------------------------')

print(f'The ARI for {bk_name} is {score}')
print(f'This corresponds to a {ari_scale[score]["grade_level"]} level of difficulty')
print(f'that is suitable for an average person {ari_scale[score]["ages"]} years old.')

print('--------------------------------------------------------')