import os
import tkinter as tk
from tkinter import filedialog
import comtypes.client
import pdfkit

def convert_visio_to_html(visio_path, output_dir):
    visio = comtypes.client.CreateObject("Visio.Application")
    doc = visio.Documents.Open(visio_path)
    html_path = os.path.join(output_dir, os.path.splitext(os.path.basename(visio_path))[0] + '.html')
    doc.SaveAs(html_path, 10)  # 10 is the constant for Visio SaveAsWeb
    doc.Close()
    visio.Quit()
    return html_path

def convert_html_to_pdf(html_path):
    pdf_path = os.path.splitext(html_path)[0] + '.pdf'
    pdfkit.from_file(html_path, pdf_path)
    return pdf_path

def add_heading_to_html(html_path, heading):
    with open(html_path, 'r') as file:
        lines = file.readlines()
    with open(html_path, 'w') as file:
        for i, line in enumerate(lines):
            if '<body>' in line:
                lines.insert(i + 1, f'<h1>{heading}</h1>\n')
                break
        file.writelines(lines)

def process_files(directory):
    output_dir = os.path.join(directory, 'converted_files')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.vsd', '.vsdx')):
                visio_path = os.path.join(root, file)
                html_path = convert_visio_to_html(visio_path, output_dir)
                add_heading_to_html(html_path, os.path.basename(visio_path))
                convert_html_to_pdf(html_path)
    
    print(f"Conversion completed. Files are saved in {output_dir}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        process_files(directory)

# Initialize main window
root = tk.Tk()
root.title("Visio to HTML and PDF Converter")

tk.Label(root, text="Select Directory of Visio Files").pack(pady=10)
select_button = tk.Button(root, text="Select Directory", command=select_directory)
select_button.pack(pady=10)

root.mainloop()
