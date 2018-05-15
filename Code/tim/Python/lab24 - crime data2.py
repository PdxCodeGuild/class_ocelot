
with open('../Reference Files/Open_Data_Sheet_data.csv', 'r', encoding='utf-8') as f:
    contents = f.read().split('\n')

raw = [r.split(',') for r in contents]

type_dict = {}
year_dict = {}
targ_dict = {}
neib_dict = {}

type_index = 8
year_index = 5
targ_index = 2
neib_index = 4

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

        if line[targ_index] not in targ_dict:
            targ_dict[line[targ_index]] = 1
        else:
            targ_dict[line[targ_index]] += 1

        if line[neib_index] not in neib_dict:
            neib_dict[line[neib_index]] = 1
        else:
            neib_dict[line[neib_index]] += 1

sort_type = sorted(type_dict.items(), key=lambda k: k[1])
sort_year = sorted(year_dict.items(), key=lambda k: k[1])
sort_targ = sorted(targ_dict.items(), key=lambda k: k[1])
sort_neib = sorted(neib_dict.items(), key=lambda k: k[1])
print_str = ['', '', '', '']  # [type, year, targ, neib]

for i in range(1, 11):
    if len(sort_type) >= i:
        pad = 30 - len(sort_type[-i][0])
        print_str[0] += '\t' + sort_type[-i][0] + pad * ' ' + str(sort_type[-i][1]) + '\n'
    if len(sort_year) >= i:
        pad = 30 - len(sort_year[-i][0])
        print_str[1] += '\t' + sort_year[-i][0] + pad * ' ' + str(sort_year[-i][1]) + '\n'
    if len(sort_targ) >= i:
        pad = 30 - len(sort_targ[-i][0])
        print_str[2] += '\t' + sort_targ[-i][0] + pad * ' ' + str(sort_targ[-i][1]) + '\n'
    if len(sort_neib) >= i:
        pad = 30 - len(sort_neib[-i][0])
        print_str[3] += '\t' + sort_neib[-i][0] + pad * ' ' + str(sort_neib[-i][1]) + '\n'

print(f'TOP 10 CRIMES BY TYPE\n{print_str[0]}')
print(f'TOP 10 CRIMIEST YEARS\n{print_str[1]}')
print(f'TOP 10 TARGETS OF CRIME\n{print_str[2]}')
print(f'TOP 10 CRIMIEST NEIGHBORHOODS\n{print_str[3]}')
