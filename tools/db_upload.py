from sqlalchemy import create_engine, exc
import pandas as pd
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Import database configuration
from mysql_credentials import db_config

# Database connection using SQLAlchemy
try:
    engine = create_engine(f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}/{db_config['db_name']}")
    logging.info("Successfully connected to the database.")
except Exception as e:
    logging.error(f"Database connection failed: {e}")

# Read Excel file
try:
    with pd.ExcelFile('data\\cggc_nwas_database_cleaned.xlsx') as xls:
        logging.info("Successfully read the Excel file.")
        
        # Loop through each sheet in the Excel file
        for sheet_name in xls.sheet_names:
            try:
                # Read each sheet into a DataFrame
                df = pd.read_excel(xls, sheet_name)
                
                if df.empty:
                    logging.warning(f"DataFrame for sheet {sheet_name} is empty.")
                    continue
                
                # Log the state of the connection object
                logging.info(f"Connection object before to_sql: {engine}")
                
                # Save the DataFrame to the SQL database
                df.to_sql(sheet_name, engine, if_exists='replace', index=False)
                logging.info(f"Successfully processed sheet {sheet_name}.")
                
            except exc.SQLAlchemyError as e:
                logging.error(f"An SQLAlchemy error occurred while processing sheet {sheet_name}: {e}")
            except Exception as e:
                logging.error(f"An error occurred while processing sheet {sheet_name}: {e}")
                logging.debug(f"Exception type: {type(e)}")
                
except Exception as e:
    logging.error(f"Failed to read Excel file: {e}")
