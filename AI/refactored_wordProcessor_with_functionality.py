
from docx import Document
from bs4 import BeautifulSoup
import csv
import os
import chardet
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize to empty dictionaries
word_data = {}
html_data = {}
csv_data = {}

def read_word_file(file_path):
    try:
        logging.info('Reading Word file...')
        doc = Document(file_path)
        for para in doc.paragraphs:
            word_data[para.style.name] = para.text
        logging.info('Word file read successfully.')
    except Exception as e:
        logging.error(f'Error reading Word file: {e}')

def read_html_file(file_path):
    try:
        logging.info('Reading HTML file...')
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        for tag in soup.find_all(True):
            html_data[tag.name] = tag.text
        logging.info('HTML file read successfully.')
    except Exception as e:
        logging.error(f'Error reading HTML file: {e}')

def read_csv_file(file_path):
    try:
        logging.info('Reading CSV file...')
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                csv_data[i] = row
        logging.info('CSV file read successfully.')
    except Exception as e:
        logging.error(f'Error reading CSV file: {e}')

def main():
    logging.info('Main function started.')
    
    # File paths should be provided for actual execution
    read_word_file('sample.docx')
    read_html_file('sample.html')
    read_csv_file('sample.csv')
    
    logging.info('Main function completed.')

if __name__ == "__main__":
    main()
