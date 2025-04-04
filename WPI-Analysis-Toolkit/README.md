# WPI-Analysis-Toolkit
A Python-based analytical toolbox for studying Wholesale Price Index (WPI) trends in India.

## Table of Contents  
- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Data Sources](#data-sources)  
- [License](#license)  
- [Contributors](#contributors)  
- [Acknowledgments](#acknowledgments)  


**Overview**

The Wholesale Price Index (WPI) serves as a key economic indicator, tracking price movements in India's wholesale markets. This Python toolbox provides a comprehensive suite of analytical tools for examining WPI trends, computing inflation rates, comparing major commodity groups, and employing machine learning models for forecasting.

**Features**

The toolbox includes the following analytical modules: 
1.Time Series Analysis of WPI Trends Analyzes monthly WPI data from 2011-12 onward. Identifies long-term trends, seasonal patterns, and cyclical behaviors.

2.Inflation Rate Calculation Based on WPI Computes month-over-month and year-over-year inflation rates. Provides insights into inflationary trends in wholesale markets.

3.Seasonal Variation Analysis in Primary Articles Examines seasonal variations in the WPI of agricultural and other primary articles. Identifies periods of price volatility and potential causes.

4.Assessing the Impact of Policy Changes on WPI Analyzes structural breaks or shifts in WPI due to major economic policies or events. Evaluates the impact of tax reforms, subsidies, and other policy changes.

5.Identifying Anomalies in WPI Data Implements anomaly detection algorithms to identify unusual spikes or drops in WPI. Helps in detecting data inconsistencies or significant economic events.

**Installation**

To use this toolbox, clone the repository and install the required dependencies: 
git clone https://github.com/rajeshwari0104/wpi-analysis-toolkit.git 
cd wpi-analysis-toolkit 
pip install -r requirements.txt

**Usage**

Each module can be executed separately or combined for comprehensive analysis. 
Example usage: from wpi_toolbox import wpi_trend_analysis wpi_trend_analysis.analyze_trends(r"C:\Users\user\Downloads\wholesale_price.xlsx")

**Data Sources**

The toolbox is designed to work with publicly available WPI datasets from government and economic research sources.

**License**  
![License](https://img.shields.io/badge/license-MIT-blue)  

This project is licensed under the MIT License.

**Contributors**
![GitHub Repo Stars](https://img.shields.io/github/stars/rajeshwari0104/wpi-analysis-toolkit?style=social)
Rajeshwari Thapa (thaparajeshwari0104@gmail.com)

**Acknowledgments**

Special thanks to economic research institutions and open data sources for providing WPI datasets.
 
