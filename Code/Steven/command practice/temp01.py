
height = 10
width = 10

for i in range(height):
    print(i)
j = 10


for j in range(height):
    for i in range(width):
        if grid[j][i]:
            print('■', end='')
        else:
            print('□', end='')
    print()