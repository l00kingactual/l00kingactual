import os
import pandas as pd
import logging
from jinja2 import Environment, FileSystemLoader

# Initialize logging
logging.basicConfig(filename='app.log', level=logging.INFO)

import os
import pandas as pd
import logging

def read_csv_files_from_folder(folder_path):
    object_list = []
    
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder {folder_path} does not exist.")
            logging.error(f"The folder {folder_path} does not exist.")
            return None
        
        # Loop through each file in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                file_path = os.path.join(folder_path, filename)
                
                try:
                    # Read the CSV file into a DataFrame
                    df = pd.read_csv(file_path)
                    
                    print(f"Successfully read CSV file from {file_path}")
                    logging.info(f"Successfully read CSV file from {file_path}")
                    
                    # Add to object list
                    base_filename = os.path.splitext(filename)[0]
                    object_list.append({"ID": base_filename, "Fields": ','.join(df.columns.tolist())})
                
                except Exception as e:
                    print(f"An error occurred while reading the file {file_path}: {str(e)}")
                    logging.error(f"An error occurred while reading the file {file_path}: {str(e)}")
        
        return object_list
    
    except Exception as e:
        print(f"An error occurred while processing the folder {folder_path}: {str(e)}")
        logging.error(f"An error occurred while processing the folder {folder_path}: {str(e)}")
        return None

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.INFO)
    folder_path = "playground\\playground_data\\csv"
    object_list = read_csv_files_from_folder(folder_path)
    
    if object_list:
        print("Successfully processed all CSV files.")
        logging.info("Successfully processed all CSV files.")


# clean the data frame before processing it in the pipeline 
def clean_data(df):
    try:
        # Implement your data cleaning logic here
        # For example, remove any NaN values
        df_cleaned = df.dropna()
        
        print("Successfully cleaned the data.")
        logging.info("Successfully cleaned the data.")
        
        return df_cleaned
    
    except Exception as e:
        print(f"An error occurred while cleaning the data: {str(e)}")
        logging.error(f"An error occurred while cleaning the data: {str(e)}")
        return None

# Write the cleaned data to a CSV file in the output folder 
def write_processed_data(df, output_folder, base_filename):
    try:
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        # Create the full output file path
        output_file_path = os.path.join(output_folder, f"{base_filename}_cleaned.csv")
        
        # Write the DataFrame to a CSV file
        df.to_csv(output_file_path, index=False)
        
        print(f"Successfully wrote cleaned data to {output_file_path}.")
        logging.info(f"Successfully wrote cleaned data to {output_file_path}.")
        
    except Exception as e:
        print(f"An error occurred while writing the processed data: {str(e)}")
        logging.error(f"An error occurred while writing the processed data: {str(e)}")

if __name__ == "__main__":
    input_folder = "playground\\playground_data\\csv"
    output_folder_clean = "playground\\playground_data"
    
    object_list = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(input_folder, filename)
            print(f"Reading file: {file_path}")
            try:
                df = pd.read_csv(file_path)
                print(f"Successfully read CSV file from {file_path}")
                logging.info(f"Successfully read CSV file from {file_path}")
                
                # Clean the data
                df_clean = clean_data(df)
                
                # Write the cleaned data
                base_filename = os.path.splitext(filename)[0]
                write_processed_data(df_clean, output_folder_clean, base_filename)
                
                # Add to object list
                object_list.append({"ID": base_filename, "Fields": ','.join(df.columns)})
                
            except Exception as e:
                print(f"An error occurred while processing {file_path}: {str(e)}")
                logging.error(f"An error occurred while processing {file_path}: {str(e)}")
    
    # Generate HTML file list
    template_path = "templates"
    
    if os.path.exists(template_path):
        env = Environment(loader=FileSystemLoader(template_path))
        
        try:
            template = env.get_template("file_list_template.html")
            html_files = [f for f in os.listdir(output_folder_clean) if f.endswith('.html')]
            output = template.render(file_list=html_files)
            
            with open("file_list.html", "w") as f:
                f.write(output)
                
        except Exception as e:
            print(f"An error occurred while generating the HTML file list: {str(e)}")
            logging.error(f"An error occurred while generating the HTML file list: {str(e)}")
    else:
        print(f"The template directory {template_path} does not exist.")
        logging.error(f"The template directory {template_path} does not exist.")
        
    # Generate object list index CSV
    df_object_list = pd.DataFrame(object_list)
    df_object_list.to_csv("object_list_index.csv", index=False)
