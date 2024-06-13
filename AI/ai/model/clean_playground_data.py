import os
import glob
import pandas as pd
import read_files  # Assuming read_files.py contains your read functions
import write_files  # Assuming write_files.py contains your write functions
# Define input and output directories
input_dir = 'training_data'
output_dir = 'training_data\\cleaned'

# Initialize a dictionary to hold DataFrames
dfs_dict = {}

# Debug: Print the list of files in the input directory
print(f"Files in input directory: {os.listdir(input_dir)}")

# Loop through each file in the input directory
for file_path in glob.glob(os.path.join(input_dir, '*')):  # This will match all files
    try:
        print(f"Processing file: {file_path}")

        # Determine file type
        file_extension = os.path.splitext(file_path)[1][1:]

        # Debug: Print the detected file extension
        print(f"Detected file extension: {file_extension}")

        # Read file based on its type
        if file_extension == 'csv':
            df = read_files.read_csv(file_path)
        elif file_extension == 'txt':
            df = read_files.read_txt(file_path)
        elif file_extension == 'md':
            df = read_files.read_md(file_path)
        elif file_extension == 'docx':
            df = read_files.read_word(file_path)
        elif file_extension == 'xlsx':
            df = read_files.read_excel(file_path)
        elif file_extension == 'html':
            df = read_files.read_html(file_path)
        else:
            print(f"Unsupported file type: {file_extension}")
            continue

        # Debug: Print the first few rows of the DataFrame
        if isinstance(df, pd.DataFrame):
            print(df.head())

                # Perform data cleaning here
        print("Cleaning data.")
        if isinstance(df, pd.DataFrame) and 'A' in df.columns:
            df.dropna(subset=['A'], inplace=True)

        # Write cleaned data to CSV
        output_file_path = os.path.join(output_dir, os.path.basename(file_path))
        write_files.write_csv(df, output_file_path)

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")

print("Data cleaning process completed.")
