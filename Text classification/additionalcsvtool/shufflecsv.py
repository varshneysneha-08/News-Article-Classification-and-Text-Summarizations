import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Shuffle the rows randomly
shuffled_df = df.sample(frac=1, random_state=42)  # Setting a random_state for reproducibility

# Save the shuffled DataFrame to a new CSV file
shuffled_df.to_csv('data.csv', index=False)