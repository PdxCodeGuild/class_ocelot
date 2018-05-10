
import re
from functools import reduce
import matplotlib.pyplot as plt
from dateutil.parser import parse



def is_date(string):
    try:
        parse(string)
        return True
    except ValueError:
        return False


with open('rainfall.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

regex = r'(\d+-\w+-\d+) +(\d+)'
data = re.findall(regex, contents)
data = tuple([(parse(d[0]), int(d[1])) for d in data])

while True:
    s_date = input('Enter a start date:\n >').replace('/', '-')
    if not is_date(s_date):
        print('Enter as a date, ya hoser')
        continue
    e_date = input('Enter a end date:\n >').replace('/', '-')
    if not is_date(e_date):
        print('Enter as a date, ya hoser')
        continue
    s_date = parse(s_date)
    e_date = parse(e_date)
    days = [d for d in data if s_date <= d[0] <= e_date]
    for d in days:
        if d[1] > 0:
            plt.plot(d[0].date(), d[1] / 10, 'ro')
    plt.show()
    break


