import string
import random

# Computer select Rock, Paper or Scissors.
RPS_choices = ['Rock', 'Paper', 'Scissors']


computer_selection = random.choice(RPS_choices)


# User select Rock, Paper or Scissors.
user_input = int(input('Enter 1 for Rock, 2 for Paper, or 3 for Scissors: '))
user_selection = RPS_choices[user_input -1]

# Determine Winner
if user_selection == computer_selection:
    play_result = 'Tie'
elif user_selection == 'Rock' and computer_selection == 'Paper':
    play_result = "Lose"
elif user_selection == 'Rock' and computer_selection == 'Scissors':
    play_result = "Win"
elif user_selection == 'Paper' and computer_selection == 'Scissors':
    play_result = "Lose"
elif user_selection == 'Paper' and computer_selection == 'Rock':
    play_result = "Win"
elif user_selection == 'Scissors' and computer_selection == 'Rock':
    play_result = "Lose"
elif user_selection == 'Scissors' and computer_selection == 'Paper':
    play_result = "Win"


# Display Results
print()
print('I shoot ' + computer_selection + '...')
print('You shoot ' + user_selection + '...')
print()
if play_result != 'Tie':
    print('You ' + play_result + '!')
else: print(play_result + '!')



# future idea - Keep Running tally of score.

