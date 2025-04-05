import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Identify time-based columns (those starting with 'INDX')
date_columns = [col for col in df.columns if col.startswith('INDX')]

# Melt the dataset to convert time-based columns into rows
df_melted = df.melt(id_vars=['COMM_NAME'], value_vars=date_columns, var_name="Date", value_name="WPI")

# Extract Date from column names (remove 'INDX' prefix)
df_melted["Date"] = pd.to_datetime(df_melted["Date"].str[4:], format='%m%Y')

# Handle missing values
df_melted['WPI'] = df_melted['WPI'].ffill()
df_melted.dropna(inplace=True)

# Aggregate WPI by month (overall index)
df_time_series = df_melted.groupby("Date")["WPI"].mean()

# Plot the WPI trend
plt.figure(figsize=(12, 6))
plt.plot(df_time_series.index, df_time_series, marker='o', linestyle='-', color='blue')
plt.xlabel("Year")
plt.ylabel("Wholesale Price Index (WPI)")
plt.title("WPI Time Series Analysis")
plt.grid(True)
plt.show()
