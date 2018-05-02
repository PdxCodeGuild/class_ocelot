import string
text_in = input('Enter text to encrypt\n')

#for x in string.ascii_lowercase:
#print(ord(x))

for x in range(len(text_in)):
   text_in_num = ord(text_in[x])
   print(text_in_num)


#for char in text_in:
#    print(char)
