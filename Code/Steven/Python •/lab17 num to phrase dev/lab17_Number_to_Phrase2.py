
num_input = 0
num_words_out = ''

# Make list of num words from 0 to 9
num_words_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',9: 'nine'}

# Make list of num words from 10 to 19
num_words_teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

# Make list of num words of "tens" from 20 to 90
num_words_20_90 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def num_to_words(num_input):
    # tens_digit = num_input // 10
    # ones_digit = num_input % 10

    # tens_digit = 50
    # ones_digit = 5

    print(num_input)

    if num_input < 10:
        num_words_out = num_words_ones[num_input]

    elif num_input > 10 and num_input < 20:
        num_words_out = num_words_teens[num_input]

    elif num_input > 20:
        num_words_out = num_words_20_90[tens_digit], num_words_ones[ones_digit]

    else:
        exit()


# num_input = 5

# input number
while num_input != '':
    # print(int(input('\nEnter number to display as a phrase \n>')))
    num_input = int(input('Enter number to display as a phrase>'))

    # num_to_words[num_input]
    # output_words = num_words_out
    print(num_words_out)




