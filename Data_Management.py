import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
#pd.set_option('display.max_columns', None)

type(df)
df.head()
pd.set_option('display.max_columns', False)
print(df)
