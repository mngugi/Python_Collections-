# Import the pandas library with the alias 'pd'
import pandas as pd

# Create a dictionary 'zoneTemperatures' containing data
zoneTemperatures = {
    'Zones': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Temperature': [35, 40, 24, 28, 18, 22, 24, 50, 36, 32],
    'Altitude': [1200, 1522, 500, 2300, 2571, 1888, 9666, 1254, 16000, 2000]
}

# Create a DataFrame 'df' from the 'zoneTemperatures' dictionary
df = pd.DataFrame(data=zoneTemperatures)

# Print the DataFrame 'df' to the console
print(df)

# Calculate and print the number of rows in the DataFrame
countRows = df.shape[0]
print("Number of Rows:", countRows)

# Calculate and print the number of columns in the DataFrame
countCols = df.shape[1]
print("Number of Columns:", countCols)

# Find and print the maximum temperature from the 'Temperature' column
maxTemperature = df['Temperature'].max()
print("Maximum Temperature:", maxTemperature)

# Find and print the minimum temperature from the 'Temperature' column
minTemperature = df['Temperature'].min()
print('Minimum Temperature:', minTemperature)

# Calculate and print the average temperature from the 'Temperature' column
averageTemperature = df['Temperature'].mean()
print("Mean Temperature:", averageTemperature)
