import matplotlib.pyplot as plt
import string, re, datetime
import requests

url = 'https://or.water.usgs.gov/non-usgs/bes/'
def get_locations():
    r = requests.get(url)
    locations = re.findall(r'\w+\.rain', r.text)
    locations.sort()
    return locations

def get_file(location):
    r = requests.get(url + location)
    return r.text

locations = get_locations()
print('\n'.join([f'{i} {location}' for i, location in enumerate(locations)]))
# i = int(input('enter a number: '))
i = int(45)

data_source_1 = get_file(locations[i])


# get local data file
# data_source_1 = 'test1.txt'
# with open(data_source_1, 'r', encoding='utf-8') as data_1_contents:
#     data_1_contents = data_1_contents.read()  # read the contents

date_rain1 = re.findall(r'(\d+-\w+-\d\d\d\d) *(\d+)', data_source_1)




def parse_date(date_str):
    date = datetime.datetime.strptime(date_str, '%d-%b-%Y')
    return (date.year, date.month, date.day)




d = {}
for i in range(len(date_rain1)):
    date_1 = date_rain1[i][0]
    d[parse_date(date_1)] = int(date_rain1[i][1])
    # convert date to datetime
    date = datetime.datetime.strptime(date_1, '%d-%b-%Y')
    daily_total = int(date_rain1[i][1])
    date_rain1[i] = (date, daily_total)
    #date_rain1[i][1] = int(date_rain1[i][1])






rows_1998 = [d[date] for date in d if date[0] == 2018]

print(sum(rows_1998)/len(rows_1998))


# print(date_rain1)

user_input = parse_date('02-MAY-2018')

print(user_input)


# date = datetime.datetime.strptime(date_rain1, '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016



