data = [{'Name': 'John', 'Age': 30, 'City': 'New York'},
        {'Name': 'Alice', 'Age': 25, 'Location': 'San Francisco'},
        {'Name': 'Bob', 'Age': 35, 'City': 'Los Angeles'}]

# Extract unique field names from all dictionaries
fieldnames = list(set().union(*(d.keys() for d in data)))

with open(output_file, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    writer.writerows(data)
