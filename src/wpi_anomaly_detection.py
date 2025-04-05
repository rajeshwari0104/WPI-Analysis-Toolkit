import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn theme for better aesthetics
sns.set_theme(style="darkgrid")

# 📂 Load the Dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# 🔎 Identify monthly index columns (those starting with 'INDX')
date_columns = [col for col in df.columns if col.startswith('INDX')]

# 🔄 Melt data: Transform from wide to long format
df_long = df.melt(
    id_vars=['COMM_NAME'],
    value_vars=date_columns,
    var_name="Date",
    value_name="WPI"
)

# 🧹 Clean & Convert Date Format
df_long["Date"] = pd.to_datetime(df_long["Date"].str[4:], format='%m%Y')
df_long["WPI"] = df_long["WPI"].ffill()  # Fill missing values
df_long.dropna(inplace=True)  # Drop any remaining NaNs

# 📈 Average WPI across commodities per month
df_avg_wpi = df_long.groupby("Date")["WPI"].mean()

# ---------------------------------------
# 🔍 Anomaly Detection Techniques
# ---------------------------------------

# 🚨 Z-Score Method
z_scores = (df_avg_wpi - df_avg_wpi.mean()) / df_avg_wpi.std()
z_anomalies = df_avg_wpi[abs(z_scores) > 3]  # threshold = 3

# ⚠️ IQR Method
Q1 = df_avg_wpi.quantile(0.25)
Q3 = df_avg_wpi.quantile(0.75)
IQR = Q3 - Q1
iqr_bounds = (Q1 - 1.5 * IQR, Q3 + 1.5 * IQR)
iqr_anomalies = df_avg_wpi[(df_avg_wpi < iqr_bounds[0]) | (df_avg_wpi > iqr_bounds[1])]

# ---------------------------------------
# 🎨 Visualization
# ---------------------------------------

plt.figure(figsize=(14, 7))
plt.plot(df_avg_wpi.index, df_avg_wpi.values, label="Average WPI", color="#007acc", linewidth=2)

# Mark anomalies
plt.scatter(z_anomalies.index, z_anomalies.values, color="crimson", label="Z-Score Anomalies", s=80, marker="o", edgecolors='k')
plt.scatter(iqr_anomalies.index, iqr_anomalies.values, color="orange", label="IQR Anomalies", s=80, marker="x", linewidths=2)

# 🎯 Plot Settings
plt.title("📊 Wholesale Price Index Anomaly Detection", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("WPI", fontsize=12)
plt.legend()
plt.tight_layout()
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.show()

# ---------------------------------------
# 📋 Print Summary of Detected Anomalies
# ---------------------------------------

def print_anomalies(name, anomalies):
    if anomalies.empty:
        print(f"\n🔹 {name} Method: No anomalies detected.")
    else:
        print(f"\n🔹 {name} Method Detected Anomalies:")
        print(anomalies.to_frame(name="WPI").reset_index().to_string(index=False))

print_anomalies("Z-Score", z_anomalies)
print_anomalies("IQR", iqr_anomalies)
