import pandas as pd

airLineData = pd.read_csv("Airline Dataset.csv", header=0, sep=",")

print(airLineData.head())
print("Airline Data Information:", airLineData.info())
print(airLineData.describe())
