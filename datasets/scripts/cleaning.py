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
ata = {'generic_name': ['Aripiprazole', 'Paclitaxel Protein-Bound', 'Albuterol Sulfate', 'Fluticasone/Salmeterol', 'Everolimus', 'Pemetrexed Disodium', 'Darbepoetin Alfa In Polysorbat', 'Efavirenz/Emtricitab/Tenofovir', 'Bevacizumab', 'Azacitidine'],
        'average_cost_per_unit': [10.5, 20.2, 5.5, 15.1, 18.9, 22.3, 12.7, 9.8, 25.0, 8.4]}

df = pd.DataFrame(data)

# Calculate the frequency of each generic name
generic_counts = df['generic_name'].value_counts()

# Select the top 10 generic names
top_10_generics = generic_counts.head(10).index.tolist()

# Filter the DataFrame to include only the top 10 generic names
filtered_df = df[df['generic_name'].isin(top_10_generics)]

plt.figure(figsize=(8, 6))
plt.bar(df['generic_name'], df['average_cost_per_unit'], color='pink', edgecolor='black')
plt.title('Average Cost Per Unit by Generic Name')
plt.xlabel('generic_name')
plt.ylabel('average_cost_per_unit')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()


# Create a histogram
plt.figure(figsize=(8, 6))
plt.hist(df['year'], bins=5, color='skyblue', edgecolor='blue')
plt.title('Total Spending 2010-2015, a growing trend')
plt.xlabel('year')
plt.ylabel('Total Spending')
plt.grid(True)
plt.show()

# Bivariate Analysis

# Scatter plot for Unit Count vs. Average Cost Per Unit 
plt.figure(figsize=(8, 6))
plt.scatter(df['average_cost_per_unit'], df['unit_count'], alpha=0.5, color='red')
plt.title('Scatter Plot: Unit Count vs. Average Cost Per Unit ')
plt.xlabel('Average Cost Per Unit ')
plt.ylabel('Unit Count')
plt.xlim(0, max(df['average_cost_per_unit']) * 0.01 )  # Adjust the multiplier as needed
plt.ylim(0, max(df['unit_count']) * 0.01 )  # Adjust the multiplier as needed
plt.grid(True)
plt.show()


# Compute correlation matrix for numerical variables
numerical_columns = df.select_dtypes(include=[np.number])

correlation_matrix = numerical_columns.corr()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot a heatmap of the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=0.5)
plt.title('Heatmap')
plt.show()

# Handling Outliers
variable_of_interest = 'average_beneficiary_cost_share_no_lis'

Q1 = df[variable_of_interest].quantile(0.25)
Q3 = df[variable_of_interest].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df[variable_of_interest] < lower_bound) | (df[variable_of_interest] > upper_bound)]

plt.figure(figsize=(8, 6))
sns.boxplot(x=variable_of_interest, data=df, palette='Set3')
plt.title(f'Boxplot: {variable_of_interest}')
plt.xlabel(variable_of_interest)
plt.grid(True)
plt.show()
