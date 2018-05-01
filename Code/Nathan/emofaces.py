import random
eyes_list = [':', ';']
nose_list = ['<', '>']
mouth_list = ['o', 'O']

complete = 0
while complete <= 5:
    complete += 1
    print(random.choice(eyes_list)+ random.choice(nose_list) + random.choice(mouth_list))