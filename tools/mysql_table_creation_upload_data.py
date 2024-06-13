import pandas as pd
import MySQLdb
import json
import logging
import hashlib
import re

# Initialize logging
logging.basicConfig(filename='database_log.json', level=logging.INFO, format='%(asctime)s %(message)s')

# Load MySQL credentials
with open('mysql_credentials.json', 'r') as f:
    db_config = json.load(f)

# Custom serializer for JSON
def custom_serializer(obj):
    if isinstance(obj, pd.DataFrame):
        return obj.to_dict()
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

# Initialize exceptions dictionary
exceptions_dict = {}

# Initialize a dictionary to keep track of column names
column_names = {}

# Define the excel_file_path
excel_file_path = "data\\cggc_nwas_database_cleaned.xlsx"

# Define a function to determine data type (this is just a placeholder)
def determine_data_type(column):
    """
    Determine the SQL data type for a given pandas Series.
    """
    # Check for datetime
    if pd.api.types.is_datetime64_any_dtype(column):
        return "DATETIME"
    
    # Check for boolean
    if pd.api.types.is_bool_dtype(column):
        return "BOOLEAN"
    
    # Check for integer
    if pd.api.types.is_integer_dtype(column):
        return "INT"
    
    # Check for float
    if pd.api.types.is_float_dtype(column):
        return "FLOAT"
    
    # Check for object or string
    if pd.api.types.is_object_dtype(column):
        # Further logic to differentiate between plain strings and potential JSON objects, etc.
        return "TEXT"
    
    # Default to TEXT
    return "TEXT"

try:
    # Connect to MySQL database
    conn = MySQLdb.connect(host=db_config['host'], user=db_config['user'], passwd=db_config['passwd'], db=db_config['db'])
    cursor = conn.cursor()

    # Drop all tables (Caution: This will remove all data)
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        try:
            cursor.execute(f"DROP TABLE {table[0]}")
            logging.info(f"Successfully dropped table {table[0]}")
        except MySQLdb.Error as e:
            logging.error(f"Couldn't drop table {table[0]}. Error: {str(e)}")





    # Read Excel workbook
    xls = pd.ExcelFile('data\\cggc_nwas_database_cleaned.xlsx')
    for sheet_name in xls.sheet_names:
        logging.info(f"Reading sheet {sheet_name}")
        print(f"Reading sheet {sheet_name}")  # Console output
        df = pd.read_excel(xls, sheet_name)

        # Create table query
        create_table_query = f"CREATE TABLE `{sheet_name}` ("
        column_names = {}
        for col in df.columns:
            sanitized_col = col.replace(" ", "_")
            if len(sanitized_col) > 64:
                sanitized_col = hashlib.md5(sanitized_col.encode()).hexdigest()[:10]




            xls = pd.ExcelFile(excel_file_path)  # Assuming you read the Excel file into a variable called xls

            for sheet_name in xls.sheet_names:
                df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
                
                # Create table query
                create_table_query = f"CREATE TABLE `{sheet_name}` ("
                
                for col in df.columns:
                    # Sanitize column names
                    sanitized_col = re.sub(r'\W+', '', col).replace(" ", "_")
                    
                    # Handle duplicate column names by appending '_num'
                    if sanitized_col in column_names:
                        sanitized_col += "_num"
                    
                    column_names[sanitized_col] = True  # Mark this column name as used
                    
                    # Determine data type
                    data_type = determine_data_type(df[col])
                    
                    create_table_query += f"{sanitized_col} {data_type}, "
                
                create_table_query = create_table_query.rstrip(", ") + ");"
                
                try:
                    cursor.execute(create_table_query)
                    logging.info(f"Successfully created table for sheet {sheet_name}")
                except Exception as e:
                    logging.error(f"An error occurred: {e}")




except Exception as e:
    logging.error(f"An error occurred: {e}")
    print(f"An error occurred: {e}")  # Console output
    with open('database_exceptions.json', 'w') as f:
        json.dump({"main_function": str(e)}, f)


finally:
    # Close MySQL connection
    if conn:
        conn.close()
