import os
import glob
import shutil
import datetime
import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Directories to search
onedrive_path = Path(os.path.expanduser('~\\OneDrive'))
attached_drives = [Path(f'{d}:\\') for d in 'DEFGHIJKLMNOPQRSTUVWXYZ' if os.path.exists(f'{d}:\\')]

# Output directories
combined_folder = Path('D:\\All_Python_Scripts')
html_file_path = combined_folder / 'index.html'
json_file_path = combined_folder / 'combined_files.json'

# Ensure the combined folder exists
combined_folder.mkdir(parents=True, exist_ok=True)

# Function to collect Python files
def collect_python_files(base_path):
    python_files = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):
                file_path = Path(root) / file
                mod_time = file_path.stat().st_mtime
                python_files.append((file_path, datetime.datetime.fromtimestamp(mod_time)))
    return python_files

# Collect Python files from OneDrive and attached disks
all_python_files = collect_python_files(onedrive_path)
for drive in attached_drives:
    try:
        all_python_files.extend(collect_python_files(drive))
        logging.info(f"Collected Python files from {drive}")
    except Exception as e:
        logging.error(f"Error collecting files from {drive}: {e}")

# Sort files by modification date (oldest first)
all_python_files.sort(key=lambda x: x[1])

# Create machine-readable JSON file
json_data = [
    {
        'Filename': file_path.name,
        'Modification Date': mod_time.strftime('%Y-%m-%d %H:%M:%S'),
        'Folder': str(file_path.parent)
    }
    for file_path, mod_time in all_python_files
]

try:
    with json_file_path.open('w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)
    logging.info(f"JSON file saved as {json_file_path}")
except Exception as e:
    logging.error(f"Error writing JSON file: {e}")

# Copy files to the combined folder
for file_path, _ in all_python_files:
    try:
        relative_path = file_path.relative_to(file_path.anchor)
        destination_path = combined_folder / relative_path
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, destination_path)
        logging.info(f"Copied {file_path} to {destination_path}")
    except Exception as e:
        logging.error(f"Error copying file {file_path} to {destination_path}: {e}")

# Create HTML file
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Files</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Python Files</h1>
        <table class="table table-striped mt-3">
            <thead>
                <tr>
                    <th>Filename</th>
                    <th>Modification Date</th>
                    <th>Folder</th>
                </tr>
            </thead>
            <tbody>
"""

for file_path, mod_time in all_python_files:
    html_content += f"""
                <tr>
                    <td>{file_path.name}</td>
                    <td>{mod_time.strftime('%Y-%m-%d %H:%M:%S')}</td>
                    <td>{file_path.parent}</td>
                </tr>
    """

html_content += """
            </tbody>
        </table>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

try:
    with html_file_path.open('w', encoding='utf-8') as html_file:
        html_file.write(html_content)
    logging.info(f"HTML file saved as {html_file_path}")
except Exception as e:
    logging.error(f"Error writing HTML file: {e}")

print(f"HTML file saved as {html_file_path}")
print(f"JSON file saved as {json_file_path}")
print(f"All Python scripts copied to {combined_folder}")
