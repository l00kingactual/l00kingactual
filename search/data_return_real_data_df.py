import os
import pandas as pd
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_random_real_world_data(directory, target_size_mb=250, seed=12345):
    """Load and combine random CSV files from a directory until the combined size reaches the target size."""
    random.seed(seed)
    
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv') and not f.endswith('_1.csv')]
    
    random.shuffle(files)
    logging.info(f"Found {len(files)} CSV files (excluding '_1.csv' files). Files are shuffled randomly.")

    combined_df = pd.DataFrame()
    total_size = 0
    
    for file in files:
        try:
            df = pd.read_csv(file, encoding='utf-8', on_bad_lines='skip')
            logging.info(f"Successfully read file {file} with UTF-8 encoding.")
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(file, encoding='ISO-8859-1', on_bad_lines='skip')
                logging.info(f"Successfully read file {file} with ISO-8859-1 encoding.")
            except UnicodeDecodeError:
                logging.warning(f"Skipping file due to encoding issues: {file}")
                continue
        except pd.errors.ParserError as e:
            logging.warning(f"Parsing error in file {file}: {e}")
            continue
        
        # Handle NaN, null, and None values: Replace with 0 for numeric columns, and empty strings for object columns
        for col in df.select_dtypes(include=['object']).columns:
            df[col].fillna('', inplace=True)
        df.fillna(0, inplace=True)  # Numeric columns
        
        file_size_mb = os.path.getsize(file) / (1024 * 1024)
        total_size += file_size_mb
        combined_df = pd.concat([combined_df, df], ignore_index=True)
        
        logging.info(f"Added file {file} ({file_size_mb:.2f} MB) to DataFrame. Total size so far: {total_size:.2f} MB")
        
        if total_size >= target_size_mb:
            logging.info("Reached the target DataFrame size.")
            break
    
    combined_df.drop_duplicates(inplace=True)
    logging.info(f"Final DataFrame shape: {combined_df.shape}")
    
    summarize_data(combined_df)
    
    return combined_df

def summarize_data(df):
    """Provide a quick summary of the DataFrame."""
    logging.info("Summarizing DataFrame...")

    # Display basic information
    logging.info(f"DataFrame shape: {df.shape}")
    logging.info(f"Data types:\n{df.dtypes.value_counts()}")
    
    # Display summary statistics
    logging.info(f"Summary statistics:\n{df.describe(include='all').transpose()}")

    # Display the first few rows of the DataFrame
    logging.info(f"First few rows of the DataFrame:\n{df.head()}")

# Usage Example
data_directory = "H:/AI_ML/astronomyMLDatasets/"
combined_df = load_random_real_world_data(data_directory)

logging.info("Data loading and summary completed.")
