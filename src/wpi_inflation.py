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

# 🌈 Set a beautiful theme
sns.set_theme(style="whitegrid")

# 📂 Load Dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# 🔍 Identify Time Columns
date_columns = [col for col in df.columns if col.startswith('INDX')]

# 🔄 Transform to Long Format
df_long = df.melt(
    id_vars=['COMM_NAME'],
    value_vars=date_columns,
    var_name="Date",
    value_name="WPI"
)

# 🧼 Clean Dates
df_long["Date"] = pd.to_datetime(df_long["Date"].str[4:], format='%m%Y')

# 🛠 Handle Missing Values
df_long['WPI'] = df_long['WPI'].ffill()
df_long.dropna(inplace=True)

# 📊 Average WPI per Month
df_ts = df_long.groupby("Date")["WPI"].mean().to_frame()

# 📈 Inflation Calculations
df_ts["MoM Inflation (%)"] = df_ts["WPI"].pct_change() * 100
df_ts["YoY Inflation (%)"] = df_ts["WPI"].pct_change(periods=12) * 100

# ------------------------------------------------------
# 📈 Plot: Month-over-Month Inflation
# ------------------------------------------------------
plt.figure(figsize=(14, 6))
plt.plot(df_ts.index, df_ts["MoM Inflation (%)"], marker='o', color="#1f77b4", label="MoM Inflation")
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.title("📅 Month-over-Month (MoM) Inflation Rate", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Inflation Rate (%)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# 📈 Plot: Year-over-Year Inflation
# ------------------------------------------------------
plt.figure(figsize=(14, 6))
plt.plot(df_ts.index, df_ts["YoY Inflation (%)"], marker='s', color="#d62728", label="YoY Inflation")
plt.axhline(0, color='gray', linestyle='--', linewidth=1)
plt.title("📆 Year-over-Year (YoY) Inflation Rate", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Inflation Rate (%)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# 📋 Summary Statistics Table
# ------------------------------------------------------
print("\n📊 Summary Statistics for WPI and Inflation Rates:\n")
try:
    styled_table = df_ts.describe().round(2).style.set_caption("🧮 Descriptive Statistics")\
        .set_table_styles([{
            'selector': 'caption',
            'props': [('font-size', '16px'), ('text-align', 'left'), ('color', 'black')]
        }])\
        .background_gradient(cmap='YlGnBu', axis=1)

    from IPython.display import display
    display(styled_table)

except ImportError:
    print("\n🧮 Descriptive Statistics (Basic Output):\n")
    print(df_ts.describe().round(2))




##Expected Insights:
##MoM Inflation: Helps identify short-term inflationary trends.
##
##YoY Inflation: Shows longer-term inflation trends over the years.
##
##Key Observations: Find periods of high inflation, deflation, and stability.
##
