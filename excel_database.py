import os
import pandas as pd

# Get a list of Excel files in the current directory
excel_files = [file for file in os.listdir() if file.endswith('.xlsx')]

# Initialize an empty list to store DataFrames
dataframes = []

# Iterate over each Excel file and read its data into a DataFrame
for file in excel_files:
    try:
        df = pd.read_excel(file)  # Read the Excel file into a DataFrame
        dataframes.append(df)  # Append the DataFrame to the list
        print(f"Read data from {file}")
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Concatenate the list of DataFrames into one combined DataFrame
combined_data = pd.concat(dataframes, ignore_index=True)

# Create a new Excel workbook and write the combined data to it
output_file = "database.xlsx"
with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
    combined_data.to_excel(writer, sheet_name='Combined_Data', index=False)
    print(f"Saved combined data to {output_file} as a new sheet")

print("Process completed.")
