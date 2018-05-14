import datetime
import matplotlib.pyplot as plt


# parse the given file's rain data
# http://or.water.usgs.gov/non-usgs/bes/
def parse_file(file_path):
    starting_line = 12
    n_cols = 26
    data = []
    name = ''
    address = ''
    with open(file_path, 'r') as file:
        header = file.readline().strip().split('-')
        name = header[0].strip()
        address = header[1].strip()

        # skip over the first few lines that contain metadata
        for _ in range(starting_line-2):
            next(file)
        for line in file:
            if line == '':  # skip over blank lines
                continue
            data_str = line.split()
            data_line = [None]*n_cols
            for i in range(len(data_str)):
                if i == 0:
                    data_line[i] = datetime.datetime.strptime(data_str[i], '%d-%b-%Y')  # convert the string to a datetime
                elif data_str[i] == '-':  # if the data is missing, let it remain as 'None'
                    continue
                else:
                    data_line[i] = int(data_str[i])*0.01*2.54  # convert to inches, then to cm
            data.append(data_line)
    return name, address, data


def find_mean_and_variance(data):
    total = 0
    count = 0
    for i in range(len(data)):
        if data[i][1] is not None:
            total += data[i][1]
            count += 1

    mean = total / count

    variance_total = 0
    for i in range(len(data)):
        if data[i][1] is not None:
            diff = data[i][1] - mean
            variance_total += diff*diff
    variance = variance_total / count

    return mean, variance


# returns the date of the raniest day
def find_rainiest_day(data):
    max_index = 0
    for i in range(len(data)):
        if data[i][1] is not None and data[i][1] > data[max_index][1]:
            max_index = i
    return data[max_index][0]


def find_rainiest_year(data):

    # build a list of all the years, use 'set' to make them unique
    years = list(set([data_line[0].year for data_line in data]))
    years.sort()
    totals = [0] * len(years)
    counts = [0] * len(years)

    for data_line in data:
        year_index = years.index(data_line[0].year)
        if data_line[1] is not None:
            totals[year_index] += data_line[1]
            counts[year_index] += 1

    average_values = [totals[i]/counts[i] for i in range(len(years))]

    plt.plot(years, average_values)
    plt.show()

    max_index = average_values.index(max(average_values))
    return years[max_index]


def graph_months(data):
    months = list(range(1, 13))
    totals = [0]*len(months)
    counts = [0]*len(months)
    for i in range(len(data)):
        if data[i][1] is None:
            continue
        index = months.index(data[i][0].month)
        totals[index] += data[i][1]
        counts[index] += 1
    averages = []
    for i in range(len(months)):
        averages.append(totals[i]/counts[i])
    plt.plot(months, averages)
    plt.show()


def graph_days(data):
    days = list(range(1, 367))
    totals = [0]*len(days)
    counts = [0]*len(days)
    for i in range(len(data)):
        if data[i][1] is None:
            continue
        index = days.index(data[i][0].timetuple().tm_yday)
        totals[index] += data[i][1]
        counts[index] += 1
    averages = []
    for i in range(len(days)):
        averages.append(totals[i]/counts[i])
    plt.plot(days, averages)
    plt.show()


def graph_year(data):
    x_values = []
    y_values = []
    for i in range(len(data)):
        if data[i][1] is not None:
            x_values.append(data[i][0])
            y_values.append(data[i][1])
    plt.plot(x_values, y_values)
    plt.show()


def find_longest_continuous_rain(data):
    longest_stretch = 0
    current_stretch = 0
    end_index = 0
    for i in range(len(data)):
        if data[i][1] is None or data[i][1] == 0: # change to != 0 to get the longest dry period
            if current_stretch > longest_stretch:
                longest_stretch = current_stretch
                end_index = i
            current_stretch = 0
        else:
            current_stretch += 1
    print(longest_stretch)
    print(data[end_index][0])
    print(data[end_index][0] - datetime.timedelta(days=longest_stretch))


def main():
    name, address, data = parse_file('sunnyside.rain.txt')
    print(data)
    mean, variance = find_mean_and_variance(data)
    rainiest_day = find_rainiest_day(data)
    rainiest_year = find_rainiest_year(data)

    print('mean: ' + str(mean) + ' cm')
    print('variance: ' + str(variance) + ' cm^2')
    print('rainiest day: ' + str(rainiest_day))
    print('rainiest year: ' + str(rainiest_year))

    graph_days(data)
    #graph_year(data)
    find_longest_continuous_rain(data)


main()