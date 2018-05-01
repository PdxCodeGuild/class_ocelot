import random
import string

count = int(input("How long should the password be: \n"))
print(count)
password = ""

selection = string.ascii_letters + string.digits + string.punctuation

while count > 0:
	password += random.choice(selection)
	count -= 1

print(password)