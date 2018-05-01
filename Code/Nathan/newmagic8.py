import random

name = input('What is your name?')

print('give me on moment to find your fate ')

output_list = ['It is certain','It is decidedly so', 'Without a doubt', 'Yes definitely']



while True:
    input('enter a question: ')
    print(random.choice(output_list))
    question = input('Would you like to ask me a yes or no question? ')
    if question == 'no':
        break



print('Thank you for playing ' + name)