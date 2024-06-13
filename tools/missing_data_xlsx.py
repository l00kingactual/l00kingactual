import pandas as pd

def clean_data(df):
    # Add data cleaning logic here
    # E.g., Remove NaN or replace them
    df.fillna("Unknown", inplace=True)
    
    # Additional cleaning logic can be placed here
    return df

    
# Clean the data
def clean_data(df):
    # Remove substrings "[edit]" and "[num]"
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = df[column].str.replace(r"\[edit\]", "", regex=True)
            df[column] = df[column].str.replace(r"\[num\]", "", regex=True)
    
    # Remove rows consisting only of whitespace or NaN
    df.replace(r'^\s*$', pd.NA, regex=True, inplace=True)
    df.dropna(how='all', inplace=True)
    
    return df

def main():
    input_file = 'wikipedia\\missing data.xlsx'
    output_file = 'wikipedia\\cleaned_missing_data.xlsx'
    
    # Reading Excel file and iterating through each sheet
    try:
        xls = pd.ExcelFile(input_file, engine='openpyxl')
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(input_file, sheet_name=sheet_name, engine='openpyxl')
            
            # Clean the data
            cleaned_df = clean_data(df)
            
            # Display first 5 rows of cleaned data for each sheet
            print(f"First 5 rows of cleaned data for sheet '{sheet_name}':")
            print(cleaned_df.head())
            
            # Write the cleaned DataFrame back to the Excel file, sheet by sheet
            cleaned_df.to_excel(writer, sheet_name=sheet_name, index=False)

if __name__ == '__main__':
    main()

