import random
user_guess_count = 0
user_guess = ""

# Computer sets target number
num_target = random.randint(1,10)

# print('\nYour classroom is set to self-destruct in 15 seconds! - can you guess the deactivation code?\n\t(It is an integer between 1 and 10)')

print(num_target)

while user_guess != num_target:
    user_guess = int(input('\tENTER DEACTIVATION CODE >'))
    user_guess_count = user_guess_count + 1

    # Comp advice 1: "Higher or Lower"
    if user_guess < num_target:
        comp_advice = 'higher'
    else:
        comp_advice = 'lower'


    if user_guess_count == 10:
        print('You dead, bruh.')
        break

    print(f'\nWrong! {10 - user_guess_count} attempts remaining until self-destruct...')
    print(f'(... maybe you should guess {comp_advice})\n')

else:
    print(f'Self-destruct DEACTIVATED. \n\t  You took {user_guess_count} tries.')




