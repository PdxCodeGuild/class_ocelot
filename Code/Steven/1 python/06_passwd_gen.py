import string, random

x = ''

for i in range(15):

    x = ''
    for j in range(12):
        x += random.choice(string.ascii_letters + string.digits)
    print(x)

