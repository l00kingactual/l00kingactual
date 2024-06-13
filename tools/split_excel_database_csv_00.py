import os
import pandas as pd

# Define the directory and file paths
input_directory = "data"
output_directory = "data\\database_csv"
input_file = "database.xlsx"

# Create the output directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Load the Excel workbook
xls_path = os.path.join(input_directory, input_file)
xls = pd.ExcelFile(xls_path)

# Loop through each sheet in the workbook
for sheet_name in xls.sheet_names:
    # Read the sheet into a DataFrame
    df = pd.read_excel(xls, sheet_name)
    
    # Define the output CSV file path
    csv_file = f"{sheet_name}.csv"
    csv_path = os.path.join(output_directory, csv_file)
    
    # Save the DataFrame as a CSV file
    df.to_csv(csv_path, index=False)

print("Excel sheets have been successfully converted to CSV files.")
