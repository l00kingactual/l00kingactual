import pandas as pd
from bs4 import BeautifulSoup
import pyodbc
from docx import Document

def write_csv(df, file_path):
    try:
        print("Writing CSV file...")
        if isinstance(df, pd.DataFrame):
            df.to_csv(file_path, index=False)
            print("CSV file written successfully.")
        else:
            print(f"Error: Data is not a DataFrame. It's a {type(df)}.")
    except Exception as e:
        print(f"Error writing CSV: {e}")


def write_txt(data, file_path):
    try:
        print("Writing TXT file...")
        with open(file_path, 'w') as f:
            f.write(data)
        print("TXT file written successfully.")
    except Exception as e:
        print(f"Error writing TXT: {e}")

def write_md(data, file_path):
    try:
        print("Writing MD file...")
        with open(file_path, 'w') as f:
            f.write(data)
        print("MD file written successfully.")
    except Exception as e:
        print(f"Error writing MD: {e}")

def write_word(data, file_path):
    try:
        print("Writing Word file...")
        doc = Document()
        doc.add_paragraph(data)
        doc.save(file_path)
        print("Word file written successfully.")
    except Exception as e:
        print(f"Error writing Word: {e}")

def write_excel(df, file_path):
    try:
        print("Writing Excel file...")
        df.to_excel(file_path, index=False)
        print("Excel file written successfully.")
    except Exception as e:
        print(f"Error writing Excel: {e}")

def write_access(df, db_path, table_name):
    try:
        print("Writing Access database...")
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path + ';')
        cursor = conn.cursor()
        for index, row in df.iterrows():
            cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", row['Column1'], row['Column2'], row['Column3'])
        conn.commit()
        print("Access database written successfully.")
    except Exception as e:
        print(f"Error writing Access: {e}")

def write_html(soup, file_path):
    try:
        print("Writing HTML file...")
        with open(file_path, 'w') as f:
            f.write(str(soup))
        print("HTML file written successfully.")
    except Exception as e:
        print(f"Error writing HTML: {e}")
'''
# Example usage
if __name__ == "__main__":
    df = pd.DataFrame({'Column1': [1, 2], 'Column2': ['a', 'b']})
    write_csv(df, 'example.csv')
    write_txt("This is a text.", 'example.txt')
    write_md("# This is a markdown.", 'example.md')
    write_word("This is a word document.", 'example.docx')
    write_excel(df, 'example.xlsx')
    write_access(df, 'example.accdb', 'table_name')
    soup = BeautifulSoup('<html><body><h1>Hello, world!</h1></body></html>', 'html.parser')
    write_html(soup, 'example.html')
'''