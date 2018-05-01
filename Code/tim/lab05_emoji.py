import random

eyes = ['o  o', 'o  o', 'o  o', 'o  o',
        '-  -', '-  -', '-  -', '-  -',
        '0  0', '0  0', '0  0', '0  0',
        'D  D', 'D  D', 'D  D', 'D  D',
        'X  X', 'X  X',
        'x  x', 'x  x',
        '$  $', '$  $',
        'C  C',
        '() ()',
        '9  9']

noses = [' - ', ' o ', ' c ', ' d ', ' z ']

mouths = ['___', '---', ' 0 ', ' Q ', ' w ']

print(f'{random.choice(eyes)}/n{random.choice(noses)}/n{random.choice(mouths)}')