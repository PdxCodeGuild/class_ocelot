import random
import time

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
noses = [' -  ', ' o  ', ' c  ', ' d  ', ' z  ']
mouths = ['____', '----', ' 0  ', ' Q  ', ' w  ']

i = 0
while i < 10:
    p_eyes = f'{random.choice(eyes)}\t{random.choice(eyes)}\t{random.choice(eyes)}'
    p_noses = f'{random.choice(noses)}\t{random.choice(noses)}\t{random.choice(noses)}'
    p_mouths = f'{random.choice(mouths)}\t{random.choice(mouths)}\t{random.choice(mouths)}'
    print(p_eyes + '\n' + p_noses + '\n' + p_mouths + '\n')
    time.sleep(1)
    i += 1