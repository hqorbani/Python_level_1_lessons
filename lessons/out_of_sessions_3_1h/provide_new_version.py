import pandas as pd

# introduce file to edit
df = pd.read_excel('price-history-1400-09-29-to-1403-10-26.xlsx')

# delete first col
df = df.drop(df.columns[0], axis=1)
# select from row 8th
df = df.iloc[7:]

# select 6 cols from the begining
df = df[['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6']]

# rename cols 
df = df.rename(columns={
    'Unnamed: 1':'gregorian_date',
    'Unnamed: 2':'solar_date',
    'Unnamed: 3':'open',
    'Unnamed: 4':'high',
    'Unnamed: 5':'low',
    'Unnamed: 6':'close'
})

# remove rows contain dash character.
df = df.query("open != '-'")
# export new version of excel file
df.to_excel(f"new_price.xlsx", index= False)

