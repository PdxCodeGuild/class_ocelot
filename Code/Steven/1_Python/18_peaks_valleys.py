import random

source_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

fruits = ['🍏', '🍎', '🍐', '🍊', '🍋', '🍉', '🍇', '🍓', '🍑']
# shapes = ['⿰', '⿱', '⿵', '⿶', '⿷', '⿸', '⿹', '⿹', '⿺']

play = 'on'

max_val = max(source_data)
fruit_len = len(fruits)

display_choice = int(input('Enter 1 for Xs, 2 for squares and 3 for random fruit\n>'))
if display_choice == '':
    play = 'off'

print()
print()
# while play == 'on':


for i in range(max_val, 0, -1):
    for j in range(len(source_data)):
        if source_data[j] >= i:
            # print('X ', end=' ')

            if display_choice == 1:
                print('X ', end=' ')
            elif display_choice == 2:
                print('☐️ ', end=' ')
            else:
                rand_fruit = random.choice(fruits)
                print(rand_fruit, end=' ')
        else:
            print('  ', end=' ')
    print()
print()
    # print(display_choice)
    # display_choice = input('Enter 1 for Xs, 2 for squares, and 3 for random fruit.\nHit \'Enter\' only to quit\n>')
    # if display_choice == '':
    #     play = 'off'

# Todo: Add water to valleys
