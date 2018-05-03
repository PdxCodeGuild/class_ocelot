text_in = ''

# Select encoding rotation (1-25).

import string


# Enter text to encode.

while text_in != '.':
    encoding = int(input('\nSelect encoding rotation (1-25) >'))
    text_in = input('Enter text to encode. \n>')


    for x in range(len(text_in)):
        text_in_num = ord(text_in[x]))

        # Adds the rotation value to the ascii num
        text_in_num = text_in_num + encoding

        # Cycles text_nums > 26 to # 1, etc.
        if text_in_num > 26:
            text_in_num -= 26

        # Prints entire output string to single line.
        print(chr(text_in_num), end="")

# convert to number


# convert to letter
# text_out = chr(text_in_num)
# print(text_out)

# Display encoded text.


# for char in text_in:
#     print(char)
