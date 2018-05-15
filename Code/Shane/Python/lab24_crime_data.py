import pandas as pd

# pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
# figsize(15, 5)


path_data = r'../../../1 Python/data/Open_Data_Sheet_data.csv'

data = pd.read_csv('../../../1 Python/data/Open_Data_Sheet_data.csv')

data



# n_lines = 100
# with open('../../../1 Python/data/Open_Data_Sheet_data.csv', 'r') as f:
#     lines = [next(f) for _ in range(n_lines)]
# print('\n'.join(lines))