
import matplotlib.pyplot as plt

from itertools import groupby

def load_data():
    n_lines = None
    with open('../../1 Python/data/Open_Data_Sheet_data.csv', 'r') as f:
        lines = f.read().split('\n')
        headers = lines[0].casefold().replace('ï»¿', '').replace(' ', '_').split(',')
        headers = [h.strip() for h in headers]
        lines = lines[1:]

    if n_lines is not None:
        lines = lines[:n_lines]
    data = []
    for line in lines:
        if line == '':
            continue
        row = line.split(',')
        row = [v.strip() for v in row]
        d = {}
        for i in range(len(headers)):
            d[headers[i]] = row[i]
        data.append(d)

    return headers, data



def group_data(data, header):
    output = []
    data.sort(key=lambda d: d[header])
    for header_value, crimes in groupby(data, key=lambda d: d[header]):
        output.append((header_value, len(list(crimes))))

        #print(neighborhood, list(crimes)[:10])

    print(output)
    # output.sort(key=lambda t: t[1])

    # print(output)
    # xv = []
    # yv = []
    # for r in output:
    #     xv.append(r[0])
    #     yv.append(r[1])
    # plt.plot(xv, yv)
    # plt.show()

    # for r in output:
    #     print(f'{r[0]} {r[1]}')





    most_dangerous = output[len(output)-10:]
    most_dangerous.reverse()
    least_dangerous = output[:10]




    print('most dangerous:\n\t', end='')
    print('\n\t'.join([' '.join([str(k) for k in v]) for v in most_dangerous]))
    print('least dangerous:\n\t', end='')
    print('\n\t'.join([' '.join([str(k) for k in v]) for v in least_dangerous]))


def most_common_crime_per_hour(data):
    # for each hour, find the most common crime
    data.sort(key=lambda d: d['occur_time'])
    for hour, hourly_crimes in groupby(data, key=lambda d: d['occur_time']):
        hourly_crimes = list(hourly_crimes)
        hourly_crimes.sort(key=lambda d: d['offense_type'])

        #mr = max(groupby(hourly_crimes, key=lambda d: d['offense_type']), key=lambda r: len(list(r[1])))


        hourly_crime_type_counts = []
        for crime_type, hour_crime_type_row in groupby(hourly_crimes, key=lambda d: d['offense_type']):
            hourly_crime_type_counts.append((crime_type, len(list(hour_crime_type_row))))
        hourly_crime_type_counts.sort(key=lambda d: d[1], reverse=True)

        print(hour, ' - '.join(':'.join([str(v2) for v2 in v]) for v in hourly_crime_type_counts[:10]))






headers, data = load_data()


for row in data:
    row['occur_time'] = int(row['occur_time'])//100


most_common_crime_per_hour(data)


#group_data(data, 'occur_time')















