import pandas as pd
import numpy as np
# graficki prikaz dataframe-a
from pandasgui import show

# pravimo podatke, unosimo ocjene
raw_data = np.random.uniform(6, size = (5, 3))
# zaokruzujemo random brojeve na 2 decimale
obradjena_data = np.round(raw_data, decimals = 2, out = None)

print('\n')

# pravimo indexe, ucenike
ucenici = ['1', '2', '3', '4', '5']

# pravimo kolone, odjeljenja
odjeljenja = ['Class 1', 'Class 2', 'Class 3']

# pravimo table
df = pd.DataFrame(obradjena_data, index = ucenici, columns = odjeljenja)
# show(df) - graficki prikaz dataframe-a
print(df)
