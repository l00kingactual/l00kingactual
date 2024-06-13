import pandas as pd
import mysql.connector
from mysql.connector import Error
from mysql_credentials import db_config  # Importing db_config

# Read CSV files
exoplanets_df = pd.read_csv('data\\exoplants.csv')
largestgalaxies_df = pd.read_csv('data\\largestgalaxies.csv')

# Function to determine the MySQL data type
def determine_dtype(series):
    if series.dtype == 'object':
        if series.str.isnumeric().all():
            return 'INT'
        else:
            return 'VARCHAR(255)'
    elif series.dtype == 'int64':
        return 'INT'
    elif series.dtype == 'float64':
        return 'FLOAT'
    else:
        return 'VARCHAR(255)'

# Connect to MySQL database
try:
    connection = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create tables
    for df, table_name in [(exoplanets_df, 'exoplanets'), (largestgalaxies_df, 'largestgalaxies')]:
        columns = df.columns
        column_types = []
        for col in columns:
            dtype = determine_dtype(df[col])
            column_types.append(dtype)

        create_table_query = f"CREATE TABLE {table_name} ({', '.join([f'`{col}` {dtype}' for col, dtype in zip(columns, column_types)] )});"
        cursor.execute(create_table_query)
        print(f"Table {table_name} created successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
