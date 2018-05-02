def remainder(before, total):
    return before - total


change_dict = {'quarter': 25, 'dime': 10, 'nickle': 5, 'penny': 1}

while True:
    change_lst = []

    amount = float(input('Enter a dollar and change amount. i.e. 1.36.  I\'ll give you the fewest coin result.\n:'))

    amount *= 100

    amount = int(amount)

    for i in change_dict:
        change_lst.append(amount // change_dict[i])

        # I just wanted to use a function here, no real need for it
        amount = remainder(amount, amount // change_dict[i] * change_dict[i])

    print(
        f'Your change is {change_lst[0]} quarters, {change_lst[1]} dimes, {change_lst[2]} nickles, {change_lst[3]} pennies')
    if input('run again?\n:') == 'no':
        break
