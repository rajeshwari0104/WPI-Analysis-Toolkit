import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Load Dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Identify time-based columns (those starting with 'INDX')
date_columns = [col for col in df.columns if col.startswith('INDX')]

# Filter for Primary Articles (Assuming 'COMM_NAME' contains category names)
primary_articles = df[df['COMM_NAME'].str.contains("Primary", case=False, na=False)]

# Reshape the dataset (Melt to convert time columns into rows)
df_melted = primary_articles.melt(id_vars=['COMM_NAME'], value_vars=date_columns, var_name="Date", value_name="WPI")

# Extract Date from column names (remove 'INDX' prefix)
df_melted["Date"] = pd.to_datetime(df_melted["Date"].str[4:], format='%m%Y')

# Handle missing values
df_melted['WPI'] = df_melted['WPI'].ffill()
df_melted.dropna(inplace=True)

# Aggregate WPI by month (overall index for Primary Articles)
df_time_series = df_melted.groupby("Date")["WPI"].mean()

# Seasonal Decomposition
decomposition = seasonal_decompose(df_time_series, model="additive", period=12)

# Plot Decomposition
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df_time_series, label="Original Time Series", color='blue')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposition.trend, label="Trend", color='green')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposition.seasonal, label="Seasonality", color='red')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposition.resid, label="Residuals", color='black')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
