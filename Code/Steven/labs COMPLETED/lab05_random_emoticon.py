import random

# define emoticon face components
emo_eyeses = [':', ';', '8']
emo_noses = ['-', 'o', '^']
emo_mouths = ['D', 'P', 'p', ')', '/', '|', '(', '<']
emo_beards = ['>', '⊃']

# randomly select face components
emo_eyes = random.choice(emo_eyeses)
emo_nose = random.choice(emo_noses)

# random beard state
beard_state = random.randint(1, 4)
if beard_state == 1:
    emo_beard = random.choice(emo_beards)
else:
    emo_beard = ''

# display emoticon
counter1 = 0
print('\n')
while counter1 < 5:
    # mouth select
    emo_mouth = random.choice(emo_mouths)
    print(emo_eyes + emo_nose + emo_mouth + emo_beard)
    counter1 += 1

print()
print()
emo_eyes = random.choice(emo_eyeses)
emo_nose = random.choice(emo_noses)
for emo_mouth in emo_mouths:
    print(emo_eyes + emo_nose + emo_mouth + emo_beard)
