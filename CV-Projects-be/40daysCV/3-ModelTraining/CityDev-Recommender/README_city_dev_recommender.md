# 🏙️ City Development Recommender System

## 📌 Overview

This project aims to build an **AI-powered city planning system** that recommends how cities should allocate their budgets to improve infrastructure, economic growth, and quality of life.

The system learns from:

- City financial data (revenue, expenditure)
- Development indicators (infrastructure, ICT, transport)

---

## 🎯 Problem Statement

Cities have limited budgets but multiple competing needs.

We want to answer:

> "Given a city's financial condition, how should it allocate its budget for optimal development?"

---

## 🧠 Core Idea

Financial Inputs → Development Outcomes

Example:

- High capital expenditure → better infrastructure
- Low revenue → higher dependency on grants

---

## 📊 Data Sources

### 1. Financial Data
- CityFinance Income Statement
- Municipal financial reports

Features:
- Revenue
- Expenditure
- Surplus/Deficit

---

### 2. Development Data
- Kaggle: 30 Indian Cities Dataset

Features:
- Infrastructure score
- ICT metrics
- Transport indicators

https://www.cityfinance.in/municipal-data/national?utm_source=chatgpt.com

"""
file: Cityfinance_Income Statement_Detailed                  
  Useful Data: Tax Revenue, Fees, Grants, Expenses, Surplus        
    (2019-2023)                                                    
  Why: Full P&L for Navi Mumbai                                    
  ────────────────────────────────────────                         
  File: MarketDashboard_Brihanmumbai                               
  Useful Data: Assets, Receivables, Investments, Cash (2020-2023)
  Why: Balance sheet items for Mumbai                              
  ────────────────────────────────────────                         
  File: CityFinance_Revenue                                        
  Useful Data: Benchmarks by population category                   
  Why: Compare your cities against averages   
  ----------------------------------------
   Yes, city-30.csv has ICT infrastructure metrics only
"""

---

## 🏗️ Project Structure

city-dev-recommender/

data/
  raw/
  processed/

notebooks/

pipeline/
  data_cleaning.py
  feature_engineering.py

models/
  clustering.py
  recommender.py

README.md

---

## ⚙️ Pipeline Overview

Raw Data → Data Cleaning → Feature Engineering → Dataset → ML Models → Recommender

---

## 🚀 Steps to Build the System

### Step 1 — Data Collection and Data Cleaning
- Collect financial data
- Collect development data
- Remove null values
- Standardize city names
- Match cities across datasets

### Step 2 — Raw data to meaningful number
MEANINGFUL SIGNALS (features) that explain city financial health
Right now you only have numbers like:

Revenue
Expenditure
Surplus

👉 These are raw inputs, not intelligence.
fetures to create-
- fiscal Balance (Profit / Loss)
df["fiscal_balance"] = df["Total Revenue"] - df["Total Expenditure"]
- Expense Ratio (Efficiency) - How much of revenue is being spent
df["expense_ratio"] = df["Total Expenditure"] / df["Total Revenue"]

< 1 Efficient spending 
- Surplus Ratio (Financial Strength)
df["surplus_ratio"] = df["fiscal_balance"] / df["Total Revenue"]
- Revenue Growth (VERY IMPORTANT)
df["revenue_growth"] = df["Total Revenue"].pct_change()
-Expenditure Growth
df["expense_growth"] = df["Total Expenditure"].pct_change()


### Step 3 — Feature Engineering
- Revenue per capita
- Surplus/Deficit
- CapEx ratio

### Step 5 — EDA
- Compare cities
- Identify trends

### Step 6 — ML Modeling
- Clustering
- Regression (optional)

### Step 7 — Recommendation Engine
- Rule-based + ML

### Step 8 — Evaluation
- Model metrics
- Policy validation

### Step 9 — Deployment
- API / Dashboard

---

## 🧠 Key Learnings

- Data engineering is the hardest part
- Real-world data is messy
- Combining datasets creates insight

---

## 🔥 Future Improvements

- Satellite data
- Graph Neural Networks
- Reinforcement learning

---

## 📌 Status Checklist

- [ ] Data collected
- [ ] Dataset merged
- [ ] Features engineered
- [ ] Model trained
- [ ] Recommender built

---

## 📜 License

MIT License
