print('Welcome to the Magic 8-Ball!')

import random

response = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

the_question = input('Enter your Yes or No question. (Enter \'done\' if done) ')

while the_question != 'done':
    magic_answer = random.choice(response)
    print(magic_answer)
    the_question = input('Enter your Yes or No question. (Enter \'done\' if done) ')

