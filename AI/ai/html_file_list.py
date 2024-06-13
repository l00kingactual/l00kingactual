import os
from jinja2 import Environment, FileSystemLoader

# Define the directory containing the HTML files
html_dir = "C:\\Users\\andy\\OneDrive\\Documents\\AstroAI\\ouchAstronomy\\AI\\ai\\playground\\playground_data\\clean\\html"

# List all HTML files in the directory
html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]

# Configure Jinja2 template environment
file_loader = FileSystemLoader('templates')  # Assuming your template is in a directory named "templates"
env = Environment(loader=file_loader)

# Load the template file
template = env.get_template('file_list_template.html')

# Render the template with the list of HTML files
output = template.render(files=html_files)

# Write the rendered HTML to a new file
with open("file_list.html", "w") as f:
    f.write(output)
