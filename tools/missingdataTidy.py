import pandas as pd
import re
import xlsxwriter

# Function to convert RA and Dec to decimal

def epoch_convert(df):
    def ra_to_decimal(ra_str):
        try:
            h, m, s = map(float, re.findall(r'\d+\.?\d*', ra_str))
            return h + m/60.0 + s/3600.0
        except ValueError:
            return ra_str

    def dec_to_decimal(dec_str):
        try:
            d, m, s = map(float, re.findall(r'\d+\.?\d*', dec_str))
            if '-' in dec_str:
                return -(abs(d) + m/60.0 + s/3600.0)
            else:
                return d + m/60.0 + s/3600.0
        except ValueError:
            return dec_str

    if 'Epoch J2000 Right ascension' in df.columns:
        df['Numeric Epoch J2000 Right ascension'] = df['Epoch J2000 Right ascension'].apply(ra_to_decimal)

    if 'Epoch J2000 Declination' in df.columns:
        df['Numeric Epoch J2000 Declination'] = df['Epoch J2000 Declination'].apply(dec_to_decimal)


    return df

# Read existing Excel workbook
xls = pd.ExcelFile('wikipeadia\\cleaned_missing_data.xlsx')
sheet_names = xls.sheet_names  # Get sheet names to read them later

import pandas as pd

# Initialize writer
with pd.ExcelWriter('wikipeadia\\cleaned_missing_data_v3.xlsx', engine='xlsxwriter') as writer:
    # Open the Excel file
    xls = pd.ExcelFile('wikipeadia\\cleaned_missing_data.xlsx')
    
    # Get the names of all sheets in the Excel file
    sheet_names = xls.sheet_names
    
    # Loop over sheet names and apply conversion only to 'globular_clusters'
    for sheet in sheet_names:
        df = pd.read_excel(xls, sheet)
        if sheet == 'globular_clusters':
            df = epoch_convert(df)
        df.to_excel(writer, sheet_name=sheet, index=False)
        
    # Save the changes
    # Initialize the Excel writer
with pd.ExcelWriter('wikipeadia\\cleaned_missing_data_v3.xlsx', engine='xlsxwriter') as writer:

    # Open the Excel file
    xls = pd.ExcelFile('wikipeadia\\cleaned_missing_data.xlsx')

    # Get all sheet names
    sheet_names = xls.sheet_names

    # Loop through the sheets
    for sheet in sheet_names:
        df = pd.read_excel(xls, sheet)
        if sheet == 'globular_clusters':
            df = epoch_convert(df)
        
        df.to_excel(writer, sheet_name=sheet, index=False)

