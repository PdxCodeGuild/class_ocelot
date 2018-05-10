
import re
import datetime
from functools import reduce


def month_num(mon_in):
    if mon_in == 'jan' or mon_in == 'january' or mon_in == '1':
        mon_out = 1
    elif mon_in == 'feb' or mon_in == 'february' or mon_in == '2':
        mon_out = 2
    elif mon_in == 'mar' or mon_in == 'march' or mon_in == '3':
        mon_out = 3
    elif mon_in == 'apr' or mon_in == 'april' or mon_in == '4':
        mon_out = 4
    elif mon_in == 'may' or mon_in == 'may' or mon_in == '5':
        mon_out = 5
    elif mon_in == 'jun' or mon_in == 'june' or mon_in == '6':
        mon_out = 6
    elif mon_in == 'jul' or mon_in == 'july' or mon_in == '7':
        mon_out = 7
    elif mon_in == 'aug' or mon_in == 'august' or mon_in == '8':
        mon_out = 8
    elif mon_in == 'sep' or mon_in == 'september' or mon_in == 'sept' or mon_in == '9':
        mon_out = 9
    elif mon_in == 'oct' or mon_in == 'october' or mon_in == '10':
        mon_out = 10
    elif mon_in == 'nov' or mon_in == 'november' or mon_in == '11':
        mon_out = 11
    elif mon_in == 'dec' or mon_in == 'december' or mon_in == '12':
        mon_out = 12
    else:
        mon_out = 0
    return mon_out


pretty_month = {
    1: 'January',
    2: 'Feruary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

with open('rainfall.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

regex = r'(\d+-\w+-\d+) +(\d+)'
data = re.findall(regex, contents)
data = tuple([(datetime.datetime.strptime(d[0], '%d-%b-%Y'), d[1]) for d in data])

while True:
    mon_in = input('Enter a month:\n >')
    mon_out = month_num(mon_in.lower())
    if mon_out > 0:
        month = [int(d[1]) for d in data if d[0].month == mon_out]
        print(f'Average rainfall for {pretty_month[mon_out]}: {round(reduce(lambda x, y: x + y, month) / len(month) / 10, 1)} in')
        break



