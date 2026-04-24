import pandas as pd

# Step 1: Load CSV file
# Replace 'data.csv' with your file name
df = pd.read_csv('data.csv')

# Display first 5 rows
print("Dataset Preview:")
print(df.head())

# Step 2: Select a column (example: 'Marks')
# Replace 'Marks' with your column name
column = df['Marks']

# Step 3: Calculate statistics
mean_value = column.mean()
median_value = column.median()
mode_value = column.mode()[0]   # mode() returns a list

# Step 4: Print results
print("\nBasic Statistics:")
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)