# print('Welcome to Change-maker Pro plus, Version 2 Extended (Home version) (multi-user) (Trial)')
print()

# Define Coin Values:
coin_quarter = 25
coin_dime = 1
coin_nickel = 5
coin_penny = 1

while True:

    input_amount = input('Enter total dollar amount and press \'Return\' to see the minimal number of coins required.\n(hit \'Return\' again to quit)\n>:')
    if input_amount == '':
        break

    input_amount = int(100 * float(input_amount))

    print()

    # use as many quarters as possible
    quarter_count_FL = input_amount // coin_quarter
    quarter_count_MD = round(input_amount % coin_quarter, 3)

    # use as many dimes as possible
    dime_count_FL = quarter_count_MD // coin_dime
    dime_count_MD = round(quarter_count_MD % coin_dime, 3)

    # use as many nickels as possible
    nickel_count_FL = dime_count_MD // coin_nickel
    nickel_count_MD = round(dime_count_MD % coin_nickel, 3)

    # use pennies as final remainder
    penny_count_FL = nickel_count_MD // coin_penny

    print(f'The minimum number of coins is {quarter_count_FL + dime_count_FL + nickel_count_FL + penny_count_FL}.')
    print(f'{quarter_count_FL} quarters, {dime_count_FL} dimes, {nickel_count_FL} nickels and {penny_count_FL} pennies.\n\n')
