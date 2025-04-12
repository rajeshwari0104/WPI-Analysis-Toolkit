import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Apply a stylish theme
sns.set_theme(style="whitegrid")

# Load the dataset
file_path = r"C:\Users\user\Downloads\wholesale_price.xlsx"
df = pd.read_excel(file_path)

# Extract relevant WPI columns
wpi_columns = [col for col in df.columns if col.startswith('INDX')]
wpi_data = df[["COMM_NAME"] + wpi_columns]

# Transform wide format to long
df_long = wpi_data.melt(id_vars="COMM_NAME", var_name="Month", value_name="WPI")
df_long["Date"] = pd.to_datetime(df_long["Month"].str.replace("INDX", ""), format="%m%Y")
df_long.dropna(subset=["WPI"], inplace=True)

# Choose a commodity
commodity = "Bajra"
if commodity not in df_long["COMM_NAME"].unique():
    print(f"⚠️ Commodity '{commodity}' not found. Showing a preview of available options:")
    print(df_long["COMM_NAME"].unique())
    commodity = df_long["COMM_NAME"].unique()[0]
    print(f"\n🔁 Defaulting to: {commodity}")

commodity_df = df_long[df_long["COMM_NAME"] == commodity].sort_values("Date")

# --- PLOT 1: Basic WPI Timeline ---
plt.figure(figsize=(14, 6))
sns.lineplot(data=commodity_df, x="Date", y="WPI", marker='o', linewidth=2, color="steelblue")
plt.axvline(pd.to_datetime("2016-07-01"), color='crimson', linestyle='--', linewidth=2, label='GST Introduction')
plt.title(f"📊 WPI Trend for {commodity}", fontsize=16, weight='bold')
plt.xlabel("📅 Date", fontsize=12)
plt.ylabel("📈 WPI Index", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# ---  Rolling Stats ---
window = 6
commodity_df["RollingMean"] = commodity_df["WPI"].rolling(window=window).mean()
commodity_df["RollingStd"] = commodity_df["WPI"].rolling(window=window).std()

# ---  PLOT 2: WPI with Rolling Mean/Std ---
plt.figure(figsize=(14, 6))
sns.lineplot(data=commodity_df, x="Date", y="WPI", label="WPI", alpha=0.5, color="gray")
sns.lineplot(data=commodity_df, x="Date", y="RollingMean", label=f"{window}-Month Rolling Mean", color="seagreen", linewidth=2)
sns.lineplot(data=commodity_df, x="Date", y="RollingStd", label=f"{window}-Month Rolling Std", color="orange", linewidth=2)
plt.axvline(pd.to_datetime("2016-07-01"), color='red', linestyle='--', linewidth=2, label='Policy Event (GST)')
plt.title(f"{commodity} WPI Trend with Rolling Statistics", fontsize=16, weight='bold')
plt.xlabel("Year")
plt.ylabel("WPI Index")
plt.legend()
plt.tight_layout()
plt.show()

# --- Event Comparison ---
event_date = pd.to_datetime("2016-07-01")
pre_event = commodity_df[commodity_df["Date"] < event_date]["WPI"]
post_event = commodity_df[commodity_df["Date"] >= event_date]["WPI"]

# ---  Insights Summary ---
pre_avg = pre_event.mean()
post_avg = post_event.mean()
diff = post_avg - pre_avg

print("**WPI Change Due to Policy Event**")
print(f"Pre-GST Average WPI for {commodity}: {pre_avg:.2f}")
print(f"Post-GST Average WPI for {commodity}: {post_avg:.2f}")
print(f"Difference (Post - Pre): {diff:.2f} {'🔺' if diff > 0 else '🔻'}")
