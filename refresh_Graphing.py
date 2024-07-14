import seaborn as sns

import matplotlib.pyplot as plt

import pandas as pd


dt = {

    'x_axis': [12, 15, 36, 65, 49, 60],
    'y_axis': [15, 19, 40, 60, 41, 59]



    }

dt = pd.Dataframe(data)

sns.lineplot( X = 'x-axis', Y = 'y-axis', data = dt, marker='0')

plt.title('Line using Line Graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True)
plt.show()

