

import requests

# r = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')


with open('rain_data.txt', 'r') as f:
    contents = f.read()

print(contents)







