import csv

def rename_columns(csv_file, old_column_names, new_column_names):
    # Read the CSV file and store its content in a list of dictionaries
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Rename the specified columns
    for row in data:
        for old_name, new_name in zip(old_column_names, new_column_names):
            row[new_name] = row.pop(old_name, None)

    # Write the updated data back to the CSV file
    fieldnames = new_column_names
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Example usage
csv_file_path = 'new_file.csv'
old_columns = ['content', 'category']  # Replace with the actual old column names
new_columns = ['article', 'Category']  # Replace with the corresponding new column names

rename_columns(csv_file_path, old_columns, new_columns)
