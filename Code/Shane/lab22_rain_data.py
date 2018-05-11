import datetime
import re
import requests
import matplotlib.pyplot as plt

r = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

contents = r.text
# print(contents)


# with open('rain_data.txt', 'r') as f:
#     contents = f.read()

dates_and_total = re.findall('(\d{2}-\w{3}-\d{4}) +(\d+)', contents)

# print(dates_and_total)
# date = datetime.datetime.strptime(dates_and_total[0][0], '%d-%b-%Y')
# print(date)
# print(date.year)

for x in range(len(dates_and_total)):
    date = dates_and_total[x][0]
    date = datetime.datetime.strptime(date, '%d-%b-%Y')
    # if dates_and_total[x][1].isdigit():
    daily_total = int(dates_and_total[x][1])
    dates_and_total[x] = (date, daily_total)

# print(dates_and_total)
#
# for row in dates_and_total:
#     if row[0].month == "APR":
#         row
mlist =[]

y_m_d = input('see data for a year, month or day?\n').lower()
input_date = int(input(f'whats the number of the {y_m_d} you want to see?\n'))

if y_m_d == "year":
    [mlist.append(row[1]) for row in dates_and_total if row[0].year == input_date]
elif y_m_d == "month":
    [mlist.append(row[1]) for row in dates_and_total if row[0].month == input_date]
elif y_m_d == "day":
    [mlist.append(row[1]) for row in dates_and_total if row[0].day == input_date]


#rows_1998 = [row for row in dates_and_total if row[0].day == 1]

# print(mlist)

# average = sum([r[1] for r in ymd_data]) / len(ymd_data)
# print(average)




plt.plot(mlist)
plt.ylabel('amount')
plt.show()
