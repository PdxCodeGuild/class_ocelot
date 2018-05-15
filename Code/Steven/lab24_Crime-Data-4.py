from itertools import groupby

def parse_csv(path):

    # get the data from the file.
    with open(path, 'r', encoding='utf8') as f:
        data_points = list()
        lines = f.readlines()

        # create keys from csv TITLES (row 0)


        # keys = [key.casefold().strip().replace(' ', '_').replace('\ufeff', '') for key in lines[0].split(',')]

        keys = [key.casefold().strip().replace(' ', '_').replace('\ufeff', '') for key in lines[0].split(',')]








        # get values from each record/row/value, starting at row 1.
        for line in lines[1:]:
            values = [value.casefold().strip() for value in line.split(',')]

            data_points.append(dict(zip(keys, values)))

        return keys, data_points


# specify source data csv file.
source_file = '../../1 Python/data/Open_Data_Sheet_data.csv'

keys, data_points = parse_csv(source_file)



print(' '.join([f'{i+1}={keys[i]}' for i in range(len(keys))]))
print(len(keys))

# keys_list = csv_headers()


crimes = [data for data in data_points if data['crime_against'] != '']

crimes = sorted(crimes, key=lambda c: c['offense_type'])

print(len(crimes))
crimes_by_neighborhood = dict()

for neighborhood, crimes in groupby(crimes, key=lambda c: c['offense_type']):
    crimes_by_neighborhood[neighborhood] = list(crimes)

most_crimes = max(crimes_by_neighborhood.items(), key=lambda x: len(x[1]))
print(most_crimes[0], len(most_crimes[1]))