import pandas as pd
import numpy as np
import xlsxwriter
import json

# Load Excel file
xls = pd.ExcelFile('data\\database.xlsx')

# Get sheet names
sheet_names = xls.sheet_names

# Initialize dictionaries
dic_fields = {}
dic_common = {}
dic_dec_ra = {}
numerical_data = {}
string_data = {}
constellation_data = {}
star_data = {}
messier_data = {}
galaxies_data = {}
other_objects_data = {}
exoplanets = {}
vis_mag = {}
abs_mag = {}
distance = {}
mass = {}

# Metadata Extraction
for sheet in sheet_names:
    df = pd.read_excel(xls, sheet)
    
    # Populate dic_fields
    dic_fields[sheet] = {
        'numerical': list(df.select_dtypes(include=['number']).columns),
        'string': list(df.select_dtypes(include=['object']).columns),
        'date': list(df.select_dtypes(include=['datetime']).columns)
    }
    
    # Populate dic_common
    for col in df.columns:
        if col not in dic_common:
            dic_common[col] = {'sheets': [], 'type': df[col].dtype}
        dic_common[col]['sheets'].append(sheet)
    
    # Populate dic_dec_ra
    if 'dec' in df.columns or 'ra' in df.columns:
        dic_dec_ra[sheet] = list(df.columns)
        
    # Populate other dictionaries based on conditions
    for col in df.columns:
        if 'constellation' in col.lower():
            constellation_data.setdefault(sheet, []).append(col)
        if 'star' in col.lower():
            star_data.setdefault(sheet, []).append(col)
        if 'messier' in col.lower():
            messier_data.setdefault(sheet, []).append(col)
        if 'galaxy' in col.lower():
            galaxies_data.setdefault(sheet, []).append(col)
        if 'exoplanet' in col.lower():
            exoplanets.setdefault(sheet, []).append(col)
        if 'vis_mag' in col.lower():
            vis_mag.setdefault(sheet, []).append(col)
        if 'abs_mag' in col.lower():
            abs_mag.setdefault(sheet, []).append(col)
        if 'distance' in col.lower():
            distance.setdefault(sheet, []).append(col)
        if 'mass' in col.lower():
            mass.setdefault(sheet, []).append(col)
        # Add your custom conditions for other_objects_data here

# Serialize dictionaries to JSON
db_profile = {
    'dic_fields': dic_fields,
    'dic_common': dic_common,
    'dic_dec_ra': dic_dec_ra,
    'numerical_data': numerical_data,
    'string_data': string_data,
    'constellation_data': constellation_data,
    'star_data': star_data,
    'messier_data': messier_data,
    'galaxies_data': galaxies_data,
    'other_objects_data': other_objects_data,
    'exoplanets': exoplanets,
    'vis_mag': vis_mag,
    'abs_mag': abs_mag,
    'distance': distance,
    'mass': mass
}

with open('db_profile.json', 'w') as f:
    json.dump(db_profile, f, indent=4)
