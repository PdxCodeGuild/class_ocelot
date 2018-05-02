import string
import random

o_list = list(string.ascii_letters + string.punctuation + string.digits)
s_list = list(string.ascii_letters + string.punctuation + string.digits)
random.shuffle(s_list)

e_dict = {}
d_dict = {}
for i in range(len(o_list)):
    e_dict[o_list[i]] = s_list[i]
    d_dict[s_list[i]] = o_list[i]

while True:
    str = input('Enter string > ')
    p_e = ''
    p_d = ''
    if str.lower() == 'done':
        break
    else:
        for c in str:
            if c == ' ':
                p_e += ' '
                p_d += ' '
            else:
                p_e += e_dict[c]
                p_d += d_dict[c]
    print(f'Encrypted > {p_e}')
    print(f'Decrypted > {p_d}')