import os
import pandas as pd

def remove_bracketed_star(dataframe):
    # Use regex to remove '[*]' from all DataFrame elements
    return dataframe.replace(to_replace='\[\*\]', value='', regex=True)

def main():
    directory = 'data\\cleaned\\database\\'

    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            
            # Read the CSV file into a DataFrame
            df = pd.read_csv(filepath)
            
            # Remove '[*]' from the DataFrame
            df_cleaned = remove_bracketed_star(df)
            
            # Write the cleaned DataFrame back to the same CSV file
            df_cleaned.to_csv(filepath, index=False)
            print(f"Cleaned data for {filename} written back to {filepath}.")

if __name__ == "__main__":
    main()
