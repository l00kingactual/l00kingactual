
import os
import csv

import data_fetching as df
# import knowledgelibray00 as kl
import logging_and_error_handling as leh
import error_recovery  as er 
import model_training as mt
import utilities as utl
from common_imports import *
import json_helpers
import logging
import pickle

import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('This is a debug message')

# Declare the data folder path
DATA_FOLDER_PATH = "data"  # Declare the data folder path

def read_csv_file(file_name):
    """
    Reads a CSV file and returns its content as a list of dictionaries.
    """
    file_path = os.path.join(DATA_FOLDER_PATH, file_name)
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

def read_txt_file(file_name):
    """
    Reads a TXT file and returns its content as a string.
    """
    file_path = os.path.join(DATA_FOLDER_PATH, file_name)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

def read_md_file(file_name):
    """
    Reads a Markdown (.md) file and returns its content as a string.
    """
    return read_txt_file(file_name)  # Markdown files are text files



# Initialize memory
memory = json_helpers.read_memory("memory.json")

# Create a model dictionary to store the models types from kl
model_dict = {}

def get_model_dict():
    return model_dict

# Initialize memory (assuming kl.read_memory is a function that reads memory)
memory = json_helpers.read_memory("memory.json")

# Initialize or load models based on memory for training
from knowledgelibray00 import initialize_models
initialize_models(memory)

# Now, you can directly access models from utl.model_dict
kmeans_model = utl.model_dict['kmeans']

def apply_to_model(data):
    """
    Function to apply data to all various models.
    """
    print("Applying data to KMeans model...")
    model_dict['kmeans'].fit(data)
    print("KMeans model updated.")

    print("Applying data to Q-table...")
    from knowledgelibray00 import q_learning
    q_learning(model_dict['q_table'], "state1", "action1", 0.5, "state2")
    print("Q-table updated.")

    print("Applying data to Neural Network...")
    model_dict['nn'].fit(data, epochs=1)
    print("Neural Network updated.")

    print("Applying data to Quantum-Inspired Neural Network...")
    model_dict['quantum_nn'].fit(data, epochs=1)
    print("Quantum-Inspired Neural Network updated.")

    print("Applying data to Enhanced Quantum-Inspired Neural Network...")
    model_dict['enhanced_quantum_nn'].fit(data, epochs=1)
    print("Enhanced Quantum-Inspired Neural Network updated.")

    print("Applying data to Simple PyTorch Model...")
    # Insert your PyTorch model training logic here
    print("Simple PyTorch Model updated.")

    print("Updating memory...")
    from knowledgelibray00 import update_memory
    update_memory(memory, "memory.json")
    print("Memory updated.")


def save_model_to_memory(model):
    """
    Serialize the model and return its byte representation.
    
    Parameters:
    model (object): The machine learning model to serialize.
    
    Returns:
    bytes: The byte representation of the model.
    """
    return pickle.dumps(model)

import importlib

def log_error(error_message):
    # Lazy import of the logging module or your custom logging module
    logging_module = importlib.import_module('logging')
    
    # Initialize logging (if your custom logging module requires initialization)
    logging_module.basicConfig(level=logging_module.ERROR)
    
    # Log the error message
    logging_module.error(error_message)
    
    # Console log
    print(f"An error occurred: {error_message}")

