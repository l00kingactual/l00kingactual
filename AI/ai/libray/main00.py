# Importing modules with namespaces
import data_fetching as df
# import knowledgelibray00 as kl
import error_recovery  as er 
import model_training as mt
# import utilities as utl
import json_helpers
from common_imports import *

from io import StringIO
from utilities import read_csv_file, read_txt_file, read_md_file  # these functions are in utilities.py
from contextlib import redirect_stdout, redirect_stderr

log_memory = StringIO()

with redirect_stdout(log_memory), redirect_stderr(log_memory):

    def main():
        # Initialize 
        from logging_and_error_handling import init_logging
        init_logging()

        # Read the memory from JSON file
        try:
            print("Reading existing memory...")
            memory = json_helpers.read_memory('memory.json')
            print(f"Memory read: {memory}")
        except Exception as e:
            print(f"An error occurred while reading memory: {e}")
            memory = {}
        
        # Fetch or create training and testing data
        train_df, test_df = df.fetch_or_create_data(memory)
        
        # Initialize your model_dict here (if not already initialized)
        from utilities import model_dict
        model_dict
        
        # Train models and update memory
        from utilities import model_dict
        mt.read_csv_filetrain_models(train_df, test_df, model_dict, memory)
        
        # Further code for model evaluation or other tasks



        print("Initializing...")
        
        # Assuming 'data' is defined here or fetched from some source
        data = memory.get('data', None)  # Replace this with actual data fetching logic if needed
        
        import knowledgelibray00 as kl

        try:
            print("Performing additional data analytics...")
            # Check if 'data' is not None
            if data is not None:
                analytics_result = kl.perform_data_analytics(data)
                print(f"Data analytics completed: {analytics_result}")
            else:
                print("Data is not available for analytics.")
        except Exception as e:
            # Log the error using leh 
            from logging_and_error_handling import handle_data_error
            handle_data_error(e)
            
            # Use functions from error_recovery.py for additional recovery logic
            er.error_recovery(e)
            
            # Console output for alerting
            print("---- ALERT: Error Occurred ----")
            print(f"An error occurred during additional data analytics: {e}")
            print("--------------------------------")


        # Initialize logging and error handling to leh
        try:
            from logging_and_error_handling import init_logging, init_error_handling
            print("Initializing logging and error handling...")
            init_logging()  # Initialize logging
            init_error_handling()  # Initialize error handling
        except Exception as e:
            print(f"An error occurred while initializing logging and error handling: {e}")

        # read the memory from JSON file
        try:
            print("Reading existing memory...")
            from utilities import read_memory
            memory = read_memory('memory.json')  # Read memory from JSON file
            print(f"Memory read: {memory}")
        except Exception as e:
            print(f"An error occurred while reading memory: {e}")
            memory = {}  # Initialize empty memory


        # Update data using functions from data_fetching.py
        try:
            print("Updating data...")
            data = df.update_data()  # Assuming update_data is a function in data_fetching.py
            print(f"Data updated: {data}")
        except Exception as e:
            print(f"An error occurred while updating data: {e}")

        # Initialize or load KMeans model using functions from knowledgelibrary00.py
        try:
            print("Reading existing memory...")
            memory = kl.read_memory('memory.json')  # Read memory from JSON file
            print(f"Memory read: {memory}")
        except Exception as e:
            print(f"An error occurred while reading memory: {e}")

        try:
            print("Initializing or loading K-means model...")
            kmeans_model = kl.init_or_load_model(memory)  # Initialize or load KMeans model
            print(f"K-means model initialized or loaded: {kmeans_model}")
        except Exception as e:
            print(f"An error occurred while initializing or loading the K-means model: {e}")

        # Initialize Q-table for Reinforcement Learning
        try:
            print("Initializing Q-table...")
            actions = ['action1', 'action2']  # Define your actions
            states = ['state1', 'state2']  # Define your states
            q_table = kl.init_q_table(actions, states)
            print("Q-table initialized.")
        except Exception as e:
            print(f"An error occurred while initializing the Q-table: {e}")

        # Build a standard Neural Network
        try:
            print("Building standard neural network...")
            input_shape = 128  # Define your input shape
            num_classes = 3  # Define the number of classes
            nn_model = kl.build_nn(input_shape, num_classes)
            print("Standard neural network built.")
        except Exception as e:
            print(f"An error occurred while building the standard neural network: {e}")

        # Build a Quantum-Inspired Neural Network
        try:
            print("Building quantum-inspired neural network...")
            qnn_model = kl.build_quantum_nn(input_shape, num_classes)
            print("Quantum-inspired neural network built.")
        except Exception as e:
            print(f"An error occurred while building the quantum-inspired neural network: {e}")

        # Additional Data Processing or Analytics Functions
        # Importing necessary modules


# Initialize memory (assuming kl.read_memory is a function that reads memory)
from json_helpers import read_memory
memory = read_memory("memory.json")

# Initialize or load models based on memory for training
from utilities import initialize_models
initialize_models(memory)

# Your new data that needs to be learned by each model
new_data = ...  # Replace with actual data

# Iterate through the models in utl.model_dict
from utilities import model_dict
for model_name, model_instance in model_dict.items():
    print(f"Applying new data to {model_name} model...")
    
    # General logic to fit new data
    if hasattr(model_instance, 'fit'):
        model_instance.fit(new_data)
        print(f"{model_name} model updated.")
    else:
        print(f"{model_name} model does not have a fit method. Skipped.")
    
    # Update memory for each model
    from knowledgelibray00 import update_memory
    update_memory(memory, model_instance, model_name, "memory.json")
    print(f"Memory for {model_name} model updated.")


def apply_to_model(data):
    """
    Function to apply data to all various models.
    """
    from knowledgelibray00 import model_dict, q_learning, nn, quantum_nn
    print("Applying data to KMeans model...")
    model_dict['kmeans'].fit(data)
    print("KMeans model updated.")

    print("Applying data to Q-table...")
    q_learning(model_dict['q_table'], "state1", "action1", 0.5, "state2")
    print("Q-table updated.")

    print("Applying data to Neural Network...")
    model_dict['nn'].fit(data, epochs=1)
    print("Neural Network updated.")

    print("Applying data to Quantum-Inspired Neural Network...")
    model_dict['quantum_nn'].fit(data, epochs=1)
    print("Quantum-Inspired Neural Network updated.")

    print("Updating memory...")
    update_memory(memory, "memory.json")
    print("Memory updated.")


    # print(f"Completed processing for file: {filename}")




    
    print("Program completed successfully.")

import sys
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO

# Initialize StringIO object to capture stdout and stderr
log_memory = StringIO()

# Redirect stdout and stderr to log_memory
with redirect_stdout(log_memory), redirect_stderr(log_memory):
    # Your main code here

    # Get the logged content
    logged_output = log_memory.getvalue()

# Create an HTML file with Bootstrap 5 formatting
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1>Log Output</h1>
    <pre>{logged_output}</pre>
  </div>
</body>
</html>
"""

# Write the HTML content to a file
with open("log_output.html", "w") as f:
    f.write(html_content)


# Main function to read data and apply to models
if __name__ == "__main__":
    DATA_FOLDER = "data"
    log_memory = StringIO()

    with redirect_stdout(log_memory):
        for filename in os.listdir(DATA_FOLDER):
            filepath = os.path.join(DATA_FOLDER, filename)

            print(f"Processing file: {filename}")

            if filename.endswith('.csv'):
                print("Reading CSV file...")
                data = read_csv_file(filepath)
                apply_to_model(data)

            elif filename.endswith('.txt'):
                print("Reading TXT file...")
                data = read_txt_file(filepath)
                apply_to_model(data)

            elif filename.endswith('.md'):
                print("Reading Markdown file...")
                data = read_md_file(filepath)
                apply_to_model(data)

    log_content = log_memory.getvalue()
    # html_content = generate_bootstrap_html(log_content)
    

