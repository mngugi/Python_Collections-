import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
df_cols = df.columns
print(df_cols) 
