import string

text_in = ''


# Enter text to encode.
while text_in != '.':
    # Select encoding num (1-25, 'Return' for default 13)
    encoding_val = int(input('Select encoding rotation from 1 to 25 \n\t(Hit \'Return\' only for 13, period to quit.) >'))
    print(encoding_val)

    text_in = input('Enter text to encode. \n>')


    for x in range(len(text_in)):
        text_in_num = ord(text_in[x])

        # Adds the rotation value to the ascii num
        text_in_num = text_in_num + encoding_val

        # Cycles text_nums > 26 to # 1, etc.
        if text_in_num > ord('z'):
            text_in_num -= 26

        # Prints entire output string to single line.
        # print(text_in_num, ' ', end="")
        print(chr(text_in_num), end="")
    print()

exit()

# convert to number


# convert to letter
# text_out = chr(text_in_num)
# print(text_out)

# Display encoded text.


# for char in text_in:
#     print(char)
