import os
import pandas as pd
import pymysql
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Database connection
def connect_to_db():
    logging.info("Connecting to the database.")
    return pymysql.connect(
        host='213.171.200.30',
        user='OuchAstronomy',
        password='@00E54m1sf1t?',
        database='ouchAstronomy'
    )

# Connect to MySQL database
conn = connect_to_db()
cursor = conn.cursor()

# Directory containing CSV files
csv_dir = r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\csv_data"

# Iterate through each CSV file in the directory
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        filepath = os.path.join(csv_dir, filename)
        table_name = filename.replace('.csv', '')
        
        logging.info(f"Processing CSV file: {filename}")
        
        # Read CSV into a DataFrame
        df = pd.read_csv(filepath)
        
        # Clean column names
        df.columns = df.columns.str.replace(r"[^a-zA-Z0-9]", "_")
        
        # Drop existing table data
        logging.info(f"Dropping existing data in table: {table_name}")
        try:
            cursor.execute(f"TRUNCATE TABLE `{table_name}`")
        except Exception as e:
            logging.warning(f"Table {table_name} does not exist or could not be truncated: {e}")
        
        # Replace NaN values with None
        df.where(pd.notna(df), None, inplace=True)
        

        # Dynamically generate column data types based on DataFrame dtypes
        column_types = []
        for col, dtype in df.dtypes.items():
            if dtype == 'object':
                column_types.append(f"`{col}` TEXT")
            elif dtype == 'int64':
                column_types.append(f"`{col}` INT")
            elif dtype == 'float64':
                column_types.append(f"`{col}` FLOAT")
            else:
                column_types.append(f"`{col}` TEXT")
        
        # Alter table structure to fit data
        alter_query = f"ALTER TABLE `{table_name}` MODIFY COLUMN {', MODIFY COLUMN '.join(column_types)}"
        logging.info(f"Altering table structure: {alter_query}")
        try:
            cursor.execute(alter_query)
        except Exception as e:
            logging.error(f"An error occurred while altering table {table_name}: {e}")
            continue
        
        # Insert data into table
        logging.info(f"Inserting data into table: {table_name}")
        for i, row in df.iterrows():
            columns_str = ", ".join([f"`{col}`" for col in df.columns])
            values_str = ", ".join(["%s"] * len(df.columns))
            sql_query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({values_str})"
            
            try:
                cursor.execute(sql_query, tuple(row))
            except Exception as e:
                logging.error(f"An error occurred while inserting data into {table_name}: {e}")
        
        # Commit changes
        logging.info(f"Committing changes for table: {table_name}")
        conn.commit()

# Close the cursor and connection
logging.info("Closing the cursor and database connection.")
cursor.close()
conn.close()
