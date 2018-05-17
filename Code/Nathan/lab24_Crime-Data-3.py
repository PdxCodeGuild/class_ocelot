#dont touch actually works

from itertools import groupby


def parse_csv(path):
    with open(path, 'r', encoding='utf8') as f:
        data_points = list()
        lines = f.readlines()
        keys = [key.casefold().strip().replace(' ', '_').replace('\ufeff', '') for key in lines[0].split(',')]

        for line in lines[1:]:
            values = [value.casefold().strip() for value in line.split(',')]
            data_points.append(dict(zip(keys, values)))

        return data_points


data_points = parse_csv('../../1 Python/data/Open_Data_Sheet_data.csv')


crimes = [data for data in data_points if data['crime_against'] == 'property']

#crimes = [data for data in data_points if data['crime_against'] == 'property']

def sort_by_neighborhood(c):
    return c['neighborhood']

crimes = sorted(crimes, key=lambda c: c['neighborhood'])

print(len(crimes))

# print(len(list(groupby(crimes, key=lambda c: c['neighborhood']))))

crimes_by_neighborhood = dict()
for neighborhood, crimes in groupby(crimes, key=lambda c: c['neighborhood']):
    crimes_by_neighborhood[neighborhood] = list(crimes)


#crimes_by_type = dict()
#for offense_type, crimes in groupby(crimes, key=lambda c: c['offense_type']):
#    crimes_by_type['offense_type'] = list(crimes)

# print(crimes_by_neighborhood.items())

# crimes_by_neighborhood = [len(x[1]) for x in crimes_by_neighborhood.items()]
#
# print(crimes_by_neighborhood)

most_crimes = max(crimes_by_neighborhood.items(), key=lambda x: len(x[1]))
print(most_crimes[0], len(most_crimes[1]))
