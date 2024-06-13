import os
import pandas as pd

# Define the directory where the CSV files are located
csv_dir = 'C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\csv_data\\wikiData'

# Initialize an empty list to hold the DataFrames
dfs = []

# Loop through each file in the directory
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        # Construct the full path of the file
        filepath = os.path.join(csv_dir, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)
        
        # Add a 'Source' column to indicate which file this data came from
        df['Source'] = filename
        
        # Append the DataFrame to the list
        dfs.append(df)

# Concatenate all the DataFrames into one
final_df = pd.concat(dfs, ignore_index=True)

# Save the final DataFrame to a new CSV file
final_df.to_csv(os.path.join(csv_dir, 'amalgamated_table.csv'), index=False)

print("Amalgamation complete. The combined table has been saved as 'amalgamated_table.csv'.")
