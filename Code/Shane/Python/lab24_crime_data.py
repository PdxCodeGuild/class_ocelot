#
# import itertools
print()
print()
print()
print()

path = '../../../1 Python/data/Open_Data_Sheet_data.csv'

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
            lines = f.readlines()[0:3]
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
    values = []
    n_line = []
    for line in lines[1:]:
        n_line = line.split(',')
        print(n_line)
        print(len(n_line))
        for value in n_line:
            values.append(value.lower().strip())
            #print(values)
            data_points.append(dict(zip(keys, values)))
    #print(data_points)

    #unchanged
    for data in range(len(data_points)):
        return data_points


data_points = parse_csv(path)



