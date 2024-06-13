# Importing modules with namespaces
from common_imports import *
# import utilities as utl

import time

# create the training and testing dataframes for the model training of the models in utl.model_dict

def train_models(train_df, test_df, model_dict, memory):
    """
    Train all models specified in model_dict and update the memory.
    
    Parameters:
    train_df (DataFrame): The training dataframe.
    test_df (DataFrame): The testing dataframe.
    model_dict (dict): Dictionary containing model names as keys and model objects as values.
    memory (dict): The memory dictionary.
    
    Returns:
    None
    """
    for name, model in model_dict.items():
        print(f"Training {name} model...")
        
        # Your logic to train the model
        model.fit(train_df)
        
        # Serialize the model and update memory
        from utilities import save_model_to_memory
        memory[name] = save_model_to_memory(model)
        
        print(f"{name} model trained and saved to memory.")

