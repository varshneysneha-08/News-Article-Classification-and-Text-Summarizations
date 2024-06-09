import pandas as pd

# Replace 'path/to/your/data.csv' with the actual path to your CSV file
csv_file_path = 'file2.csv'
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/crawling and scraping/file2.csv')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
# Create a new DataFrame with an equal number of rows from each category
min_rows = df['Category'].value_counts().min()
print(df['Category'].value_counts())
selected_categories=df['Category'].unique()
print(selected_categories)
equal_rows_df = pd.concat([df[df['Category'] == category].sample(min_rows) for category in selected_categories])
# Display the first few rows of the new DataFrame
print(equal_rows_df.head())

# Save the new DataFrame to a new CSV file
equal_rows_csv_path = 'file22.csv'
equal_rows_df.to_csv(equal_rows_csv_path, index=False)