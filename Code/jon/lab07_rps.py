import random

print('Let\'s play Rock, Paper, Scissors!')



rps = ['rock', 'paper', 'scissors']
you = input('rock, paper, or scissors?')
cpu = random.choice(rps)

if you in rps:
    if you == cpu:
        print('tie')
    elif you == 'rock' and cpu == 'paper':
        print('loser')
    elif you == 'paper' and cpu == 'rock':
        print('winner')
    elif you == 'scissors' and cpu == 'paper':
        print('winner')
    else:
        print(f'{you} beats {cpu}')
else:
    print('good job!')



