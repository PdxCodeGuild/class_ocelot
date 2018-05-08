



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks = []
valleys = []
"""for x in range(leng(data)):
if x - 1 < 0 or x + 1 > len(data):
    continue
    if -1 index and +1 index == less than than current index:
        peaks.append(current index)
    elif -1 index and +1 index == less than than current index:
        valleys.append(current index)
"""

for x in range(1, len(data)-1):
    if data[x-1] < data[x] and data[x+1] < data[x]:
        peaks.append(x)
    elif data[x-1] > data[x] and data[x+1] > data[x]:
        valleys.append(x)

print(f"{valleys} - Valleys Data")
print(f"{peaks} - Peaks Data")
print(f"{valleys + peaks} - Peaks and Valleys Data")

