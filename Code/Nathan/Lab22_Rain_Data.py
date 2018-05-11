
import requests
import re
import datetime
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
i = int(input('enter a number: '))
#print(get_file(locations[i]))
working_data = get_file(locations[i])
#print(working_data)

rain_data = (re.findall(r'(\d+-\w+-\d\d\d\d) *(\d+)',working_data))

#date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')

for i in range(len(rain_data)):
    date = rain_data[i][0]
    #convert date to datetime
    date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
    daily_total = int(rain_data[i][1])

    rain_data[i] = (date,daily_total)
#print(rain_data)
#test of dec 1 2017 and dec 2nd 2017




