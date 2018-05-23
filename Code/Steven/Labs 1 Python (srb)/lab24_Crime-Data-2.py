
# n_lines = 100
# with open('../../1 Python/data/Open_Data_Sheet_data.csv', 'r') as f:
#     lines = [next(f) for _ in range(n_lines)]
# print('\n'.join(lines))
#
#
#
# case_number
#
# crime_against
#
from pprint import pprint

from itertools import groupby

def parse_csv(path):
    with open(path, 'r', encoding='utf8') as f:
        data_points = list()
        lines = f.readlines()[:10000]
        keys = [key.casefold().strip().replace(' ', '_').replace('\ufeff', '') for key in lines[0].split(',')]

        for line in lines[1:]:
            values = [value.casefold().strip() for value in line.split(',')]
            data_points.append(dict(zip(keys, values)))

        return data_points


data_points = parse_csv('../../1 Python/data/Open_Data_Sheet_data.csv')


crimes = [data for data in data_points if data['crime_against'] == 'property']
crimes = sorted(crimes, key=lambda c: c['neighborhood'])

print(len(crimes))

crimes_by_neighborhood = dict()
for neighborhood, crimes in groupby(crimes, key=lambda c: c['neighborhood']):
    crimes_by_neighborhood[neighborhood] = list(crimes)

most_crimes = max(crimes_by_neighborhood.items(), key=lambda x: len(x[1]))
print(most_crimes[0], len(most_crimes[1]))