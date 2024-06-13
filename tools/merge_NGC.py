import os
import pandas as pd

# Initialize an empty DataFrame to hold all the data
all_data_df = pd.DataFrame()

# Directory containing the CSV files
input_dir = "data\\cleaned"

# Loop through the range of NGC objects
for start in range(1, 8001, 1000):
    end = start + 999
    if end > 7840:
        end = 7840  # The last file goes up to 7840
    filename = f"List_of_NGC_objects_({start}-{end}).csv"
    filepath = os.path.join(input_dir, filename)

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(filepath)
        
        # Append the DataFrame to the main DataFrame
        all_data_df = pd.concat([all_data_df, df], ignore_index=True)

    except Exception as e:
        print(f"An error occurred while reading {filename}: {e}")

# Write the combined data to a new CSV file
output_filepath = os.path.join(input_dir, "List_of_all_NGC_objects.csv")
try:
    all_data_df.to_csv(output_filepath, index=False)
    print(f"Combined data written to {output_filepath}.")
except Exception as e:
    print(f"An error occurred while writing the combined CSV file: {e}")
