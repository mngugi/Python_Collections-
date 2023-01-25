import numpy as np
import pandas as pd

a = '''
This output indicates that we have two types of combinations.

Case 1: Gender = F & Gender Group = 1
Case 2: Gender = M & GenderGroup = 2.
This validates our initial assumption that these two fields 
essentially portray the same information.
'''
print(a)
store = "Cartwheeldata.csv"
df = pd.read_csv(store)

j = df.groupby(['Gender', 'GenderGroup']).size()
print(j)

