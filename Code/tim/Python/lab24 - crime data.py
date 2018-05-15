
import datetime

data = {}

with open('../Reference Files/Open_Data_Sheet_data.csv', 'r', encoding='utf-8') as f:
    contents = f.read().split('\n')

raw = [r.split(',') for r in contents]

type_dict = {}
year_dict = {}
against_dict = {}

type_index = 8
year_index = 5
against_index = 2

for line in raw:

    if len(line) >= 8 and line != raw[0]:

        if line[type_index] not in type_dict:
            type_dict[line[type_index]] = 1
        else:
            type_dict[line[type_index]] += 1

        t_year = line[year_index][-4:]
        if t_year not in year_dict:
            year_dict[t_year] = 1
        else:
            year_dict[t_year] += 1

        if line[against_index] not in against_dict:
            against_dict[line[against_index]] = 1
        else:
            against_dict[line[against_index]] += 1

print(f'Most frequent crime type is {max(type_dict, key=lambda k: type_dict[k])}')
print(f'Least frequent crime type is {min(type_dict, key=lambda k: type_dict[k])}')
print(f'Most frequent crime year is {max(year_dict, key=lambda k: year_dict[k])}')
print(f'Most frequent crime target is {max(against_dict, key=lambda k: against_dict[k])}')
