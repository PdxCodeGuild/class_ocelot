

import random
#
guess_amount = 10

how_big = int(input("How big is this guessing game?\n:"))

answer = random.choice(range(1, how_big+1))

print(answer)

guess_lst = []

while True:

    guess = int(input("guess a number between 1 and 10\n:"))

    guess_lst.append(guess)

    if answer == guess:
        print(f"You win, the answer was {answer}.\nYou answered in {len(guess_lst)} tries\n"
              f"Your guesses were {guess_lst}")
        break
    elif guess < answer:
        print("Low")

    else:
        print("High")