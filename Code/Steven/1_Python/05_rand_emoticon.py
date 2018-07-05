import random

# define sideways face parts
eyeses = [':', ';', '8']
noses = ['-', 'o', '^']
mouths = ['D', 'P', 'p', ')', '/', '|', '(', '<']
# head_left = ' ⏜ '
# head_right = ' ⏝ '

# choose random face parts
eyes = random.choice(eyeses)
nose = random.choice(noses)
mouth = random.choice(mouths)

print('\n\n')

for mouth in mouths:
    # print( head_left, end="\t")
    print(eyes + nose + mouth, end="\t")
    # print(head_right, end="\t")
print('\n\n\n\n')


