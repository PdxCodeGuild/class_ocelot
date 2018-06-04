import random

num_input = 0
ones_digit = 0
tens_digit = 0
hund_digit = 0
thou_digit = 0

def print_answer():
    print(f'You entered the number {num_words_out}.\n')

def out_of_range():
    oor_msg_list = ['I don\'t know that...', 'Come on, nobody knows that.', 'Ummm... Forty-two??']
    oor_msg = random.choice(oor_msg_list)
    print(f'{oor_msg} Please enter a number less than 10,000.\n')

# Offset ints - permitting the num word dictionaries to use meaningful key numbers that match the associated values
num_words_teens_offset = 10
num_words_20_90_offset = 2

# Make list of num words from 0 to 9
num_words_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',9: 'nine'}

# Make list of num words from 10 to 19
num_words_teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

# Make list of num words of "tens" from 20 to 90
num_words_20_90 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

while num_input != '':
    num_input = int ( input ( 'Enter number to display as a phrase (Enter -1 to exit): ' ) )

    ones_digit = num_input % 10
    tens_digit = num_input // 10
    hund_digit = num_input // 100
    thou_digit = num_input // 1000

    # print(f'ones: {ones_digit}, tens: {tens_digit}, hund: {hund_digit}, thou: {thou_digit}') # TESTER

    if num_input < 0:                                          # Ones place
        print('Game Over - thanks for playing.')
        exit()

    if num_input >= 0 and num_input < 10:                                          # Ones place
        num_words_out = num_words_ones[ones_digit]
        print_answer ( )

    elif num_input >= 10 and num_input < 20:                    # Tens place: Teens
        ones_digit = int(ones_digit) + num_words_teens_offset
        num_words_out = num_words_teens[ones_digit]
        print_answer ( )

    elif num_input >= 20 and num_input < 100:                   # Tens place: 20-99
        if ones_digit == 0:
            num_words_out = num_words_20_90[ tens_digit ]
            print_answer ( )
        else:
            num_words_out = num_words_20_90[ tens_digit ] , '-' , num_words_ones[ ones_digit ]
            num_words_out = ''.join ( num_words_out )
            print_answer ( )
            # print('macaroni 1'')

    # TODO Create hundreds and thousands place recognition
    # elif num_input >= 100 and num_input < 1000:                 # Hundreds place
    #     if ones_digit == 0:
    #         num_words_out = num_words_20_90[ tens_digit ]
    #     else:
    #         num_words_out = num_words_20_90[tens_digit], '-', num_words_ones[ones_digit]
    #         num_words_out = ''.join(num_words_out)

    # elif num_input >= 1000 and num_input < 10000:               # Thousands place
    #     ones_digit = int(ones_digit) + num_words_teens_offset
    #     num_words_out = num_words_teens[ones_digit]

    elif num_input >= 10000:                                    # >= 10,000
        print_oor = out_of_range ()
        print(print_oor)


    # TODO Complete comments



