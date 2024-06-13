from collections import defaultdict
import os
import pandas as pd
import MySQLdb

# Import database credentials from mysql_credentials.py
from mysql_credentials import db_config

def clean_column_names(columns):
    """Clean column names by removing special characters."""
    return [col.replace('[', '').replace(']', '').replace('*', '') for col in columns]

def create_meta_data_frame(cursor):
    """Create a DataFrame containing meta-data about database tables."""
    meta_data = []
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
        cursor.execute(f"DESCRIBE {table[0]}")
        columns = cursor.fetchall()
        for column in columns:
            meta_data.append({
                'Table': table[0],
                'Field': column[0],
                'Type': column[1],
                'Null': column[2],
                'Key': column[3],
                'Default': column[4],
                'Extra': column[5]
            })
    meta_data_df = pd.DataFrame(meta_data)
    meta_data_df.to_csv('meta_data.csv', index=False)

def identify_common_fields(meta_data_df):
    """Identify common fields across tables."""
    common_fields = meta_data_df['Field'].value_counts()
    common_fields = common_fields[common_fields > 1]
    return common_fields

def check_data_integrity(df, common_fields):
    """Check data integrity for common fields."""
    for field in common_fields.index:
        if field in df.columns:
            # Perform your data integrity checks here
            pass

def main():
    # Initialize a dictionary to hold grouped errors
    error_dict = defaultdict(list)

    # Connect to MySQL database using credentials from mysql_credentials.py
    db = MySQLdb.connect(host=db_config['host'], 
                         user=db_config['user'], 
                         passwd=db_config['password'], 
                         db=db_config['database'])
    cursor = db.cursor()

    # Create meta-data DataFrame
    create_meta_data_frame(cursor)

    # Identify common fields
    meta_data_df = pd.read_csv('meta_data.csv')
    common_fields = identify_common_fields(meta_data_df)

    # Directory containing cleaned CSV files
    input_directory = 'data\\'

    # Loop through each CSV file in the directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            try:
                # Read CSV file into a DataFrame
                filepath = os.path.join(input_directory, filename)
                df = pd.read_csv(filepath)

                # Clean column names
                df.columns = clean_column_names(df.columns)

                # Check data integrity for common fields
                check_data_integrity(df, common_fields)

                # Drop existing table
                table_name = filename[:-4]
                cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`")

                # Create table
                create_table_query = f"CREATE TABLE `{table_name}` ("
                for col in df.columns:
                    create_table_query += f"`{col}` TEXT, "
                create_table_query = create_table_query[:-2] + ")"
                
                print(f"Executing SQL: {create_table_query}")  # Debugging line
                cursor.execute(create_table_query)

                # Insert data into table
                for index, row in df.iterrows():
                    insert_query = f"INSERT INTO `{table_name}` VALUES ("
                    for col in df.columns:
                        value = str(row[col]).replace("'", "\\'")  # Escape single quotes
                        insert_query += f"'{value}', "
                    insert_query = insert_query[:-2] + ")"
                    cursor.execute(insert_query)

                print(f"Created table and inserted data for {table_name}.")

            except MySQLdb.MySQLError as e:
                error_message = str(e)
                print(f"An SQL error occurred while processing {filename}: {error_message}")
                error_dict[error_message].append(filename)
                
            except Exception as e:
                error_message = str(e)
                print(f"An error occurred while processing {filename}: {error_message}")
                error_dict[error_message].append(filename)

    # Commit changes and close connection
    db.commit()
    cursor.close()
    db.close()

    # Write grouped errors to errors.txt
    with open("errors.txt", "w") as f:
        for error, files in error_dict.items():
            f.write(f"Error: {error}\nFiles:\n")
            for file in files:
                f.write(f"  - {file}\n")
            f.write("\n")

if __name__ == "__main__":
    main()