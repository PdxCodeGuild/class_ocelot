1


data = []
with open('../../1 Python/data/Open_Data_Sheet_data.csv', 'r') as f:
    contents = f.read()
    lines = contents.split('\n')
    lines.pop(0) # remove header
    # for line in lines:
    for line in range(100):
        if line == '':
            continue
        line = line.split(',')
        data.append([float(v) if v != '' else -1 for v in line])

print(data)