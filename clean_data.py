# Scripts for data cleaning - Assignment #6

import pandas as pd
import numpy as np
from scipy import stats

# Load the raw dataset
df = pd.read_csv("messy_population_data.csv")
print("***Describe messy data***:")
df.info()

# Part 2: Cleaning the Data
#2.1. Check and drop rows with missing data 
df.replace("", pd.NA, inplace=True)
df.replace("N/A", pd.NA, inplace=True)
missing_values= df.isnull().sum()
print(missing_values)
df.dropna(inplace=True)  
print(df.isnull().sum()) 

#print(df['income_groups'].unique())
#df.dropna(subset=['income_groups'], inplace=True)


#2.2. Check and remove duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
df.drop_duplicates(inplace=True)

#2.3. Check outliers
#df['z_score'] = stats.zscore(df['population'])
#df = df[df['z_score'].abs() <= 3]
#df = df.drop(columns=['z_score'])

#2.4. Correcting the typos in the income_groups column
df['income_groups'] = df['income_groups'].replace({
    'lower_middle_income_typo': 'lower_middle_income',
    'low_income_typo': 'low_income',
    'high_income_typo': 'high_income',
    'upper_middle_income_typo': 'upper_middle_income'
})

# Drop if year > 2024
df.sort_values(by='year', ascending=True)
df = df[df['year'] <= 2024]

# Save the cleaned dataset
df.to_csv("cleaned_population_data.csv", index=False)

print("***Clean dataset desciption***")
df.info()
df = pd.read_csv("cleaned_population_data.csv")
df.describe(include='all')
missing_values= df.isnull().sum()
print(missing_values)
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")