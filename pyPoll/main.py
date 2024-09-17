import pandas as pd
import numpy as np

data = ("resources/election_data.csv")
#convert to dataframe
df = pd.read_csv(data)

ballots_total = len(df)
print(f"Ballots:",ballots_total)

info = (df['Candidate'].value_counts()/df['Candidate'].count())*100
df.loc['Canidate'] = df.sum()
print(info)
