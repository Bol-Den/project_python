import pandas as pd

xlsx = "Asset Allocation.xlsx"
df_excel_file = pd.ExcelFile(xlsx)

# print( df_excel_file.sheet_names)

df_trades = df_excel_file.parse("Trades")
# print(df_trades)

df_summary = df_excel_file.parse("Summary", skiprows=16)
print(df_summary)
