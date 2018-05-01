
import random

cases = {'paper' : ['rock', 'scissor'], "rock" : ['scissor','paper'], "scissor": ['paper', 'rock']}



while True:
    human = input("Choose... rock, paper or scissor\n").lower()

    computer = random.choice(['rock', 'paper', 'scissor'])

    print(computer)

    if human == computer:
        print("you tied")
    elif human == computer[0]:
        print("you lose")
    else:
        print('you win')
    if input("play again? Hit Enter\n ") == 'no':
        break