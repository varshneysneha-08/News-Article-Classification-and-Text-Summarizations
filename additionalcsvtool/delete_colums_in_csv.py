import pandas as pd

# Read the CSV file into a DataFrame with tab as the delimiter
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/crawling and scraping/bbc-news-data.csv', error_bad_lines=False, delimiter='\t')

# Print the column titles
print(df.columns)
columns_to_delete = [ 'filename', 'title']

# Drop the specified columns
df = df.drop(columns=columns_to_delete)

# Save the modified DataFrame back to a CSV file
df.to_csv('new_file.csv', index=False)
