import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# Step 1: Checking missing values
print("Missing Values:\n", df.isnull().sum())

# Step 2: Handling missing values
# Fill missing age with median, and embark with mode
df['age'].fillna(df['age'].median(), inplace=True)
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)

# Step 3: Drop rows with any missing values in important columns
df.dropna(subset=['deck'], inplace=True)

print("\nAfter Handling Missing Values:\n", df.isnull().sum())

# Handling Duplicates
# Step 1: Check for duplicates
duplicates = df.duplicated().sum()
print("\nNumber of Duplicates:", duplicates)

# Step 2: Drop duplicates if any
df.drop_duplicates(inplace=True)

# Detecting Outliers
# Using IQR for outlier detection in the 'age' column
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['age'] < (Q1 - 1.5 * IQR)) | (df['age'] > (Q3 + 1.5 * IQR))]

print("\nOutliers in 'age' column:\n", outliers[['age']])