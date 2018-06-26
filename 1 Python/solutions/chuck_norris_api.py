


import requests

import json


for i in range(1000):

    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = json.loads(response.text)
    print('NOT FUNNNYNYNYNY', data['value'])






