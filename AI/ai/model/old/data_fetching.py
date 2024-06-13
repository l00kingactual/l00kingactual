from common_imports import *


# Function to read Markdown files
def read_md_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Function to read CSV files
def read_csv_file(file_path):
    return pd.read_csv(file_path)

# Function to read Text files
def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

# Function to read HTML files
def read_html_file(file_path):
    with open(file_path, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
        return soup.prettify()

# Function to dynamically read files based on their extensions
def read_file(file_path):
    """
    Reads a file based on its extension and returns its content.
    
    Parameters:
    file_path (str): The path to the file.
    
    Returns:
    Various: Content of the file, type depends on file extension.
    """
    _, file_extension = os.path.splitext(file_path)
    
    if file_extension == '.md':
        return read_md_file(file_path)
    elif file_extension == '.csv':
        return read_csv_file(file_path)
    elif file_extension == '.txt':
        return read_txt_file(file_path)
    elif file_extension == '.html':
        return read_html_file(file_path)
    else:
        print(f"Unsupported file extension: {file_extension}")
        return None

def fetch_or_create_data(memory):
    # Your logic to fetch or create data
    train_df = ...
    test_df = ...
    return train_df, test_df


import os
import pandas as pd
from sklearn.model_selection import train_test_split

def list_data_files(folder_path):
    """
    List all data files in the specified folder.
    
    Parameters:
    folder_path (str): The path to the folder.
    
    Returns:
    list: List of file names in the folder.
    """
    return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def update_data(folder_path='data'):
    data_files = list_data_files(folder_path)
    data_content = {}
    
    for file in data_files:
        full_path = os.path.join(folder_path, file)
        data_content[file] = pd.read_csv(full_path)  # Assuming the files are CSVs
    
    return data_content

def fetch_or_create_data(memory):
    """
    Fetch or create training and testing dataframes.
    
    Parameters:
    memory (dict): The memory dictionary.
    
    Returns:
    tuple: Training and testing dataframes.
    """
    if 'train_df' in memory and 'test_df' in memory:
        train_df = pd.DataFrame(memory['train_df'])
        test_df = pd.DataFrame(memory['test_df'])
    else:
        data_content = update_data()
        # Combine data_content into a single dataframe (if needed)
        combined_df = pd.concat(data_content.values(), ignore_index=True)
        
        # Split the data into training and testing sets
        train_df, test_df = train_test_split(combined_df, test_size=0.2)
        
        # Update memory
        memory['train_df'] = train_df.to_dict()
        memory['test_df'] = test_df.to_dict()
    
    return train_df, test_df



