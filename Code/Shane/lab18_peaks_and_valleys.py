

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

peaks = []
valleys = []
"""
for x in range(leng(data)):
if x - 1 < 0 or x + 1 > len(data):
    continue
    if -1 index and +1 index == less than than current index:
        peaks.append(current index)
    elif -1 index and +1 index == less than than current index:
        valleys.append(current index)
"""


def find_P_and_V(lst):
    for x in range(1, len(data)-1):
        if data[x-1] < data[x] and data[x+1] < data[x]:
            peaks.append(x)
        elif data[x-1] > data[x] and data[x+1] > data[x]:
            valleys.append(x)
    return f"{valleys} - Valleys Data\n{peaks} - Peaks Data\n{valleys + peaks} - Peaks and Valleys Data"

print(find_P_and_V(data))



"""
from 7 working your way down to 1
for max value in (list) #determins the height of the printout

if value = max print x else print " "\\n

"""

for i in range(max(data), 0, -1):
    for x in range(len(data)):
        if data[x] >= i:
            print("X", end='')
        else:
            print(" ", end='')
    print()



