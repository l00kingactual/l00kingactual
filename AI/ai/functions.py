import os
import ast
import webbrowser

output_dir = 'model'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

html_file_path = os.path.join(output_dir, 'function_list.html')

def extract_functions(file_path):
    with open(file_path, 'r') as f:
        tree = ast.parse(f.read())
    return [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]

def generate_html(directory):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Functions</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1>Python Functions</h1>
            <ul>
    """
    
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            functions = extract_functions(os.path.join(directory, filename))
            html_content += f"<li><strong>{filename}</strong><ul>"
            for function in functions:
                html_content += f"<li>{function}</li>"
            html_content += "</ul></li>"
    
    html_content += """
            </ul>
        </div>
    </body>
    </html>
    """
    
    with open(html_file_path, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_content)

    print(f"HTML file created: {html_file_path}")
    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(html_file_path)

# Replace 'your_directory' with the directory containing your Python files
generate_html('model')
