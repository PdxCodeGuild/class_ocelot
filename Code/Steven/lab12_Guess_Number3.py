import random
user_guess_count = 0
user_guess = ""
wrong_guess_margin = 0

# Computer sets target number
num_target = random.randint(1,10)

print('\nYour classroom is set to self-destruct in 15 seconds!')
print('\n\tTo deactivate self-destruct, enter the code number (1 - 10)')
print(f'\tHint: It\'s {num_target}')

while user_guess != num_target:
    user_guess = int(input('\tENTER DEACTIVATION CODE >'))
    wrong_guess_margin_PREVIOUS = wrong_guess_margin

    wrong_guess_margin = abs(user_guess - num_target)
    # print(wrong_guess_margin)

    # Count guesses
    user_guess_count = user_guess_count + 1

    # Comp advice 2: "Warmer or Colder"
    if wrong_guess_margin == 1:
        comp_advice = 'YOU\'RE WALKING ON THE SUN!!'

    elif wrong_guess_margin < wrong_guess_margin_PREVIOUS:
        comp_advice = 'Getting warmer...'

    elif wrong_guess_margin > wrong_guess_margin_PREVIOUS:
        comp_advice = 'Getting colder...'

    else:
        comp_advice = 'You remain equally wrong.'

    # if user_guess < num_target:
    #     comp_advice = 'higher'
    # else:
    #     comp_advice = 'lower'


    if user_guess_count == 10:
        print('\n You have exploded. Have a nice day.')
        break

    print(f'\n {comp_advice} {10 - user_guess_count} attempts remaining until self-destruct')

else:
    print(f'Self-destruct DEACTIVATED. \n\t  You took {user_guess_count} tries.')




