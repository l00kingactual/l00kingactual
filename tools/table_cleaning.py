import os
import pandas as pd

def sanitize_name(name):
    # Remove special characters and replace spaces with underscores
    sanitized_name = ''.join(e for e in name if e.isalnum() or e == ' ')
    sanitized_name = sanitized_name.replace(' ', '_')
    # Truncate to 64 characters (MySQL's limit for identifiers)
    return sanitized_name[:64]

def main():
    input_dir = 'data\\cleaned'
    output_dir = 'data\\cleaned\\database'

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            filepath = os.path.join(input_dir, filename)
            df = pd.read_csv(filepath)

            # Sanitize table name
            table_name = sanitize_name(filename.replace('.csv', ''))

            # Sanitize field names
            df.columns = [sanitize_name(col) for col in df.columns]

            # Write cleaned DataFrame to new CSV file
            output_filepath = os.path.join(output_dir, f"{table_name}.csv")
            df.to_csv(output_filepath, index=False)
            print(f"Cleaned data for {table_name} written to {output_filepath}.")

if __name__ == "__main__":
    main()
