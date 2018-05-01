import string
import random

user_response_letters = int(input('How many letters would you like your password to be?\n'))
user_response_digits = int(input('How many digits would you like in the password?\n '))

password= []

for i in range(user_response_letters):
    password += (random.choice(string.ascii_letters))

for i in range(user_response_digits):
    password += (random.choice(string.digits))
random.shuffle(password)
password= ''.join(password)
print(password)

