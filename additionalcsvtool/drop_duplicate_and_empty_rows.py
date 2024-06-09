import pandas as pd

# Replace 'path/to/your/data.csv' with the actual path to your CSV file
df = pd.read_csv('model_dataset.csv')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.to_csv('model_dataset.csv', index=False)