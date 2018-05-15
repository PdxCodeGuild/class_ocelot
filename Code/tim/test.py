

n_lines = 100
with open('../../1 Python/data/Open_Data_Sheet_data.csv', 'r') as f:
    lines = [next(f) for x in range(n_lines)]
print('\n'.join(lines))


