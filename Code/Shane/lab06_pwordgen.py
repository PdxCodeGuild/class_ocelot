import random
import string

count = int(input('lowercase?\n'))
pword = []
for i in range(count):
    pword += random.choice(string.ascii_lowercase)
count = int(input('how many upper?\n'))
for i in range(count):
    pword += random.choice(string.ascii_uppercase)
count = int(input('how many puncuation?\n'))
for i in range(count):
    pword += random.choice(string.punctuation)
print(pword)
random.shuffle(pword)
pword = "".join(pword)
print(pword)