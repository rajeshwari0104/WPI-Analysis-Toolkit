import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Identify time-based columns (those starting with 'INDX')
date_columns = [col for col in df.columns if col.startswith('INDX')]

# Reshape dataset (Melt time columns into rows)
df_melted = df.melt(id_vars=['COMM_NAME'], value_vars=date_columns, var_name="Date", value_name="WPI")

# Extract Date from column names (remove 'INDX' prefix)
df_melted["Date"] = pd.to_datetime(df_melted["Date"].str[4:], format='%m%Y')

# Handle missing values
df_melted['WPI'] = df_melted['WPI'].ffill()
df_melted.dropna(inplace=True)

# Aggregate WPI data by Date (average across commodities)
df_time_series = df_melted.groupby("Date")["WPI"].mean()

# -------------- Anomaly Detection Methods --------------

# --- 1. Z-Score Method ---
z_scores = (df_time_series - df_time_series.mean()) / df_time_series.std()
z_threshold = 3  # Common threshold for anomalies
z_anomalies = df_time_series[abs(z_scores) > z_threshold]

# --- 2. Interquartile Range (IQR) Method ---
Q1 = df_time_series.quantile(0.25)
Q3 = df_time_series.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
iqr_anomalies = df_time_series[(df_time_series < lower_bound) | (df_time_series > upper_bound)]

# -------------- Visualization --------------
plt.figure(figsize=(12,6))
plt.plot(df_time_series, label="WPI", color="blue")
plt.scatter(z_anomalies.index, z_anomalies, color="red", label="Z-Score Anomalies", marker="o")
plt.scatter(iqr_anomalies.index, iqr_anomalies, color="orange", label="IQR Anomalies", marker="x")
plt.xlabel("Date")
plt.ylabel("WPI")
plt.title("WPI Anomaly Detection")
plt.legend()
plt.show()

# Print detected anomalies
print("\n🔹 Z-Score Detected Anomalies:")
print(z_anomalies)
print("\n🔹 IQR Detected Anomalies:")
print(iqr_anomalies)
