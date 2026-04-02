# Understand how the city is behaving financially over time
import pandas as pd
import matplotlib.pyplot as plt

# Load Navi Mumbai Balance Sheet data
filepath = "../../City-Dataset/Cityfinance_Balance Sheet_Summary_NMMC_22-23.xlsx"
df = pd.read_excel(filepath, sheet_name='Balance Sheet')

# Clean and prepare data
df = df.dropna(subset=['Major Group/Minor Group'])  # Remove rows with NaN in description
df = df[df['Major Group/Minor Group'].str.contains('Assets|Investments|Reserves', case=False, na=False)]  # Filter useful rows

# Melt the dataframe to long format for time series plotting
years = ['2019-20', '2020-21', '2021-22', '2022-23']
df_melted = df.melt(id_vars=['Major Group/Minor Group'], value_vars=years,
                    var_name='Year', value_name='Amount')

# Convert Amount to numeric, handling any non-numeric values
df_melted['Amount'] = pd.to_numeric(df_melted['Amount'], errors='coerce')
df_melted = df_melted.dropna()

# Sort by year
df_melted['Year'] = pd.Categorical(df_melted['Year'], categories=years, ordered=True)
df_melted = df_melted.sort_values('Year')

print("Data preview:")
print(df_melted.head())

# Create visualization
plt.figure(figsize=(12, 8))

# Plot each financial category
for category in df_melted['Major Group/Minor Group'].unique():
    category_data = df_melted[df_melted['Major Group/Minor Group'] == category]
    plt.plot(category_data['Year'], category_data['Amount'] / 1e9,  # Convert to billions for readability
             marker='o', label=category, linewidth=2)

plt.title('Navi Mumbai Financial Assets Over Time (in Billions INR)', fontsize=14, fontweight='bold')
plt.xlabel('Financial Year', fontsize=12)
plt.ylabel('Amount (Billions INR)', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('/Users/swapnil/Documents/Coding/Python/A-computer-vision/CV-Projects-be/40daysCV/3-ModelTraining/CityDev-Recommender/utils/navi_mumbai_financial_trends.png', dpi=300, bbox_inches='tight')
print("Visualization saved as 'navi_mumbai_financial_trends.png'")

# Show summary statistics
print("\nSummary Statistics:")
summary = df_melted.groupby(['Major Group/Minor Group', 'Year'])['Amount'].sum().unstack()
print(summary / 1e9)  # In billions