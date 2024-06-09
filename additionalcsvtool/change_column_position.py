import csv

def change_column_position(csv_file, old_index, new_index):
    # Read the CSV file and store its content in a list of dictionaries
    with open(csv_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Change the position of the specified column
    for row in data:
        row_keys = list(row.keys())
        row_values = list(row.values())

        # Remove the column from the current position
        removed_column = row_keys.pop(old_index)
        row_values.pop(old_index)

        # Insert the column at the new position
        row_keys.insert(new_index, removed_column)
        row_values.insert(new_index, row[removed_column])

        # Update the row with the new order
        row.clear()
        row.update(zip(row_keys, row_values))

    # Write the updated data back to the CSV file
    fieldnames = data[0].keys() if data else []
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# Example usage
csv_file_path = 'new_file.csv'
old_index = 1  # Index of the column to move (0-based)
new_index = 0  # New index for the column

change_column_position(csv_file_path, old_index, new_index)
