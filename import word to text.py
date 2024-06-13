from docx import Document

# Path to your .docx file
docx_file_path = 'C:\\Users\\actua\\OneDrive\\Desktop\\hello_world.docx'
# Path to the output .txt file
txt_file_path = 'output.txt'

# Function to read a .docx file and save its content to a .txt file
def docx_to_txt(docx_path, txt_path):
    # Load the .docx file
    doc = Document(docx_path)
    # Open the .txt file for writing
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        # Iterate through each paragraph in the document and write it to the .txt file
        for paragraph in doc.paragraphs:
            txt_file.write(paragraph.text + '\n')

# Call the function with the file paths
docx_to_txt(docx_file_path, txt_file_path)
