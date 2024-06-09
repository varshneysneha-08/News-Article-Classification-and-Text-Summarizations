import pandas as pd

# List of CSV file paths to be combined
csv_files = ['data.csv', 'pol2_processed.csv']

# Create an empty DataFrame
pol_combined = pd.DataFrame()

# Loop through the CSV files and concatenate them vertically
for file in csv_files:
    data = pd.read_csv(file)
    pol_combined = pd.concat([pol_combined, data], ignore_index=True)

# Save the combined data to a new CSV file
pol_combined.to_csv('pol_combined.csv', index=False)