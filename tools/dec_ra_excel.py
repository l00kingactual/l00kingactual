import pandas as pd
import logging

# Initialize logging
logging.basicConfig(filename='excel_processing.log', level=logging.INFO, format='%(asctime)s %(message)s')

input_excel_path = 'data\\new_data_RAW.xlsx'
output_excel_path = 'data\\new_data_dec_ra.xlsx'

# Initialize Excel writer
try:
    writer = pd.ExcelWriter(output_excel_path, engine='openpyxl')
except Exception as init_error:
    logging.error(f"An error occurred while initializing the Excel writer: {init_error}")
    print(f"An error occurred while initializing the Excel writer: {init_error}")
    exit(1)  # Exit the program

# Read the Excel workbook
try:
    xls = pd.ExcelFile(input_excel_path)
except Exception as read_error:
    logging.error(f"An error occurred while reading the Excel file: {read_error}")
    print(f"An error occurred while reading the Excel file: {read_error}")
    exit(1)  # Exit the program

# Loop through each sheet in the workbook
for sheet_name in xls.sheet_names:
    try:
        logging.info(f"Reading sheet {sheet_name}")
        print(f"Reading sheet {sheet_name}")

        # Read the sheet into a DataFrame
        df = pd.read_excel(input_excel_path, sheet_name=sheet_name)

        # Check if RAHour, RAMinute, DecSign, DecDeg, DecMinute exist in the DataFrame
        if all(col in df.columns for col in ['RAHour', 'RAMinute', 'DecSign', 'DecDeg', 'DecMinute']):
            logging.info(f"Calculating ra_decimal and dec_decimal for sheet {sheet_name}")
            print(f"Calculating ra_decimal and dec_decimal for sheet {sheet_name}")

            # Calculate decimal RA
            df['ra_decimal'] = df['RAHour'] + df['RAMinute'] / 60.0

            # Calculate decimal Dec
            df['dec_decimal'] = df['DecDeg'] + df['DecMinute'] / 60.0
            df['dec_decimal'] = df['dec_decimal'] * df['DecSign'].apply(lambda x: -1 if x == '-' else 1)

            # Write the modified DataFrame back to Excel
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    except Exception as sheet_error:
        logging.error(f"An error occurred while processing sheet {sheet_name}: {sheet_error}")
        print(f"An error occurred while processing sheet {sheet_name}: {sheet_error}")

# Save the modified Excel workbook
try:
    writer.save()
except Exception as save_error:
    logging.error(f"An error occurred while saving the workbook: {save_error}")
    print(f"An error occurred while saving the workbook: {save_error}")

logging.info("Successfully completed all tasks.")
print("Successfully completed all tasks.")
