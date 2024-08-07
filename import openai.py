import openai

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

def read_file(file_path):
    """Reads the content of a Python file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def send_to_chatgpt(content):
    """Sends the content of the Python file to ChatGPT-4 for analysis."""
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Specify the appropriate model here
            prompt=f"Analyze the following Python code:\n\n{content}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error sending data to ChatGPT-4: {e}")
        return None

# Path to your Python file
file_path = 'path_to_your_python_file.py'

# Read the content of the Python file
file_content = read_file(file_path)
if file_content:
    # Send the content to ChatGPT-4 for analysis
    analysis = send_to_chatgpt(file_content)
    if analysis:
        print("Analysis from ChatGPT-4:")
        print(analysis)
    else:
        print("Failed to get analysis from ChatGPT-4.")
else:
    print("No content to analyze.")
