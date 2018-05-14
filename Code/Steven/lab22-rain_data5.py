








data = []
with open('rain_output.csv', 'r') as f:
    contents = f.read()
    lines = contents.split('\n')
    lines.pop(0) # remove header
    for line in lines:
        if line == '':
            continue
        line = line.split(',')
        data.append([float(v) if v != '' else -1 for v in line])


