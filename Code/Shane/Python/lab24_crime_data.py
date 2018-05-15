#
# import itertools
print()
print()
print()
print()

path = '/Users/shane/Desktop/PDX_Code/full_stack/class_ocelot/1 Python/data/Open_Data_Sheet_data.csv'

# f = open(path)
# data_points = list()
#
# if path.endswith('.csv'):
#     lines = f.readlines()[:5]
#     print(lines)
#
# print(f)

def parse_csv(path):
    if path.endswith('.csv'):
        with open(path) as f:
            lines = f.readlines()[:100]
    # print(lines)
    print()

    #creating keys for the dict
    # keys = [key.casefold().strip().replace(' ', '_').replace('\ufeff', '') for key in lines[0].split(',')]
    keys =[]
    for key in lines[0].split(','):
        keys.append(key.lower().strip().replace('\ufeff', '').replace(' ', '_'))
    #print(keys)

    # for line in lines[1:]:
    #     values = [value.casefold().strip() for value in line.split(',')]
    #     data_points.append(dict(zip(keys, values)))
    data_points = list()
    for line in lines[1:]:
        values = []
        for value in line.split(','):
            values.append(value.lower().strip())
            #print(values) #testing the list build-up
        data_points.append(dict(zip(keys, values)))
    #print(data_points)

    #unchanged
    for data in range(len(data_points)):
        return data_points


data_points = parse_csv(path)

#didn't change this one because it looks like a normal list comp.

#added this while loop

crime_against = input('property, society or person').lower()

crimes = [data for data in data_points if data['crime_against'] == crime_against]
#print(crimes)
print(f'{len(crimes)} crimes against {crime_against} in the past 2 years\n')

# crimes = sorted(crimes, key=lambda c: c['neighborhood'])....
##### Is this right?
# def sortting(c):
#     return c['neighborhood']



# crimes_by_neighborhood = dict()
# for neighborhood, crimes in groupby(crimes, key=lambda c: c['neighborhood']):
#     crimes_by_neighborhood[neighborhood] = list(crimes)
#
# most_crimes = max(crimes_by_neighborhood.items(), key=lambda x: len(x[1]))
# print(most_crimes[0], len(most_crimes[1]))

crimes_by_neighborhood = {}

#(crime_against\nneighborohood\noccur_time\noffense_type\n)
