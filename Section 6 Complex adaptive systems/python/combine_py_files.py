import os
import json

def read_py_files(directory):
    data = {}
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                folder_name = os.path.basename(root)
                key = f"{folder_name}/{file_name}"
                with open(file_path, 'r') as f:
                    data[key] = f.read()
    return data

def main():
    directory = r'C:\Users\actua\OneDrive\masters\CO7315_Bio_inspired_computing\python_code\week02_05'
    combined_data = read_py_files(directory)
    output_file = 'combined_py_files.json'
    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=4)
    print(f'Combined data saved to {output_file}')

if __name__ == "__main__":
    main()
