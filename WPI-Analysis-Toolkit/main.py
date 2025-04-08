import os

scripts = [
    "wpi_time_series.py", "wpi_inflation.py", "wpi_seasonal_analysis.py", 
    "wpi_policy_impact.py","wpi_anomaly_detection.py"
]

for script in scripts:
    print(f"\nRunning {script}...")
    os.system(f"python src/{script}")
