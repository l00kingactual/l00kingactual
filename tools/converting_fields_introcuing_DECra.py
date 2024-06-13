import os
import pandas as pd
import MySQLdb
import re
from mysql_credentials import db_config

# desgien the function that will inspect the content of the csv file and if fields described similatar to Dec & RA to additional fields with their decimal version and RA in the same fashion. the data looks like this: Dec =  29 05 27 0 and RA =  00h 08m 23 17s

def convert_to_decimal(coord, coord_type):
    """
    Converts DMS (Degrees, Minutes, Seconds) or HMS (Hours, Minutes, Seconds) to decimal.
    
    Parameters:
        coord (str): The coordinate in DMS or HMS format.
        coord_type (str): Either 'Dec' for Declination or 'RA' for Right Ascension.
        
    Returns:
        float: The coordinate in decimal format.
    """
    elements = coord.split()
    
    if coord_type == 'Dec':
        degrees = float(elements[0])
        minutes = float(elements[1])
        seconds = float(elements[2])
        milliseconds = float(elements[3])
        decimal_value = degrees + (minutes / 60) + (seconds / 3600) + (milliseconds / 3600000)
        
    elif coord_type == 'RA':
        hours = float(elements[0][:-1])  # Remove 'h'
        minutes = float(elements[1][:-1])  # Remove 'm'
        seconds = float(elements[2])
        milliseconds = float(elements[3][:-1])  # Remove 's'
        decimal_value = 15 * (hours + (minutes / 60) + (seconds / 3600) + (milliseconds / 3600000))
        
    else:
        raise ValueError("Invalid coordinate type. Use 'Dec' for Declination or 'RA' for Right Ascension.")
        
    return decimal_value




def convertDatabse_main():
    db = MySQLdb.connect(host=db_config['host'], 
                         user=db_config['user'], 
                         passwd=db_config['password'], 
                         db=db_config['database'])
    cursor = db.cursor()

    input_directory = 'data\\'

    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(input_directory, filename)
            df = pd.read_csv(filepath)

            # Clean column names
            df.columns = clean_column_names(df.columns)

            # Determine data types and modify schema
            create_table_query = f"CREATE TABLE `{filename[:-4]}` ("
            for col in df.columns:
                dtype = 'TEXT'
                if df[col].dtype == 'int64':
                    dtype = 'INT'
                elif df[col].dtype == 'float64':
                    dtype = 'FLOAT'
                create_table_query += f"`{col}` {dtype}, "

            # Check for Declination and Right Ascension
            for col in df.columns:
                if re.search(r'declination|dec', col, re.I):
                    df['decimal_Dec'] = df[col].apply(convert_to_decimal)
                    create_table_query += "`decimal_Dec` FLOAT, "
                if re.search(r'right ascension|ra', col, re.I):
                    df['decimal_RA'] = df[col].apply(convert_to_decimal)
                    create_table_query += "`decimal_RA` FLOAT, "

            create_table_query = create_table_query[:-2] + ")"
            cursor.execute(f"DROP TABLE IF EXISTS `{filename[:-4]}`")
            cursor.execute(create_table_query)

            # Insert data (your existing logic here)

    db.commit()
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
