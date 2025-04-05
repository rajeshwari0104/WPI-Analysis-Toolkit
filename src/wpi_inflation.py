##Problem 2: Inflation Rate Calculation Based on WPI
##Objective:
##Compute the month-over-month (MoM) and year-over-year (YoY) inflation rates using WPI data, providing insights into inflationary trends in the wholesale market.
##Implementation Steps:
##Load and Prepare Data – Convert WPI data into time-series format.
##
##Compute MoM Inflation Rate – Percentage change between consecutive months.
##
##Compute YoY Inflation Rate – Percentage change compared to the same month in the previous year.
##
##Visualize Inflation Trends – Line plots and bar charts for better understanding.
##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Identify time-based columns
date_columns = [col for col in df.columns if col.startswith('INDX')]

# Convert data to time-series format
df_melted = df.melt(id_vars=['COMM_NAME'], value_vars=date_columns, var_name="Date", value_name="WPI")
df_melted["Date"] = pd.to_datetime(df_melted["Date"].str[4:], format='%m%Y')  # Extracting month-year

# Handle missing values
df_melted['WPI'] = df_melted['WPI'].ffill()
df_melted.dropna(inplace=True)

# Aggregate WPI by month (overall index)
df_time_series = df_melted.groupby("Date")["WPI"].mean()

# Compute MoM Inflation Rate
df_time_series = df_time_series.to_frame()
df_time_series['MoM Inflation'] = df_time_series['WPI'].pct_change() * 100

# Compute YoY Inflation Rate (compared to the same month of the previous year)
df_time_series['YoY Inflation'] = df_time_series['WPI'].pct_change(periods=12) * 100

# Plot MoM Inflation
plt.figure(figsize=(12, 6))
plt.plot(df_time_series.index, df_time_series['MoM Inflation'], marker='o', linestyle='-', color='blue', label="MoM Inflation")
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.title("Month-over-Month (MoM) Inflation Rate")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.legend()
plt.grid(True)
plt.show()

# Plot YoY Inflation
plt.figure(figsize=(12, 6))
plt.plot(df_time_series.index, df_time_series['YoY Inflation'], marker='o', linestyle='-', color='red', label="YoY Inflation")
plt.axhline(0, color='black', linewidth=1, linestyle='--')
plt.title("Year-over-Year (YoY) Inflation Rate")
plt.xlabel("Year")
plt.ylabel("Inflation Rate (%)")
plt.legend()
plt.grid(True)
plt.show()

# Display summary statistics
print("Summary Statistics:")
print(df_time_series.describe())

##Expected Insights:
##MoM Inflation: Helps identify short-term inflationary trends.
##
##YoY Inflation: Shows longer-term inflation trends over the years.
##
##Key Observations: Find periods of high inflation, deflation, and stability.
##
