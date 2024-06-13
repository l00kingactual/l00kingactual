import os
from PyPDF2 import PdfMerger

def collect_pdfs(directory):
    pdf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

# Define directories and output file
directory = r'C:\path\to\your\pdfs'
output_file = r'C:\path\to\output\combined.pdf'

# Collect and merge PDF files
pdf_files = collect_pdfs(directory)
merge_pdfs(pdf_files, output_file)

print(f"PDF files combined into {output_file}")
