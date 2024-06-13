import pandas as pd
import re
from openpyxl.utils.exceptions import InvalidFileException

def ensure_string(value):
    if pd.isna(value):
        return ''
    else:
        return str(value)

def sexagesimal_to_decimal(ra, dec):
    ra = ensure_string(ra)
    dec = ensure_string(dec)
    ra_match = re.match(r'(\d+)h (\d+)m ([\d.]+)s', ra)
    dec_match = re.match(r'([+-]?\d+)[^\d]+(\d+)[^\d]+(\d+)', dec)
    if ra_match:
        ra_hours = int(ra_match.group(1))
        ra_minutes = int(ra_match.group(2))
        ra_seconds = float(ra_match.group(3))
        ra_decimal = ra_hours + ra_minutes / 60 + ra_seconds / 3600
    else:
        ra_decimal = None
    if dec_match:
        dec_degrees = int(dec_match.group(1))
        dec_arcminutes = int(dec_match.group(2))
        dec_arcseconds = int(dec_match.group(3))
        dec_decimal = abs(dec_degrees) + dec_arcminutes / 60 + dec_arcseconds / 3600
        dec_decimal = dec_decimal if dec_degrees >= 0 else -dec_decimal
    else:
        dec_decimal = None
    return ra_decimal, dec_decimal

def format_sexagesimal(ra_decimal, dec_decimal):
    def decimal_to_sexagesimal(value, is_ra=False):
        if pd.isna(value):
            return None, None, None
        degrees = int(value)
        minutes = int((value - degrees) * 60)
        seconds = (value - degrees - minutes / 60) * 3600
        if is_ra:
            hours = degrees / 15
            return int(hours), int(minutes), seconds
        else:
            return degrees, minutes, seconds
    if ra_decimal and not pd.isna(ra_decimal):
        ra_hours, ra_minutes, ra_seconds = decimal_to_sexagesimal(ra_decimal, is_ra=True)
        ra_sexagesimal = f"{ra_hours}h {ra_minutes}m {ra_seconds:.3f}s"
    else:
        ra_sexagesimal = None
    if dec_decimal and not pd.isna(dec_decimal):
        dec_degrees, dec_minutes, dec_seconds = decimal_to_sexagesimal(dec_decimal)
        dec_sexagesimal = f"{dec_degrees}° {dec_minutes}' {dec_seconds:.3f}\""
    else:
        dec_sexagesimal = None
    return ra_sexagesimal, dec_sexagesimal

def process_excel_file(input_file_path, output_file_path):
    try:
        workbook = pd.ExcelFile(input_file_path)
        all_data = []
        for sheet_name in workbook.sheet_names:
            sheet_data = pd.read_excel(workbook, sheet_name=sheet_name)
            if 'RA' in sheet_data.columns and 'Declination' in sheet_data.columns:
                sheet_data[['RA_decimal', 'Dec_decimal']] = sheet_data.apply(
                    lambda row: pd.Series(sexagesimal_to_decimal(row['RA'], row['Declination'])), axis=1)
                sheet_data[['RA_sexagesimal', 'Dec_sexagesimal']] = sheet_data.apply(
                    lambda row: pd.Series(format_sexagesimal(row['RA_decimal'], row['Dec_decimal'])), axis=1)
                all_data.append(sheet_data)
        combined_data = pd.concat(all_data, ignore_index=True)
        sorted_combined_data = combined_data.sort_values(by=['RA_decimal', 'Dec_decimal'])
        sorted_combined_data.to_excel(output_file_path, index=False)
        print(f"Processed file saved to {output_file_path}")
    except InvalidFileException as e:
        print(f"Error reading the Excel file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace 'path_to_input_excel_file.xlsx' with the path to the Excel file to be processed.
# Replace 'path_to_output_excel_file.xlsx' with the path where the output Excel file should be saved.
process_excel_file('path_to_input_excel_file.xlsx', 'path_to_output_excel_file.xlsx')
