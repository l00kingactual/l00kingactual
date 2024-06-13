import pandas as pd
from bs4 import BeautifulSoup
import pyodbc
from docx import Document

def read_csv(file_path):
    try:
        print("Reading CSV file...")
        df = pd.read_csv(file_path)
        print("CSV file read successfully.")
        return df
    except Exception as e:
        print(f"Error reading CSV: {e}")

def read_txt(file_path):
    try:
        print("Reading TXT file...")
        with open(file_path, 'r') as f:
            data = f.read()
        print("TXT file read successfully.")
        return data
    except Exception as e:
        print(f"Error reading TXT: {e}")

def read_md(file_path):
    try:
        print("Reading MD file...")
        with open(file_path, 'r') as f:
            data = f.read()
        print("MD file read successfully.")
        return data
    except Exception as e:
        print(f"Error reading MD: {e}")

def read_word(file_path):
    try:
        print("Reading Word file...")
        doc = Document(file_path)
        data = [p.text for p in doc.paragraphs]
        print("Word file read successfully.")
        return data
    except Exception as e:
        print(f"Error reading Word: {e}")

# In read_files.py
def read_excel(file_path):
    try:
        print("Reading Excel file...")
        xls = pd.ExcelFile(file_path)
        sheet_name = xls.sheet_names[0]  # Get the name of the first sheet
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        print(f"Excel file read successfully from sheet {sheet_name}.")
        return df
    except Exception as e:
        print(f"Error reading Excel: {e}")


def read_access(db_path, table_name):
    try:
        print("Reading Access database...")
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path + ';')
        df = pd.read_sql_query(f'SELECT * FROM {table_name}', conn)
        print("Access database read successfully.")
        return df
    except Exception as e:
        print(f"Error reading Access: {e}")

def read_html(file_path):
    try:
        print("Reading HTML file...")
        with open(file_path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
        print("HTML file read successfully.")
        return soup
    except Exception as e:
        print(f"Error reading HTML: {e}")
'''
# Example usage
if __name__ == "__main__":
    csv_data = read_csv('example.csv')
    txt_data = read_txt('example.txt')
    md_data = read_md('example.md')
    word_data = read_word('example.docx')
    excel_data = read_excel('example.xlsx')
    access_data = read_access('example.accdb', 'table_name')
    html_data = read_html('example.html')
'''