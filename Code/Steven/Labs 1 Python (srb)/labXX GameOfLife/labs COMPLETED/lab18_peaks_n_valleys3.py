

def peaks_and_valleys(data):
    peak_data = []
    valley_data = []

    for i in range(1, len(data) - 1):
        data_current = data[i]
        data_left = data[i - 1]
        data_right = data[i + 1]

        if data_left < data_current and data_right < data_current:
            peak_data.append(i)

        if data_left > data_current and data_right > data_current:
            valley_data.append(i)

    return peak_data, valley_data

# print(f'Peaks: ' {peak_data}')
# print(f'Valleys: ' {valley_data}')

source_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peak_data, valley_data = peaks_and_valleys(source_data)

print(peak_data)
print(valley_data)

for i in range(len(source_data)):
    for j in range(source_data[i]):
        print('X', end='')
    print()
    #print('X' * source_data[i])





