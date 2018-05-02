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


print(f'{name} the total amount of coins needed is {quarters_needed + dimes_needed + nickels_needed + pennies_needed}\nyou will need\n{quarters_needed} Quarters\n{dimes_needed} Dimes\n{nickels_needed} Nickels\n{pennies_needed} Pennies')

if value_1 > 10000:
    print('Go out to a nice dinner')

else:
    print('Save up and eat top Ramen')



