

source_data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_data = []
valley_data = []


for i in range(20):
    data_current = source_data[i]
    data_left = source_data[i - 1]
    data_right = source_data[i + 1]

    if data_current - 1 < 0:
        data_current = 0
    elif data_current + 1 > 20:
        data_current = 20

    if data_left < data_current and data_right < data_current:
        peak_data.append(i)

    elif data_left > data_current and data_right > data_current:
        valley_data.append(i)

print(f'Peaks: ' {peak_data}')
print(f'Valleys: ' {valley_data}')

# print(peak_data)
# print(valley_data)

