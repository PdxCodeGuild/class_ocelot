
import random


print('Welcome to the Magic 8-Ball!')

confidence = int(input('How confident are you today? 2 = Very, 1 = Slightly, or 0 = Not at all.\n>'))

response_pos = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes']

response_neutral = ['Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again']

response_neg = ['Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


the_question = input('\nEnter your Yes or No question. (Hit \'Enter\' when done) ')

while the_question != '':
    if confidence == 2:
        response_list = random.choice([response_pos, response_neutral, response_neg, response_pos])
    else:
        response_list = random.choice([response_pos, response_neutral, response_neg, ['That\'s a stupid question.']])

    magic_answer = random.choice(response_list)

    print(magic_answer + '\n')
    the_question = input('Enter your Yes or No question. (Enter \'done\' if done) ')

