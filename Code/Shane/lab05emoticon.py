import random

eye_lst = [":", ";", "=", "}","8"]
nose_lst = [">","-","^","{","~","=="]
mouth_lst = ["J",")","(","|","P","]","[","D"]

count = input("How many faces do you want?\n")

while True:
    for i in range(int(count)):
        print(random.choice(eye_lst) + random.choice(nose_lst) + random.choice(mouth_lst))
    if input("Again, just type a number? \n") == 'no':
        break


