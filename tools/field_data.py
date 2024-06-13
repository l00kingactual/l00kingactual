import os
import pandas as pd
from collections import defaultdict

# Initialize dictionaries to hold table fields and field usage
table_fields = {}
field_usage = defaultdict(list)

# Directory containing the cleaned CSV files
input_dir = "data\\cleaned\\database_cleaned\\"

# Read headers of all CSV files
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        filepath = os.path.join(input_dir, filename)
        try:
            df = pd.read_csv(filepath, nrows=0)  # Read only the header
            fields = df.columns.tolist()
            table_name = filename[:-4]  # Remove '.csv' from filename
            table_fields[table_name] = fields

            # Update field usage
            for field in fields:
                field_usage[field].append(table_name)

        except Exception as e:
            print(f"An error occurred while reading {filename}: {e}")

# Create table_fields.csv
table_fields_df = pd.DataFrame(list(table_fields.items()), columns=['table', 'fields'])
table_fields_df['fields'] = table_fields_df['fields'].apply(lambda x: ','.join(x))
table_fields_df.to_csv("table_fields.csv", index=False)

# Create field_usage.csv
field_usage_df = pd.DataFrame(list(field_usage.items()), columns=['field', 'tables'])
field_usage_df['tables'] = field_usage_df['tables'].apply(lambda x: ','.join(x))
field_usage_df.to_csv("field_usage.csv", index=False)

print("CSV files created successfully.")
