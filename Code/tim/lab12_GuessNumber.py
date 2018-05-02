import random

hints = 2
guesses = []
diffs = []

def DisplayHintOptions(guesses):
    if len(guesses) > 0:
        print('''Hint Menu
    1 = eliminate a quartile
    2 = divisible by 3?
    3 = greater/less than my last guess
    4 = heat map''')
    else:
        print('''Hint Menu
    1 = eliminate a quartile
    2 = divisible by 3?''')

def AddToGuesses(guesses, diffs, diff):
    guesses.append(guess)
    diffs.append(diff)

def DisplayHeatMap(guesses, diffs):
    p = ''
    for i in range(len(guesses)):
        if i == 0:
            p = f'{guesses[i]}\n'
        else:
            print(diffs[i])
            print(diffs[i - 1])
            p += f'{guesses[i]} {diffs[i] < diffs[i - 1]}\n'.replace('True', 'Warmer').replace('False', 'Colder')
    print(p)

target = random.randrange(1,101)
print('Guess a number 1 to 100. You get 5 guesses and 2 hint (type "hint").')

for i in range(10):
    guess = input(f'Guess #{i + 1}: ')
    if guess.lower() == 'hint':
        x = 1
        # if hints == 0:
        #     print('You have no more hints remaining')
        #     i -= 1
        # else:
        #     DisplayHintOptions(guesses)
        #     hint_num = int(input('Which hint would you like? > '))
        #     if hint_num == 1:
        #         x = 1
        #     elif hint_num == 2:
        #         x = 1
        #     elif hint_num == 3:
        #         x = 1
        #     elif hint_num == 4:
        #         DisplayHeatMap(guesses, diffs)
        #     hints -= 1
    else:
        guess = int(guess)
    if guess in guesses:
        print('You already guessed that, try again')
        i -= 1
    elif type(guess) == int:
        if guess == target:
            print('You got it!')
            break
        else:
            guesses.append(guess)
            diffs.append(abs(guess - target))
            DisplayHeatMap(guesses, diffs)
