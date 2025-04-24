# WPI-Analysis-Toolkit

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)

A Python-based analytical toolbox for studying Wholesale Price Index (WPI) trends in India.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Contributors](#contributors)
- [Acknowledgments](#acknowledgments)

---

## 📊 Overview

The Wholesale Price Index (WPI) is a key economic indicator in India. This Python toolkit helps analyze WPI trends, calculate inflation rates, compare commodity groups, and forecast using machine learning models.

---

## ✨ Features

- 📈 **Time Series Analysis**  
  Analyze monthly WPI data to identify trends, seasonality, and cycles.

- 🔢 **Inflation Rate Calculation**  
  Calculate MoM and YoY inflation from WPI data.

- 🌾 **Seasonal Variation in Primary Articles**  
  Understand seasonal patterns in agricultural and other primary goods.

- 🧾 **Policy Impact Analysis**  
  Detect structural breaks due to GST, subsidies, etc.

- ⚠️ **Anomaly Detection**  
  Spot data inconsistencies or major economic events using algorithms.

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/rajeshwari0104/wpi-analysis-toolkit.git

# Move into the folder
cd wpi-analysis-toolkit

# Install dependencies
pip install -r requirements.txt
```
---

## 🗂️ Data Sources

The data used in this toolkit is sourced from:

- [Office of the Economic Adviser, Ministry of Commerce & Industry, India](https://eaindustry.nic.in/)
- Public datasets and open government APIs

Please check the `data/README.md` file for data formatting and update guidelines.

---

## 👩‍💻 Contributors

- [Rajeshwari](https://github.com/rajeshwari0104) — Project Maintainer

Contributions are welcome! Feel free to fork the repository, raise issues, or open pull requests.

---

## 🙏 Acknowledgments

Special thanks to:

- Government of India for making WPI data publicly available.
- Contributors to open-source Python libraries like `pandas`, `matplotlib`, `seaborn`,`numpy` etc.
- Researchers and analysts whose work inspired this toolkit.