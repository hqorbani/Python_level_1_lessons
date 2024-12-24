import pandas as pd
file_path = 'data/xls/output.xlsx'

# Sample DataFrame
df = pd.DataFrame({
'Name': ['Omid', 'Hamzeh', 'Ali', 'Mina'],
'Age': [28, 24, 35, 32]
})

# Save DataFrame to Excel
df.to_excel(file_path, index=False)