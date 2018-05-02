import random


pennies = int(input('How many pennies?'))
dollars = int(input('How many dollars?'))

dollars = pennies // 100
pennies -= dollars * 100

quarters = pennies // 25
pennies -= quarters * 25

dimes = pennies // 10
pennies -= dimes * 10

nickles = pennies // 5
pennies -= nickles * 5

pennies = dollars * 100
dollars -= pennies // 100

nickles = dollars * 5
dollars -= nickles //5

dimes = dollars * 10
dollars -= dimes // 10

quarters = dollars * 25
dollars -= quarters // 25

p_string = f'''Your change is:
    dollars: \t{dollars}
    quarters: \t{quarters}
    dimes: \t{dimes}
    nickles: \t {nickles}
    pennies: \t{pennies}'''

d_string = f'''How much are you paying?:
    dollars: \t{dollars}
    quarters: \t{quarters}
    dimes: \t{dimes}
    nickles: \t{nickles}
    pennies: \t{pennies}'''


print(d_string)










