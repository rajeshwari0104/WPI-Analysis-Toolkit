import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Filter out only the columns with WPI index data
wpi_columns = [col for col in df.columns if col.startswith('INDX')]
wpi_data = df[["COMM_NAME"] + wpi_columns]

# Melt the dataframe to long format
df_long = wpi_data.melt(id_vars="COMM_NAME", var_name="Month", value_name="WPI")

# Convert 'Month' from 'INDXMMYYYY' to datetime
df_long["Date"] = pd.to_datetime(df_long["Month"].str.replace("INDX", ""), format="%m%Y")

# Drop rows with missing WPI values
df_long.dropna(subset=["WPI"], inplace=True)

# Example: Analyze average WPI trend for a specific commodity (e.g., 'Bajra')
commodity = "Bajra"
commodity_df = df_long[df_long["COMM_NAME"] == commodity].sort_values("Date")

# Plot the WPI time series
plt.figure(figsize=(14, 6))
sns.lineplot(data=commodity_df, x="Date", y="WPI", marker='o')
plt.axvline(pd.to_datetime("2016-07-01"), color='red', linestyle='--', label='GST Introduction')
plt.title(f"WPI Trend for {commodity}")
plt.xlabel("Date")
plt.ylabel("WPI Index")
plt.legend()
plt.tight_layout()
plt.show()

# Rolling statistics
window = 6
commodity_df["RollingMean"] = commodity_df["WPI"].rolling(window=window).mean()
commodity_df["RollingStd"] = commodity_df["WPI"].rolling(window=window).std()

# Plot with rolling mean and std
plt.figure(figsize=(14, 6))
sns.lineplot(data=commodity_df, x="Date", y="WPI", label="WPI", alpha=0.5)
sns.lineplot(data=commodity_df, x="Date", y="RollingMean", label=f"{window}-month Rolling Mean", color="green")
sns.lineplot(data=commodity_df, x="Date", y="RollingStd", label=f"{window}-month Rolling Std", color="orange")
plt.axvline(pd.to_datetime("2016-07-01"), color='red', linestyle='--', label='Policy Event (GST)')
plt.title(f"{commodity} WPI Trend with Rolling Stats")
plt.xlabel("Date")
plt.ylabel("WPI")
plt.legend()
plt.tight_layout()
plt.show()

# Compare pre- and post-policy WPI
event_date = pd.to_datetime("2016-07-01")
pre_event = commodity_df[commodity_df["Date"] < event_date]["WPI"]
post_event = commodity_df[commodity_df["Date"] >= event_date]["WPI"]

print(f"Pre-event average WPI for {commodity}: {pre_event.mean():.2f}")
print(f"Post-event average WPI for {commodity}: {post_event.mean():.2f}")
print(f"Difference: {post_event.mean() - pre_event.mean():.2f}")
