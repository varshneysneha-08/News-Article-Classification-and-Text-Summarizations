import csv

def replace_label(csv_file, label_column, label_to_replace, new_value):
    # Read the CSV file and store its content in a list of dictionaries
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Update values based on the specified label and new value
    for row in data:
        if row[label_column] == label_to_replace:
            row[label_column] = new_value

    # Write the updated data back to the CSV file
    fieldnames = data[0].keys() if data else []
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Example usage
csv_file_path = 'new_file.csv'
label_column_name = 'Category'  # Replace with the actual column name containing labels
label_to_replace = 'sport'
new_value = 'sports'

replace_label(csv_file_path, label_column_name, label_to_replace, new_value)
