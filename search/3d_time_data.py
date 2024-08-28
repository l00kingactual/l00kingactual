import os
import glob
import json
import pandas as pd
from datetime import datetime

# Define the required keys for the JSON data
required_keys = {'r2', 'kappa', 'logloss', 'precision', 'accuracy', 'balanced_acc', 'jaccard', 'mcc', 'mae', 'mse', 'f1', 'recall'}

def check_missing_keys(data, required_keys):
    """
    Check for missing keys in the JSON data and log warnings if any are missing.
    """
    missing_keys = required_keys - data.keys()
    if missing_keys:
        print(f"Missing keys in JSON data: {missing_keys}")
    return missing_keys

def load_json_file(file_path, required_keys):
    """
    Load JSON file, handle errors, and check for missing keys.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        # If data is a list, assume it's a list of dictionaries and take the first element
        if isinstance(data, list):
            data = data[0] if data else {}
        missing_keys = check_missing_keys(data, required_keys)
        if missing_keys:
            for key in missing_keys:
                data[key] = None  # Setting default value as None for missing keys
        # Add file creation time as 'time'
        data['time'] = datetime.fromtimestamp(os.path.getctime(file_path)).isoformat()
        return data
    except json.JSONDecodeError as e:
        print(f'Error reading JSON file {file_path}: {e}')
        return None

def clean_and_combine_json_files(root_dir, required_keys):
    """
    Read and clean all JSON files in the directory and subdirectories, then combine them into a single DataFrame.
    """
    file_paths = glob.glob(os.path.join(root_dir, '**/*.json'), recursive=True)
    data_list = []

    for file_path in file_paths:
        data = load_json_file(file_path, required_keys)
        if data:
            data_list.append(data)

    if not data_list:
        print("No valid data found.")
        return pd.DataFrame(columns=list(required_keys) + ['time'])

    combined_df = pd.DataFrame(data_list)
    combined_df = combined_df.dropna(subset=required_keys, how='all')

    return combined_df

def save_dataframe_to_json(df, output_dir):
    """
    Save the DataFrame to a JSON file with the current datetime in the filename.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_file_path = os.path.join(output_dir, f'3d_time_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    df.to_json(output_file_path, orient='records', lines=True)
    print(f"DataFrame saved to {output_file_path}")

# Main script execution
root_dir = 'analysis'
output_dir = 'analysis'
combined_df = clean_and_combine_json_files(root_dir, required_keys)
save_dataframe_to_json(combined_df, output_dir)

combined_df.head()  # Display the head of the combined DataFrame for inspection
