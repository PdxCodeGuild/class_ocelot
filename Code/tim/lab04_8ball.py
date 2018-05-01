import random

choices = """It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful""".split('\n')

print('Welcome to Magic Eight Ball, ' + input('What is your name? > '))

while True:
    question = input('What is your question? > ')
    if question == 'I\'m done with you':
        print('Fine! I don\' like you either!')
        break
    print(random.choice(choices))