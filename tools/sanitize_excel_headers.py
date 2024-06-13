
import pandas as pd
from openpyxl import load_workbook
import json
import re
import logging

# Initialize logging
logging.basicConfig(filename='database_log.json', level=logging.INFO, format='%(asctime)s %(message)s')

# Initialize exceptions dictionary
exceptions_dict = {}

# Function to sanitize header names for MySQL compatibility
def sanitize_header_name(name):
    sanitized_name = re.sub(r'\W+', '_', name)  # Replace non-alphanumeric characters with '_'
    sanitized_name = re.sub(r'^\d+', '', sanitized_name)  # Remove leading digits
    return sanitized_name.lower()  # Convert to lowercase for MySQL

# Initialize the excel_file_path
excel_file_path = "data\\cggc_nwas_database_cleaned.xlsx"

# Initialize a dictionary to keep track of sanitized column names
sanitized_column_names = {}

# Initialize workbook writer
book = load_workbook(excel_file_path)
writer = pd.ExcelWriter('cggc_nwas_database_cleaned_sanitized.xlsx', engine='openpyxl')
writer.book = book

try:
    # Load Excel workbook
    xl = pd.ExcelFile(excel_file_path)
    
    # Loop through each sheet in the workbook
    for sheet_name in xl.sheet_names:
        logging.info(f"Processing sheet for header sanitisation: {sheet_name}")
        
        # Read sheet into a DataFrame
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        
        # Initialize an empty list to keep track of new column names for the current sheet
        new_column_names = []
        
        # Check for duplicate and blank field names
        seen = {}
        for idx, col in enumerate(df.columns):
            sanitized_col = sanitize_header_name(col if not pd.isna(col) else f"blank_{idx}")
            
            # Handle duplicates
            if sanitized_col in seen:
                seen[sanitized_col] += 1
                sanitized_col = f"{sanitized_col}_{seen[sanitized_col]}"
            else:
                seen[sanitized_col] = 0
            
            new_column_names.append(sanitized_col)
        
        # Update DataFrame columns
        df.columns = new_column_names
        
        # Save changes to the workbook
        df.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Update sanitized column names dictionary
        sanitized_column_names[sheet_name] = new_column_names
        
        logging.info(f"Completed processing sheet for header sanitisation: {sheet_name}")
    
    # Save the workbook after all sheets are processed
    writer.save()
    logging.info("Workbook processed and saved successfully.")

except Exception as e:
    exceptions_dict['header_sanitisation'] = str(e)
    logging.error(f"An exception occurred: {str(e)}")

# Log exceptions if any
if exceptions_dict:
    with open('database_exceptions.json', 'w') as f:
        json.dump(exceptions_dict, f)

# Save sanitized_column_names for later use
with open('sanitized_column_names.json', 'w') as f:
    json.dump(sanitized_column_names, f)
