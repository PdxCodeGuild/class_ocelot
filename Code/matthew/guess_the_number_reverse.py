

def guess_the_number(lower_bound, upper_bound):
    print(f'{lower_bound} - {upper_bound}')
    if lower_bound >= upper_bound:
        print('I\'ve been lied to.')
        return

    guess = (lower_bound + upper_bound)//2
    answer = input(f'is it {guess}? ').lower()
    if answer in ['yes', 'y', 'yeah', 'duh']:
        print('got it!')
    else:
        hl = input('is it higher or lower? ').lower()
        if hl == 'lower':
            guess_the_number(lower_bound, guess)
        else:
            guess_the_number(guess, upper_bound)


lower_bound = 0
upper_bound = 100
print(f'pick a number between {lower_bound} and {upper_bound}')
guess_the_number(lower_bound, upper_bound)












