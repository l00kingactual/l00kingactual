import pandas as pd
import json
import logging
import re

# Initialize logging
logging.basicConfig(filename='database_log.json', level=logging.INFO, format='%(asctime)s %(message)s')

# Initialize exceptions dictionary
exceptions_dict = {}

# Initialize a dictionary to keep track of column names
column_names = {}

# Define the excel_file_path
excel_file_path = "data\\cggc_nwas_database_cleaned.xlsx"

# Custom serializer for JSON
def custom_serializer(obj):
    if isinstance(obj, pd.DataFrame):
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def determine_data_type(column):
    """
    Determine the SQL data type for a given pandas Series.
    """
    # Check for datetime
    if pd.api.types.is_datetime64_any_dtype(column):
        return "DATETIME"
    
    # Check for boolean
    if pd.api.types.is_bool_dtype(column):
        return "BOOLEAN"
    
    # Check for integer
    if pd.api.types.is_integer_dtype(column):
        return "INT"
    
    # Check for float
    if pd.api.types.is_float_dtype(column):
        return "FLOAT"
    
    # Check for object or string
    if pd.api.types.is_object_dtype(column):
        # Further logic to differentiate between plain strings and potential JSON objects, etc.
        return "TEXT"
    
    # Default to TEXT
    return "TEXT"
'''
# Example usage:
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')
for col in df.columns:
    dtype = determine_data_type(df[col])
    print(f"The column {col} has data type {dtype}.")
'''

# Initialize dictionaries for data profiling
fields_dict = {}
common_dict = {}
dec_ra_dict = {}
numerical_data_dict = {}
string_data_dict = {}
duplicates_dict = {}
field_types_dict = {}
dec_ra_full = {}

# Read Excel file
xls = pd.ExcelFile(excel_file_path)

from collections import defaultdict

# Initialize a dictionary to keep track of duplicate column names
duplicate_column_tracker = defaultdict(int)

# Loop through each sheet in the 


from concurrent.futures import ThreadPoolExecutor

def process_sheet(sheet_name):
    try:
        logging.info(f"Reading sheet {sheet_name}")
        print(f"Reading sheet {sheet_name}")

        # Read the sheet into a DataFrame
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)

        # Sanitize column names and handle duplicates
        new_columns = []
        duplicate_column_tracker = {}
        for col in df.columns:
            sanitized_col = col.strip().replace(" ", "_").replace(".", "")
            if sanitized_col in new_columns:
                duplicate_column_tracker[sanitized_col] = duplicate_column_tracker.get(sanitized_col, 0) + 1
                sanitized_col = f"{sanitized_col}_{duplicate_column_tracker[sanitized_col]}"
            new_columns.append(sanitized_col)

        # Update DataFrame with new column names
        df.columns = new_columns

        # Write back the new header row to the sheet
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

        # Update fields_dict for data profiling
        fields_dict[sheet_name] = {
            "numerical": [col for col in df.columns if determine_data_type(df[col]) in ["INT", "FLOAT"]],
            "string": [col for col in df.columns if determine_data_type(df[col]) == "TEXT"],
            "date": [col for col in df.columns if determine_data_type(df[col]) == "DATETIME"],
            "boolean": [col for col in df.columns if determine_data_type(df[col]) == "BOOLEAN"]
        }
    except Exception as e:
        logging.error(f"An error occurred while processing sheet {sheet_name}: {e}")
        exceptions_dict[sheet_name] = str(e)

# Initialize dictionaries for data profiling
fields_dict = {}
common_dict = {}
dec_ra_dict = {}
numerical_data_dict = {}
string_data_dict = {}
duplicates_dict = {}
field_types_dict = {}
dec_ra_full = {}
exceptions_dict = {}

# Initialize logging
logging.basicConfig(filename='database_log.json', level=logging.INFO, format='%(asctime)s %(message)s')

# Define the excel_file_path
excel_file_path = "data\\cggc_nwas_database_cleaned.xlsx"

# Read sheet names
xls = pd.ExcelFile(excel_file_path)
sheet_names = xls.sheet_names

# Process sheets in parallel
with ThreadPoolExecutor() as executor:
    executor.map(process_sheet, sheet_names)

# Save exceptions to JSON
with open('database_exceptions.json', 'w') as f:
    json.dump(exceptions_dict, f, default=custom_serializer)

# Save dictionaries to JSON (database_profile_enhanced.json)
with open('database_profile_enhanced.json', 'w') as f:
    json.dump({
        'fields': fields_dict,
        'common': common_dict,
        'dec_ra': dec_ra_dict,
        'numerical_data': numerical_data_dict,
        'string_data': string_data_dict,
        'duplicates': duplicates_dict,
        'field_types': field_types_dict
    }, f, default=custom_serializer)

logging.info("Successfully completed all tasks.")
print("Successfully completed all tasks.")

