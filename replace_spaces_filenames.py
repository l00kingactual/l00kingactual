import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def parse_html_filenames(html_directory):
    try:
        parsed_filenames = []
        # Iterate over the HTML files in the specified directory
        for filename in os.listdir(html_directory):
            if filename.endswith('.html'):
                # Parse the filename to replace "-" and " " with "_"
                parsed_filename = filename.replace("-", "_").replace(" ", "_").upper()
                # Ensure that the parsed filename contains only letters and "_"
                parsed_filename = ''.join(char for char in parsed_filename if char.isalpha() or char == '_')
                # Append the parsed filename to the list
                parsed_filenames.append(parsed_filename)
        
        logger.debug("Filenames parsed successfully.")
        return parsed_filenames
    except Exception as e:
        logger.error(f"Error parsing HTML filenames: {e}")
        return []

# Specify the directory containing the HTML files
html_directory = 'html\\'

try:
    # Parse HTML filenames
    parsed_filenames = parse_html_filenames(html_directory)
    print("Parsed Filenames:")
    for filename in parsed_filenames:
        print(filename)
except Exception as e:
    logger.error(f"An error occurred during parsing: {e}")
