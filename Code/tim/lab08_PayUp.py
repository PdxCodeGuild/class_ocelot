import random

# def change(o, p):
#
#     return(due)

#randrange(self, start, stop=None, step=1, _int=int)

pennies = int(input('How many pennies? > '))

dollars = pennies // 100
pennies -= dollars * 100

halfers = pennies // 50
pennies -= halfers * 50

quarters = pennies // 25
pennies -= quarters * 25

dimes = pennies // 10
pennies -= dimes * 10

nickles = pennies // 5
pennies -= nickles * 5

wooden_nickles = pennies // 3
pennies -= wooden_nickles * 3

super_pennies = pennies // 2
pennies -= super_pennies * 2

p_string = f'''Your change:
    dollars:\t{dollars}
    half-dollars:\t{halfers}
    quarters:\t{quarters}
    dimes:\t{dimes}
    nickles:\t{nickles}
    wooden nickles:\t{wooden_nickles}
    super pennies:\t{super_pennies}
    pennies:\t{pennies}'''

print(p_string)
