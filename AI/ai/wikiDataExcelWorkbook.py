import os
import pandas as pd

# Initialize directories and file paths
input_dir = 'csv_data\\wikiData\\'
output_file_path = 'csv_data\\xlsx\\wikiData.xlsx'

# Initialize an empty dictionary to hold DataFrames
dfs = {}

# Log: Starting the process
print("Starting the process of amalgamating CSV files.")

# Read CSV files into DataFrames
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        filepath = os.path.join(input_dir, filename)
        
        # Log: Reading file
        print(f"Reading file: {filename}")
        
        # Read CSV into DataFrame
        try:
            df = pd.read_csv(filepath, on_bad_lines='skip')
        except Exception as e:
            print(f"Exception occurred while reading {filename}: {e}")
            continue
        
        # Extract base name (without _table_number)
        base_name = filename.split('_table_')[0]
        
        # Combine DataFrames with the same base name
        if base_name in dfs:
            dfs[base_name] = pd.concat([dfs[base_name], df], ignore_index=True)
        else:
            dfs[base_name] = df

# Log: Writing to Excel
print("Writing DataFrames to Excel workbook.")

# Write DataFrames to Excel workbook
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, df in dfs.items():
        # Log: Writing sheet
        print(f"Writing sheet: {sheet_name}")
        
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# Log: Process completed
print("All steps completed.")
