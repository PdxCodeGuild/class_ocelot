

import random


#rps = ['rock', 'paper', 'scissors']
human_score = 0
computer_score = 0

for i in range(1000000):
    computer_choice = random.randint(0,2)
    human_choice = random.randint(0,0)

    if human_choice != computer_choice:
        if human_choice == (computer_choice+1)%3:
            human_score += 1
        else:
            computer_score += 1

print(f'computer score: {computer_score}\nhuman score: {human_score}')

print(computer_score/human_score)








