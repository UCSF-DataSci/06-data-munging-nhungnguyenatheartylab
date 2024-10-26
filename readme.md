### Documentation of process and findings for the Assignment #6

### Part 0: Creating the Messy Dataset

# Install packages needed in a virtual environment
        ```pip install pandas ```
         ```pip install numpy ```
         ```pip install argparse ```
         ```pip install tqdm ```

# Run the provided `dirty-data.py` script to create the messy dataset:
          ```python dirty-data.py```

# The dataset `messy_population_data.csv` was gerated.

### Create the script file for data cleaning
      ```nano clean_data.py```

### Load the messy dataset ("messy_population_data.csv") using Python with pandas
         ```import pandas as pd```
        ```df = pd.read_csv("messy_population_data.csv")```

### Part 1: Identifying Data Issues
df.info ()
df.describe ()
print(df.dtypes)

# Check values in each column
df['age'].value_counts()
df['gender'].value_counts()
df['income_groups'].value_counts()
df['year'].value_counts()
df['population'].value_counts()
      
# Number of missing values for each column:
           income_groups    6306
           age              6223
           gender           5907
           year             6202
           population       6340

# Number of duplicates: 2950

# Column(s) affected: The "income_groups" column has many typos, the columns "population" and "year" have unusual values

low_income                  28433
upper_middle_income         28354
high_income                 28343
lower_middle_income         28323
lower_middle_income_typo     1517
low_income_typo              1505
high_income_typo             1475
upper_middle_income_typo     1462

# Example of the problematic data: Some year values are greater than the current year, while some population values are very small.

      year
2113.0      2
2108.0      2
2117.0      1
2118.0      1
2102.0      1


population
104.0        6
189.0        5
454.0        5
270.0        5
105.0        5
 
 # Potential impact on analysis if left uncleaned: Wrong estimates and predictions will be made if using the uncleaned data

### Part 2: Data cleaning
# Drop missing values
df.dropna() 
              income_groups   age  gender    year  population
0               high_income   0.0     1.0  1950.0   7798286.0
1               high_income   0.0     1.0  1951.0   7739711.0
2               high_income   0.0     3.0  1952.0   7713905.0
3               high_income   0.0     1.0  1953.0   7722053.0
4               high_income   0.0     1.0  1954.0   7756149.0
...                     ...   ...     ...     ...         ...
125713           low_income  29.0     1.0  2115.0  16617821.0
125714           low_income  27.0     1.0  2108.0   4913711.0
125715  lower_middle_income  87.0     2.0  2105.0   3978771.0
125716  lower_middle_income  74.0     1.0  2110.0   9614177.0
125717           low_income  16.0     2.0  2111.0   9182705.0

[97639 rows x 5 columns]

# Drop duplicates
>>> df.drop_duplicates()
              income_groups   age  gender    year  population
0               high_income   0.0     1.0  1950.0   7798286.0
1               high_income   0.0     1.0  1951.0   7739711.0
2               high_income   0.0     3.0  1952.0   7713905.0
3               high_income   0.0     1.0  1953.0   7722053.0
4               high_income   0.0     1.0  1954.0   7756149.0
...                     ...   ...     ...     ...         ...
125713           low_income  29.0     1.0  2115.0  16617821.0
125714           low_income  27.0     1.0  2108.0   4913711.0
125715  lower_middle_income  87.0     2.0  2105.0   3978771.0
125716  lower_middle_income  74.0     1.0  2110.0   9614177.0
125717           low_income  16.0     2.0  2111.0   9182705.0

[122768 rows x 5 columns]

# Fix typos in the column income_groups:
income_groups
low_income             29938
lower_middle_income    29840
high_income            29818
upper_middle_income    29816

### Part 3: Documenting Results
# The cleaned data now has no missing values or duplicates or invalid values for year. The number of data points reduces more than half.
# Having errors with the command to remove outliers in the column population. When. I tried to remove outliers, the results returned all null values!
# Some missing values in the income_groups were stored as "" not NaN
