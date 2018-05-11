
import requests
import re

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
print(get_file(locations[i]))



