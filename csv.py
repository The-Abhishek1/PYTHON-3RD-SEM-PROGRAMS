import csv

# Create a new CSV file with headers
with open('example.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])

# Insert values into the CSV file
with open('example.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['John Doe', '30', 'New York'])
    writer.writerow(['Jane Smith', '25', 'San Francisco'])
    writer.writerow(['Bob Johnson', '40', 'Los Angeles'])

# Operate on multiple columns in the CSV file
with open('example.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}.")

# Update values in the CSV file
with open('example.csv', mode='r', newline='') as file:
    rows = list(csv.DictReader(file))
    rows[0]['Age'] = '31'
    rows[2]['City'] = 'Chicago'

with open('example.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
    writer.writeheader()
    writer.writerows(rows)

# Delete values in the CSV file
with open('example.csv', mode='r', newline='') as file:
    rows = list(csv.DictReader(file))
    rows.pop(1)

with open('example.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
    writer.writeheader()
    writer.writerows(rows)
