import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Set plot style
sns.set_theme(style="whitegrid")

# Load the dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Identify date-based WPI columns
date_columns = [col for col in df.columns if col.startswith('INDX')]

# Filter for Primary Articles
primary_articles = df[df['COMM_NAME'].str.contains("Primary", case=False, na=False)]

# Handle no matches creatively
if primary_articles.empty:
    print("⚠️ No 'Primary' articles found! Defaulting to first 5 commodities.")
    primary_articles = df.head(5)

# Melt to long format
df_melted = primary_articles.melt(
    id_vars=['COMM_NAME'],
    value_vars=date_columns,
    var_name="Date",
    value_name="WPI"
)

# Extract proper datetime from 'INDXMMYYYY'
df_melted["Date"] = pd.to_datetime(df_melted["Date"].str[4:], format='%m%Y')

# Forward fill and drop missing
df_melted['WPI'] = df_melted['WPI'].ffill()
df_melted.dropna(inplace=True)

# Average WPI per month across primary articles
df_time_series = df_melted.groupby("Date")["WPI"].mean()

# Decompose time series
decomposition = seasonal_decompose(df_time_series, model="additive", period=12)

# 🎨 Enhanced Plot
fig, axes = plt.subplots(4, 1, figsize=(14, 10), sharex=True)
fig.suptitle("📊 Seasonal Decomposition of WPI – Primary Articles", fontsize=16, weight='bold')

axes[0].plot(df_time_series, label="Original", color='royalblue')
axes[0].legend(loc="upper left")
axes[0].set_ylabel("WPI")

axes[1].plot(decomposition.trend, label="Trend", color='seagreen')
axes[1].legend(loc="upper left")
axes[1].set_ylabel("Trend")

axes[2].plot(decomposition.seasonal, label="Seasonality", color='tomato')
axes[2].legend(loc="upper left")
axes[2].set_ylabel("Seasonality")

axes[3].plot(decomposition.resid, label="Residual", color='gray')
axes[3].legend(loc="upper left")
axes[3].set_ylabel("Residual")

plt.xlabel("Date")
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()

# 🧠 Optional: Summary Stats
print("\n📌 WPI Decomposition Summary:")
print(f"🕰️ Time Range: {df_time_series.index.min().date()} to {df_time_series.index.max().date()}")
print(f"📉 Mean WPI: {df_time_series.mean():.2f}")
print(f"📈 Max WPI: {df_time_series.max():.2f}")
print(f"📉 Min WPI: {df_time_series.min():.2f}")
