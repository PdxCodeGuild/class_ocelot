import random

positive = """It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
""".split('\n')

negative = """Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful""".split('\n')

neutral = """Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again""".split('\n')

choices = [positive, neutral]
neg_keywords = ['wife','girlfriend','job','work','money','rich']

print('Welcome to Magic Eight Ball, ' + input('What is your name? > '))

while True:
    response = input('What is your question? > ')
    if response == 'I\'m done with you':
        print('Fine! I don\'t like you either!')
        break
    response = response.split(' ')
    for word in response:
        if word in neg_keywords:
            l = negative
    if not l:
        l = random.choice(choices)
    print(random.choice(l))