import os

def convert_py_to_text(directory, output_file):
    # Create a list of .py files in the specified directory
    py_files = [file for file in os.listdir(directory) if file.endswith('.py')]
    
    # Check if the list is empty
    if not py_files:
        print("No Python files found in the directory.")
        return

    # Open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Loop through each file
        for file in py_files:
            # Print the file being processed (for debugging)
            print(f"Processing file: {file}")
            # Open each .py file in read mode
            with open(os.path.join(directory, file), 'r') as infile:
                # Write the name of the file as a header
                outfile.write(f"\n\n# File: {file}\n")
                # Read the content of the file and write it to the output file
                content = infile.read()
                outfile.write(content)

# Make sure to replace 'path/to/directory' with the actual path to your Python files directory
convert_py_to_text('\\', 'combined.txt')
