import os
import pandas as pd

def identify_empty_tables(data_path):
    empty_tables = []
    for filename in os.listdir(data_path):
        if filename.endswith('.csv'):
            filepath = os.path.join(data_path, filename)
            df = pd.read_csv(filepath)
            if df.empty:
                empty_tables.append(filename[:-4])  # Remove '.csv' from filename
    return empty_tables

def find_urls_for_empty_tables(empty_tables, wikipedia_path):
    urls = {}
    for table in empty_tables:
        try:
            with open(os.path.join(wikipedia_path, f"{table}.txt"), 'r') as f:
                url = f.readline().strip()  # Assuming the URL is the first line in the text file
                urls[table] = url
        except FileNotFoundError:
            print(f"No Wikipedia data found for table {table}")
    return urls

def write_urls_to_file(urls, output_path):
    with open(output_path, 'w') as f:
        for table, url in urls.items():
            f.write(f"{table}: {url}\n")

if __name__ == "__main__":
    data_path = 'data\\'
    wikipedia_path = 'wikipedia\\'
    output_path = 'no_data.txt'

    empty_tables = identify_empty_tables(data_path)
    urls = find_urls_for_empty_tables(empty_tables, wikipedia_path)
    write_urls_to_file(urls, output_path)
