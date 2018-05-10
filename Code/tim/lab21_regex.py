
import re
import string

with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read().lower().replace('\n', ' ').replace('\t', ' ')

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

t_words = 0
t_words_len = 0
t_sent = 0

sentences = re.split('[.?!]', contents)
for s in sentences:
    words = s.split(' ')
    if len(words) > 1:
        t_sent += 1
    t_words += len(words)
    #  print('Words in sentence:', len(words))
    for w in words:
        #  print('Word length:', len(w))
        t_words_len += len(w)

char_per_word = t_words_len / t_words
words_per_sent = t_words / t_sent

ind = int(4.71 * char_per_word + .5 * words_per_sent - 21.43)
grade = ari_scale[ind]['grade_level'].split()[0]
ages = ari_scale[ind]['ages']

print('Book intended for ' + grade + '-graders (ages ' + ages + ')')






