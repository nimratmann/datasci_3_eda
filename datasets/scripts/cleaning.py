# Univariate Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## loading the clean .csv file - patients_cleaned.csv

df = pd.read_csv('https://raw.githubusercontent.com/nimratmann/datasci_3_eda/main/datasets/processed/health-medicare-drug-spending.csv')

df.columns

## Displaying the first 10 rows of the dataset
df.head(10)

## Health Medicare Drug Spending Data 
## This is a curated collection on Medicare prescription drug spending from 2010 - 2015. Medicare Part B is part of Original Medicare and covers services and supplies that are medically necessary to treat your health condition. This can include outpatient care, preventive services, ambulance services and durable medical equipment. Medicare Part D refers to prescription drug coverage. Medicare is a single-payer national social insurance program administered by the US federal government.

# Calculate measures of central tendency
mean = df['unit_count'].mean()
median = df['unit_count'].median()
mode = df['unit_count'].mode().values[0]

# Calculate measures of central tendency
mean = df['total_spending'].mean()
median = df['total_spending'].median()
mode = df['total_spending'].mode().values[0]

# Calculate measures of spread
range_val = df['unit_count'].max() - df['unit_count'].min()
variance = df['unit_count'].var()
std_deviation = df['unit_count'].std()
iqr = df['unit_count'].quantile(0.75) - df['unit_count'].quantile(0.25)

# Calculate measures of spread
range_val = df['total_spending'].max() - df['total_spending'].min()
variance = df['total_spending'].var()
std_deviation = df['total_spending'].std()
iqr = df['total_spending'].quantile(0.75) - df['total_spending'].quantile(0.25)

# Print the results
print("Measures of Central Tendency:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print("\nMeasures of Spread:")
print(f"Range: {range_val}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"IQR (Interquartile Range): {iqr}")


# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(df['brand_name'], bins=20, color='skyblue', edgecolor='black')
plt.title('Average Cost Per Unit')
plt.xlabel('brand_name')
plt.ylabel('unit_cost')
plt.grid(True)
plt.show()

# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(df['total_spending'], bins=20, color='navy', edgecolor='black')
plt.title('Spending Based on Coverage Type')
plt.xlabel('coverage_type')
plt.ylabel('total_spending')
plt.grid(True)
plt.show()

# Bivariate Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Scatter plot for Brand Name vs. Cost per Unit
plt.figure(figsize=(8, 6))
plt.scatter(df['brand_name'], df['unit_cost'], alpha=0.5, color='blue')
plt.title('Scatter Plot: Drug Brand Name vs. Cost per Unit')
plt.xlabel('brand_name')
plt.ylabel('unit_cost')
plt.grid(True)
plt.show()

# Scatter plot for Coverage Type vs. Total Spending 
plt.figure(figsize=(8, 6))
plt.scatter(df['coverage_type'], df['total_spending'], alpha=0.5, color='red')
plt.title('Scatter Plot: Medicare Coverage Type vs. Total Spending')
plt.xlabel('coverage_type')
plt.ylabel('total_spending')
plt.grid(True)
plt.show()

# Compute correlation matrix for numerical variables
correlation_matrix = df.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Strong Correlations
# For computing the correlation coefficient:heatmap. 

#Handling Outliers
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
