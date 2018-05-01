import string
import random

p_len = int(input('How long do you want your password to be? > '))
num_p = int(input('How many passwords do you want? > '))

p_word = ''
for i in range(num_p):
    for j in range(p_len):
        p_word += random.choice(string.ascii_letters + string.digits)
    print(p_word)
    p_word = ''
