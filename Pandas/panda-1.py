import pandas as pd
# Give Index
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])


# Data Frame
df = pd.DataFrame({"name": ["Soban Amjad", "Ahmad Anwar", "Ali"], "marks": [ 98, 56, 78 ]})
print(df)

# Read CSV
df = pd.read_csv("csv/customers-100.csv")
print(df)

df.head()