name = input('Hello, let\'s start with your name? \n')
value = float(input('What is the dollar amount, ie 1.36, that you would like to use the least amount of coins for?> \n'))

value = value*100
value_1 = int(value)


quarter = 25

dime = 10

nickel = 5

penny = 1

quarters_needed = value_1//25

remainder = value_1 % 25
dimes_needed = remainder // 10

nickels_needed = remainder % 10
remainder = remainder // 5

remainder = remainder % 5
pennies_needed = remainder // 1


print(f'{name}, You will need, {quarters_needed} Quarters, {dimes_needed} Dimes, {nickels_needed} Nickels and {pennies_needed} Pennies')




