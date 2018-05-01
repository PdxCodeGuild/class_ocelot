import string
import random

x = ''

for i in range(15):
    for j in range(20):
        x += random.choice(string.ascii_letters + string.digits)

    print(x)
    x = ''