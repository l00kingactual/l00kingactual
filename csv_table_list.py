import os
import csv

def list_csv_tables(directory_path):
    # Initialize CSV file with headers
    with open('tables_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Table', 'Fields'])

    table_id = 1  # Initialize table ID

    for filename in os.listdir(directory_path):
        if filename.endswith(".csv"):
            # Remove '_cleaned' from the table name if present
            table_name = filename.replace('_cleaned', '').replace('.csv', '')

            # Read the first row to get field names
            with open(os.path.join(directory_path, filename), mode='r') as file:
                reader = csv.reader(file)
                fields = next(reader)  # Read the first row

            # Write to tables_list.csv
            with open('tables_list.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([table_id, table_name, ', '.join(fields)])

            table_id += 1  # Increment table ID

if __name__ == "__main__":
    directory_path = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\clean\\csv"
    list_csv_tables(directory_path)
