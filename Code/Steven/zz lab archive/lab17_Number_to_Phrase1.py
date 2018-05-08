# input number

num_words_ones = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

num_words_teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

num_words_tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

# num_input = int(input('\nEnter number to display as a phrase \n>'))
num_input = int(0)

# tens_digit = num_input//10
# ones_digit = num_input%10
tens_digit = int(3)
ones_digit = int(0)

print(tens_digit)
print(ones_digit)
print('\n')
print(num_words[tens_digit+18])
print(num_words[ones_digit])


# for i in range(30):
#     print(num_words[i])

# if num_input <21:
#     print(num_words[num_input])
#
# else:
#     num_input >= 21
#     print(f'{num_words[tens_digit+18]}-{num_words[ones_digit]}')

