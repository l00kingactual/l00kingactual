import pandas as pd
import os

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text

def simplify_name(filename):
    name_parts = filename.split("_")
    return name_parts[0]

input_dir = 'wikipeadia\\arch\\'
output_file = 'combined_data.xlsx'

with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            df = pd.read_csv(f'{input_dir}{filename}')
            
            # Remove 'List_of_' prefix and simplify the filename to use as sheet name
            sheet_name = simplify_name(remove_prefix(filename.replace('.csv', ''), 'List_of_'))
            
            # Check for Excel's sheetname length limit
            if len(sheet_name) > 31:
                sheet_name = sheet_name[:31]
            
            df.to_excel(writer, sheet_name=sheet_name, index=False)


# Define function to remove "List_of_" from a string
def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]

# Specify the directory where the CSV files are located
input_dir = 'wikipeadia\\arch\\'
output_dir = 'wikipeadia\\arch\\'  # Output directory, as specified

# Initialize Excel writer
with pd.ExcelWriter(f'{output_dir}combined_data.xlsx', engine='xlsxwriter') as writer:

    # Loop through each CSV file in the directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            # Read the CSV file into a DataFrame
            df = pd.read_csv(f'{input_dir}{filename}')
            
            # Optionally, sort the DataFrame by a specific column if needed
            # df = df.sort_values(by='YourColumnName')

            # Remove "List_of_" from filename to use as sheet name
            sheet_name = remove_prefix(filename.replace('.csv', ''), 'List_of_')
            
            # Write DataFrame to specific Excel sheet
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# The Excel file is saved automatically when exiting the 'with' block
