import pandas as pd

"""
1. Script for dataset preprocessing

Preprocessing depends on the dataset. The script needs to be adapted for your dataset.
Checkpoint 1 included finding the dataset and analysis. Here we need to preprocess based on that analysis.
Below is an example of preprocessing the cars dataset.
"""

# Defining path to CSV file
CSV_FILE_PATH = "CarsData.csv"

# Loading CSV file and displaying row and column count
df = pd.read_csv(CSV_FILE_PATH, delimiter=',')
print("CSV size before: ", df.shape)

# Clean whitespace from column names and data
df.columns = df.columns.str.strip()
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Convert price and mileage to numeric, removing any currency symbols or commas
df['price'] = pd.to_numeric(df['price'])
df['mileage'] = pd.to_numeric(df['mileage'])

# Standardize manufacturer names (example: convert variations of names)
df['Manufacturer'] = df['Manufacturer'].str.lower()
df['Manufacturer'] = df['Manufacturer'].replace({
    'bmw': 'BMW',
    'merc': 'Mercedes-Benz',
    'volkswagen': 'Volkswagen',
    'toyota': 'Toyota',
    'hyundi': 'Hyundai',
    'vauxhall': 'Vauxhall',
    'audi': 'Audi',
    'skoda': 'Skoda',
    'ford': 'Ford'
})

# Drop any rows with missing values
df = df.dropna()
print("CSV size after: ", df.shape)
print(df.head())

# Random split of dataset into 80:20 (will need later)
df20 = df.sample(frac=0.2, random_state=1)
df = df.drop(df20.index)
print("CSV size 80: ", df.shape)
print("CSV size 20: ", df20.shape)

# Save preprocessed dataset to new CSV file
df.to_csv("CarsData_PROCESSED.csv", index=False)
df20.to_csv("CarsData_PROCESSED_20.csv", index=False)