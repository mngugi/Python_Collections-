# python program to perform splicing 
import numpy as np
import pandas as pd

store = "Cartwheeldata.csv"
df = pd.read_csv(store)
i = df.loc[:, "Wingspan"]

print(i)
