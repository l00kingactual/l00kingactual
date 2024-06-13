import pandas as pd

# Function to clean general unwanted elements
def general_clean(df):
    df.replace(to_replace=r'\[.*?\]', value='', regex=True, inplace=True)
    df.replace(to_replace='back to top', value='', regex=True, inplace=True)
    return df

import re

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

    df['Epoch J2000 Right ascension'] = df['Epoch J2000 Right ascension'].apply(ra_to_decimal)
    df['Epoch J2000 Declination'] = df['Epoch J2000 Declination'].apply(dec_to_decimal)

    return df


# Function to clean 'unnumbered minor planets' sheet
def clean_unnumbered(df):
    # Combining multi-row headers and renaming them
    new_header = df.iloc[0]  # Assuming the header is at row 0
    df = df[1:]  # Remove the first row
    df.columns = new_header  # Set the header row as df header
    df.reset_index(drop=True, inplace=True)

    # Adding a date column
    df['Date'] = "1980-1989"  # Add dates according to your logic
    
    return df

# Read the Excel file
xl = pd.ExcelFile('wikipedia\\cleaned_missing_data.xlsx')

# Initialize ExcelWriter to save cleaned data
with pd.ExcelWriter('wikipedia\\cleaned_missing_data_v1.xlsx') as writer:
    # Iterate through each sheet
    for sheet in xl.sheet_names:
        df = xl.parse(sheet)

        # Perform general cleaning on each sheet
        df = general_clean(df)

        # Sheet-specific cleaning
        if sheet == 'globular clusters':
            df = epoch_convert(df)
        elif sheet == 'unnumbered minor planets':
            df = clean_unnumbered(df)
        
        # Write the cleaned DataFrame back to Excel
        df.to_excel(writer, sheet_name=sheet, index=False)
