import pandas as pd
import json
from collections import defaultdict

# Initialize dictionaries
fields = {}
common = defaultdict(list)
dec_ra = {}
numerical_data = {}
string_data = {}

# Load workbook
wb = pd.ExcelFile('data\\cggc_nwas_database_cleaned.xlsx')

# Iterate through sheets
for sheetname in wb.sheet_names:
    print(f"INFO: Processing sheet: {sheetname}")
    
    # Load sheet into DataFrame
    df = pd.read_excel(wb, sheet_name=sheetname)
    
    # Dictionary to hold field types
    field_types = defaultdict(list)
    
    # Iterate through columns to populate 'fields' and 'common'
    for col, dtype in df.dtypes.items():
        dtype_str = str(dtype)
        field_types[dtype_str].append(col)
        common[col].append(sheetname)
        
        # Check for 'dec' and 'ra' in any form
        if 'dec' in col.lower() or 'ra' in col.lower():
            dec_ra.setdefault(sheetname, []).append(col)
    
    fields[sheetname] = field_types
    
    # Populate 'numerical_data' and 'string_data'
    for dtype_str, cols in field_types.items():
        if dtype_str.startswith('int') or dtype_str.startswith('float'):
            for col in cols:
                numerical_data.setdefault(col, {}).setdefault('sheet_names', []).append(sheetname)
        else:
            for col in cols:
                string_data.setdefault(col, {}).setdefault('sheet_names', []).append(sheetname)
    
    print(f"INFO: Completed processing for sheet: {sheetname}")

# Simplified AI logic (for demonstration)
# Here you can implement more advanced AI & ML algorithms
# For example, clustering similar columns based on data distribution, outlier detection, etc.

# Save profile to JSON
data_profile = {
    'fields': fields,
    'common': common,
    'dec_ra': dec_ra,
    'numerical_data': numerical_data,
    'string_data': string_data
}

try:
    with open('data_profile.json', 'w') as f:
        json.dump(data_profile, f)
    print("INFO: Saving profile to JSON...")
except Exception as e:
    print(f"ERROR: An unexpected error occurred. Reason: {str(e)}")

print("INFO: Database connection closed.")
