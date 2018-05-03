text_in = ''

while text_in != '.':
    encoding = int(input('\nSelect distance moved (1-25) >'))
    text_selected = input('Enter text to encode. \n> ')


    for x in range(len(text_in)):
        text_in_num = int(ord(text_selected[x]))
        text_in_num = text_in_num + encoding

        if text_in_num > 26:
            text_in_num -= 26

        print(chr(text_in_num), end="")


