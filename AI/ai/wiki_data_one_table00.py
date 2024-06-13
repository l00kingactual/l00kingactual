import os
import pandas as pd

# Define the directory where the CSV files are located
csv_dir = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\csv_data\\wikiData'

# Initialize an empty list to hold the DataFrames
dfs = []

# Console log: Starting the process
print("Starting the process of amalgamating CSV files.")

# Loop through each file in the directory
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        # Console log: Reading a file
        print(f"Reading file: {filename}")
        
        # Construct the full path of the file
        filepath = os.path.join(csv_dir, filename)
        
        try:
            # Read the CSV file into a DataFrame, skipping bad lines
            df = pd.read_csv(filepath, on_bad_lines='skip')

            
            # Console log: File read successfully
            print(f"Successfully read file: {filename}")
            
            # Add a 'Source' column to indicate which file this data came from
            df['Source'] = filename
            
            # Console log: Adding source information
            print(f"Adding source information to DataFrame for file: {filename}")
            
            # Append the DataFrame to the list
            dfs.append(df)
            
            # Console log: DataFrame appended to list
            print(f"DataFrame for file {filename} appended to list.")
        except pd.errors.ParserError as e:
            print(f"ParserError: {e}. Skipping file: {filename}")

# Console log: Concatenating DataFrames
print("Concatenating all DataFrames into one.")

# Concatenate all the DataFrames into one
final_df = pd.concat(dfs, ignore_index=True)

# Console log: Concatenation complete
print("Concatenation complete.")

# Save the final DataFrame to a new CSV file
final_csv_path = os.path.join(csv_dir, 'amalgamated_table.csv')
final_df.to_csv(final_csv_path, index=False)

# Console log: Saving final DataFrame
print(f"Amalgamation complete. The combined table has been saved as 'amalgamated_table.csv' at {final_csv_path}.")
