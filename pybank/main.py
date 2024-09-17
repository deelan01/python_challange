import pandas as pd
import numpy as np

#imported data
data = ("resources/budget_data.csv")

#convert to dataframe
df = pd.read_csv(data)

#print length of dates
dates_length = len(df.Date)
print(f"dates:", dates_length)

#print sum of profits
changes = df.sum()
print(f"added total:", changes)

#convert to nummeric and find average
df['Profit/Losses'] = pd.to_numeric(df['Profit/Losses'])
average = df['Profit/Losses'].diff()
print(f"rounded difference:", {round(average.mean(),2)})

#print max of data column rounded
print(f"maximum:",{round(average.max(),0)})

#print min of data column rounded
print(f"miniumum:",{round(average.min(),0)})