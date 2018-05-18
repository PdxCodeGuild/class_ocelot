import random
eyes_list = [":", ";", "=", "}", "8"]
nose_list = ["==", ">", "-", "^", "{", "~"]
mouth_list = ["J", ")", "(", "|", "P", "]", "[", "D"]

complete = 0
while complete <= 5:
    complete += 1
    print(random.choice(eyes_list)+ random.choice(nose_list) + random.choice(mouth_list))