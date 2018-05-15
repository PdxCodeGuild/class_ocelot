from itertools import groupby

def parse_csv(path):

    # get the data from the file.
    with open(path, 'r', encoding='utf8') as f:
        data_points = list()
        lines = f.readlines()

        # create keys from csv TITLES (row 0)
        keys = []

        for key in lines[0].split(','):
            keys.append(key.casefold().strip().replace(' ', '_').replace('\ufeff', ''))

        # list comprehension of above
        # keys = [key.casefold().strip().replace(' ', '_').replace('\ufeff', '') for key in lines[0].split(',')]

        # get values from each record/row/value, starting at row 1.
        for line in lines[1:]:
            values = [value.casefold().strip() for value in line.split(',')]

            data_points.append(dict(zip(keys, values)))

        return keys, data_points


# specify source data csv file.
source_file = '../../1 Python/data/Open_Data_Sheet_data.csv'

keys, data_points = parse_csv(source_file)



print(' '.join([f'{i+1} = {keys[i]}' for i in range(len(keys))]))

selec_num = input(f'Select field: \n>')
max_or_min = {'max':max, 'min':min}[input(f'Max or min: \n>').lower]
# max_or_min(...)
selection = keys[int(selec_num)-1]

# crimes = [data for data in data_points if data['crime_against'] != '']

crimes = sorted(data_points, key=lambda c: c[selection])

# print(len(crimes))
req_info = dict()

for val_sel, crimes in groupby(crimes, key=lambda c: c[selection]):
    req_info[val_sel] = list(crimes)

val_rtn = max(req_info.items(), key=lambda x: len(x[1]))
print(val_rtn[0], len(val_rtn[1]))