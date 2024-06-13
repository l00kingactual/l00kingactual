import os
import pandas as pd
import glob

# Step 1: Read all CSV files into a dictionary
all_data = {}
input_dir = "training_data"
for file_path in glob.glob(os.path.join(input_dir, "*.csv")):
    file_name = os.path.basename(file_path).split('.')[0]
    try:
        print(f"Reading CSV file: {file_name}")
        all_data[file_name] = pd.read_csv(file_path)
    except Exception as e:
        print(f"An error occurred while reading {file_name}: {e}")

# Step 2: Amalgamate tables
amalgamated_data = {}
for key in all_data.keys():
    base_key = key.split('_table_')[0]
    if base_key not in amalgamated_data:
        amalgamated_data[base_key] = []
    amalgamated_data[base_key].append(all_data[key])

for key, dfs in amalgamated_data.items():
    try:
        amalgamated_data[key] = pd.concat(dfs, ignore_index=True)
    except Exception as e:
        print(f"An error occurred while amalgamating {key}: {e}")

# Step 3: Clean data
for key, df in amalgamated_data.items():
    try:
        print(f"Cleaning data for {key}")

        # Remove duplicates
        print("Removing duplicate rows.")
        df.drop_duplicates(inplace=True)

        # Remove footer rows (assuming footer contains the word 'Total')
        if 'Total' in df.values:
            print("Removing footer rows.")
            df = df.loc[~df.isin(['Total']).any(axis=1)]

        # Update the cleaned DataFrame back into the dictionary
        amalgamated_data[key] = df

        print(f"Data cleaning for {key} completed successfully.")
    except Exception as e:
        print(f"An error occurred while cleaning data for {key}: {e}")

# Step 4: Write cleaned data to CSV
output_dir = "training_data/cleaned"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for key, df in amalgamated_data.items():
    try:
        output_file_path = os.path.join(output_dir, f"{key}.csv")
        df.to_csv(output_file_path, index=False)
        print(f"Cleaned data for {key} written to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while writing cleaned data for {key}: {e}")
