import random


attempts = 1
answer = random.randint(1, 20)
isCorrect = False
guess = int(input('What\'s your guess? '))

while answer != guess and attempts < 6:
    if guess < answer:
        print('Higher')
    if guess > answer:
        print('Lower')
    guess = int(input('Take a guess. '))
    attempts += 1


if attempts == 6:
    print('\nSorry you lose... ')
    print('You should have picked', answer)

else:
    print('\nYou win!, The number was', answer)
    print('You guessed it in', attempts, 'attempts')













