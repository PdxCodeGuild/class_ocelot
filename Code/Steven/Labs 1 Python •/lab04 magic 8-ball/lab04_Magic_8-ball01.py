import random

print('Welcome to the Magic 8-Ball!')

# Load magic responses
response = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

# Input question
the_question = input('Enter your Yes or No question. (Enter \'done\' if done) ')

# Print random answer
while the_question != 'done':                                           # If input != 'done'
    magic_answer = random.choice(response)                              # Randomly choose answer from list
    print(magic_answer)                                                 # Print answer
    print ()                                                            # Print blank line
    the_question = input('Enter your Yes or No question. (Enter \'done\' if done) ')    # Repeat...


