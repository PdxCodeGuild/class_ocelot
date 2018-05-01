import random

# random beard state
beard_state = random.randint(1, 4)



# define emoticon face components
emo_eyeses = [':', ';', '8']
emo_noses = ['-', 'o', '{']
emo_mouths = [')', '|', '(', 'o', '/', 'P', 'D']
emo_beards = ['>', '>']




if beard_state == 1:
    emo_beard = random.choice(emo_beards)

else:
    emo_beard = ''

# display emoticon
counter1 = 0
while counter1 < 5:
    # randomly select face components
    emo_eyes = random.choice(emo_eyeses)
    emo_nose = random.choice(emo_noses)
    emo_mouth = random.choice(emo_mouths)
    print(emo_eyes + emo_nose + emo_mouth + emo_beard)
    counter1 += 1
