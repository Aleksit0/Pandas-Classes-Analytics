import pandas as pd
import numpy as np
# dataframe graphical preview
from pandasgui import show

# generating data
raw_data = np.random.uniform(6, size = (5, 3))
# rounding random integers to 2 decimals
re_data = np.round(raw_data, decimals = 2, out = None)

print('\n')

# making labels
labels = pd.Index(['1', '2', '3', '4', '5'], name = 'Labels')

# making columns
columns = ['Class 1', 'Class 2', 'Class 3']

# making main table (dataframe)
df = pd.DataFrame(re_data, index = labels, columns = columns)
# show(df) - show dataframe in gui
print(df)
