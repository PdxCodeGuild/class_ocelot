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
    print(f'{10-user_guess_count} attempts remaining...')


# Indicate result

print(f'You guessed the number in {user_guess_count} tries!')

