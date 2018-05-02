# Select encoding rotation (1-25).

import string

# Enter text to encode.
text_in = input('Enter text to encode. \n>')

for x in range(len(text_in)):
    text_in_num = int(ord(text_in[x]))
    text_in_num = text_in_num + 13
    print(chr(text_in_num), end="")


# convert to number


# convert to letter
# text_out = chr(text_in_num)
# print(text_out)

# Display encoded text.


# for char in text_in:
#     print(char)
