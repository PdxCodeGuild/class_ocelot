import random

print('I am thinking of a number between 1 and 10')

computer_selection = random.randint(1, 10)
print(computer_selection)

guesses_taken = 0

guess_list = []

while guesses_taken < 11:
    guess = int(input('Take a guess at the number\n'))
    guesses_taken = guesses_taken + 1

    if guess == computer_selection:
        break

    elif guess < computer_selection:
        print('Your guess is too low')
        if

    elif guess > computer_selection:
        print('Your guess is too high')

if guess == computer_selection:
    guesses_taken = str(guesses_taken)
    print('Good job you guessed my number in ' + guesses_taken + ' guesses')

if guess !=computer_selection:
    print(f'Nope, the number I was thinking of was {computer_selection}')









