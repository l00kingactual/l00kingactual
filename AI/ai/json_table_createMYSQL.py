import os
import pandas as pd
import json

# Step 1: Read CSV files and create data object
def read_csv_files(directory_path):
    data_object = {}
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            table_name = filename.replace('.csv', '')
            df = pd.read_csv(os.path.join(directory_path, filename))
            headers = list(df.columns)
            data = df.values.tolist()
            data_object[table_name] = {'headers': headers, 'data': data}
    return data_object

# Step 2: Generate JSON data document
def generate_json(data_object, json_file_path):
    with open(json_file_path, 'w') as json_file:
        json.dump(data_object, json_file, indent=4)

# Step 3: Generate MySQL table creation queries
def generate_mysql_queries(data_object, sql_file_path):
    with open(sql_file_path, 'w') as sql_file:
        for table, info in data_object.items():
            query = f"CREATE TABLE `{table}` (\n"
            for header in info['headers']:
                query += f"  `{header}` VARCHAR(255),\n"
            query = query.rstrip(",\n")
            query += "\n);\n\n"
            sql_file.write(query)

if __name__ == "__main__":
    directory_path = r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\csv_data"
    json_file_path = r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\csv_data_json.json"
    sql_file_path = r"C:\Users\andy\OneDrive\Documents\AstroAI\ouchAstronomy\AI\ai\tables_create.sql"

    data_object = read_csv_files(directory_path)
    generate_json(data_object, json_file_path)
    generate_mysql_queries(data_object, sql_file_path)
