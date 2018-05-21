# Peaks and Valleys

# peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
#
# valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
#
# peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

data_input = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]



def pv(data_input):
    peak_data = []
    valley_data = []


    for i in range(1, len(data_input)-1):
        data_current = data_input[i]
        data_right = data_input[i + 1]
        data_left = data_input[i - 1]
        if data_right < data_input[i] and data_left < data_input[i]:
            peak_data.append(i)

        if data_right > data_input[i] and data_left > data_input[i]:
            valley_data.append(i)
    return peak_data, valley_data

peak_data, valley_data = pv(data_input)

print(peak_data)
print(valley_data)

# for i in range(len(data_input)):
#     print('X' * data_input[i])

max_value = max(data_input)

for i in range(max_value, 0, -1):
    for x in range(len(data_input)):
        if data_input[x] >= i:
            print('X', end='')
        else:
            print(' ', end='')
    print()
