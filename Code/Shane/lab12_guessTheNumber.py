import random


def hot_cold(first, second):
    if first > second:
        return "colder"
    elif first < second:
        return "hotter"
    else:
        return ""


guess_amount = int(input("How many chances do you get?\n:"))

how_big = int(input("How big is this guessing game?\n:"))

answer = random.choice(range(1, how_big+1))

# here for sanity check
# print(answer)

guess_lst = []

hot_or_cold = []

while True:

    guess = int(input("guess a number between 1 and 10\n:"))

    guess_lst.append(guess)

    hot_or_cold.append(abs(guess - answer))

    # print(guess_lst)
    # sanity check
    # print(hot_or_cold)

    if answer == guess:
        print(f"You win, the answer was {answer}.\nYou answered in {len(guess_lst)} tries\n"
              f"Your guesses were {guess_lst}")
        if input("N to stop... Enter to play again.\n").upper() == "N":
            break
        else:
            guess_amount = int(input("How many chances do you get?\n:"))

            how_big = int(input("How big is this guessing game?\n:"))

            answer = random.choice(range(1, how_big + 1))

            # here for sanity check
            print(answer)

            guess_lst = []

            hot_or_cold = []

    elif guess < answer:
        print("Low")
        if len(guess_lst) > 1:
            print(hot_cold(hot_or_cold[-1], hot_or_cold[-2]))
    else:
        print("High")
        if len(guess_lst) > 1:
            print(hot_cold(hot_or_cold[-1], hot_or_cold[-2]))
