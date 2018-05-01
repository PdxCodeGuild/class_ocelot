import random
import chalk

rps = ['ROCK', 'PAPER', 'SCISSORS']

h_ans = input('Rock, Paper or Scissors? > ').upper()
c_ans = random.choice(rps)
print(f'Computer picks: ' + chalk.red(c_ans))

if h_ans in rps:
    if h_ans == c_ans:
        print('tie, lame')
    elif h_ans == 'ROCK' and c_ans == 'PAPER':
        print('Paper covers rock, you lose')
    elif c_ans == 'ROCK' and h_ans == 'PAPER':
        print('Paper covers rock, you win')
    elif c_ans == 'ROCK' and h_ans == 'SCISSORS':
        print('Rock smashes scissors, you lose')
    elif h_ans == 'ROCK' and c_ans == 'SCISSORS':
        print('Rock smashes scissors, you win')
    elif c_ans == 'SCISSORS' and h_ans == 'PAPER':
        print('Scissors cuts paper, you lose')
    else:
        print('Scissors cuts paper, you win')
else:
    print(f'you didn\'t follow the instructions, you lose')
