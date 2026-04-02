import pandas as pd

# Path to the Excel file (using absolute path for reliability)
filepath = "/Users/swapnil/Documents/Coding/Python/A-computer-vision/CV-Projects-be/40daysCV/3-ModelTraining/City-Dataset/Cityfinance_Balance Sheet_Summary_2026-03-27_00-50-45.xlsx"

# Load the Excel file to check available sheets
excel_file = pd.ExcelFile(filepath)
print("Available sheets:", excel_file.sheet_names)

# Read the first sheet
df = pd.read_excel(filepath, sheet_name=0)
print("Data shape:", df.shape)
print("Columns:", list(df.columns))
print("\nFull DataFrame:")
print(df)

# To identify useful data, look for rows with financial terms
useful_keywords = ['asset', 'cash', 'investment', 'receivable', 'liability', 'equity', 'reserve']
print("\nRows containing useful keywords:")
for index, row in df.iterrows():
    text = str(row['Major Group/Minor Group']).lower()
    if any(keyword in text for keyword in useful_keywords):
        print(f"Row {index}: {row['Major Group/Minor Group']} - Values: {row[['2022-23', '2021-22', '2020-21', '2019-20']].to_dict()}")

# Useful columns are typically the monetary value columns for different years
useful_columns = ['2022-23', '2021-22', '2020-21', '2019-20']
print(f"\nUseful columns for analysis: {useful_columns}")
print("These contain the financial values over time.")


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