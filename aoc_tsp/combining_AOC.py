import os

def combine_py_files(directory, output_file):
    """
    Combines all .py files in the specified directory into a single file.

    Parameters:
    directory (str): The directory containing the .py files.
    output_file (str): The path to the output file where the combined content will be saved.
    """
    combined_content = ""
    
    # Walk through the directory and read all .py files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    combined_content += f"\n# File: {file}\n"
                    combined_content += f.read()
                    combined_content += "\n"  # Add a newline between files for readability
    
    # Save the combined content into the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_content)
    print(f"Combined file created at: {output_file}")

# Specify the directory and output file
directory = r"C:\Users\actua\OneDrive\masters\CO7315_Bio_inspired_computing\python_code\AOC"
output_file = r"C:\Users\actua\OneDrive\masters\CO7315_Bio_inspired_computing\python_code\AOC\combined_aoc_code.py"

# Combine the .py files
combine_py_files(directory, output_file)
