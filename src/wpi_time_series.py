import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import FancyBboxPatch

# Set the visual theme
sns.set(style="whitegrid")

# Load Dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Identify WPI time-based columns
date_columns = [col for col in df.columns if col.startswith('INDX')]

# Melt into long format
df_melted = df.melt(id_vars=['COMM_NAME'], value_vars=date_columns,
                    var_name="Date", value_name="WPI")

# Extract datetime
df_melted["Date"] = pd.to_datetime(df_melted["Date"].str[4:], format='%m%Y')

# Clean missing data
df_melted['WPI'] = df_melted['WPI'].ffill()
df_melted.dropna(inplace=True)

# Monthly average WPI across commodities
df_time_series = df_melted.groupby("Date")["WPI"].mean()

# Create a creative plot
plt.figure(figsize=(14, 7))
plt.plot(df_time_series.index, df_time_series, marker='o', linestyle='-', color='midnightblue', label='Monthly Avg WPI')

# Annotate policy event (example: GST)
policy_date = pd.to_datetime("2016-07-01")
plt.axvline(policy_date, color='crimson', linestyle='--', linewidth=1.5, label='🔺 GST Introduced')

# Add annotation
plt.text(policy_date, df_time_series.max()*0.98, 'GST (Jul 2016)', rotation=90,
         verticalalignment='top', fontsize=10, color='crimson')

# Dynamic insights
mean_val = df_time_series.mean()
latest_date = df_time_series.index[-1].strftime('%b %Y')
latest_val = df_time_series.iloc[-1]

# Info box
props = dict(boxstyle="round,pad=0.4", facecolor="lavender", edgecolor="gray", alpha=0.6)
info_text = f"📅 Latest: {latest_date}\n📈 Latest WPI: {latest_val:.2f}\n📊 Mean WPI: {mean_val:.2f}"
plt.gca().text(0.75, 0.15, info_text, transform=plt.gca().transAxes, fontsize=11, bbox=props)

# Titles and labels
plt.title("📈 National WPI Trend Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Year")
plt.ylabel("Wholesale Price Index (WPI)")
plt.legend()
plt.tight_layout()
plt.show()
