
# dictionaries

num_words_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',9: 'nine'}

num_words_teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

num_words_20_90 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

num_input = 1

while num_input != '':
    num_input = int(input('Enter number to display as a phrase \n>'))

    tens_digit = int(num_input // 10)
    ones_digit = (num_input % 10)

    if num_input < 10:
        print(num_words_ones[num_input])

    elif num_input > 10 and num_input < 20:
        print(num_words_teens[num_input])

    elif num_input > 20 and num_input < 100:
        print(f'{num_words_20_90[tens_digit]}-{num_words_ones[ones_digit]}')


else:
    exit()
