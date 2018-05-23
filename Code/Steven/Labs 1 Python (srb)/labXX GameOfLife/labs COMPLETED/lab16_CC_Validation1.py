# Convert the input string into a list of ints
#card_num = list(input('Input your card number: \n>'))

card_entry_shortcut = input('Test card shortcut: 1 for Valid, 2 for invalid, \'Return\' to quit.\n>')

if card_entry_shortcut == '1':
    card_num = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'.split(' ')

elif card_entry_shortcut == '2':
    card_num = list('1234' * 4)

else:
    exit()

for i in range(len(card_num)):
    card_num[i] = int(card_num[i])

# Slice off the last digit. That is the check digit.
check_digit = card_num.pop()

# Reverse the digits.
card_num.reverse()
print(card_num, '\n')

# Double every other element in the reversed list.
for i in range(0, len(card_num), 2):
    card_num[i] = card_num[i] * 2
    # card_num = [2 * i for i in card_num]
print(card_num, '\n')
# print(i, int(card_num[i])*2, '\n')


# num_list_doubled


# Subtract nine from numbers over nine.
for i in range(len(card_num)):
    if card_num[i] > 9:
        card_num[i] -= 9

print(card_num, '\n')

# Sum all values.
total = sum(card_num)
print(total)

# Take the second digit of that sum.

second_digit = int(str(total)[-1])

if second_digit == check_digit:
    print('Card is valid')

else:
    print('Card is invalid')

# If that matches the check digit, the whole card number is valid.