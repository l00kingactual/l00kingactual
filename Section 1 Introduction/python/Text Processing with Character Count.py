import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def count_characters(input_text_path):
    """
    Counts the occurrences of each character in a text file.
    
    Parameters:
    input_text_path (str): Path to the input text file.
    
    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    try:
        logging.info(f"Reading input text file: {input_text_path}")
        with open(input_text_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        logging.debug(f"Input text length: {len(text)} characters")

        # Count occurrences of each character
        char_count = {}
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        logging.info("Character counting completed successfully")
        return char_count

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
input_text_path = 'path_to_input_text.txt'
char_count_dict = count_characters(input_text_path)
print(char_count_dict)
