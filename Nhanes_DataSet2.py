import numpy as np
import pandas as pd

store = "nhanes_2015_2016.csv"
df = pd.read_csv(store)

i = df.shape
j = df.columns
k = df.dtypes

print(i,"\n")
print(j,"\n")
print(k,"\n")


