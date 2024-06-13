import os
import re
import pandas as pd
import logging

logging.basicConfig(filename='database_cleaning.log', level=logging.ERROR)

def clean_column_names(columns):
    # Remove special characters and make the string SQL-friendly
    return [re.sub('[^0-9a-zA-Z]+', '_', col)[:64] for col in columns]

def clean_dataframe(df):
    # Clean column names
    df.columns = clean_column_names(df.columns)
    # Remove special characters from string-type columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace('[^0-9a-zA-Z]+', ' ', regex=True)
    return df

def main():
    input_directory = 'data\\cleaned\\database\\'
    output_directory = 'data\\cleaned\\database_cleaned\\'

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.csv'):
            try:
                filepath = os.path.join(input_directory, filename)
                df = pd.read_csv(filepath)
                df_cleaned = clean_dataframe(df)
                output_filepath = os.path.join(output_directory, filename)
                df_cleaned.to_csv(output_filepath, index=False)
                print(f"Cleaned and saved {filename}")
            except Exception as e:
                logging.error(f"An error occurred while processing {filename}: {str(e)}")

if __name__ == "__main__":
    main()
