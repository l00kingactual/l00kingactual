import numpy as np
import json
import os
import tensorflow as tf
from datetime import datetime
from decimal import Decimal, getcontext
import logging
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from compute_metrics import compute_metrics, save_metrics_to_json
from quantum.quantum_layer import QuantumCircuitLayer
from quantum.quantum_bit_utils import encode_quantum_bit, decode_quantum_bit
from quantum.quantum_circuit_tuning import tune_quantum_circuit

# Define a class for integrated bit description with quantum encoding/decoding
from UQEBM_EnhancedBitDescription import EnhancedBitDescription
from UQEMB_IntegratedBitDescription import IntegratedBitDescription
from UQEBM_BitDescriptionModel import BitDescriptionModel, build_combined_model

# Correct imports based on provided files
from search.pso import run_pso_optimization
from search.simulated_annealing import simulated_annealing_optimization
from search.grid_search import run_search_optimization as grid_search_optimization
from search.bayesian import bayesian_optimization
from search.hyperband import hyperband_optimization
from search.optuna_optimization import optuna_optimization

from neural_network import build_enhanced_nn as NeuralNetworkModel
from sklearn.base import BaseEstimator, ClassifierMixin

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set precision for decimal operations
getcontext().prec = 5000

# Define optimization flags to select the desired optimization techniques in the most effective order
optimization_flags = {
    "pso": True,                    # Focus on continuous variables
    "simulated_annealing": True,    # Escape local optima
    "bayesian": True,               # Refine with probabilistic models
    "optuna": True,                 # Adaptive search (if enabled)
    "hyperband": True,              # Exhaustive final checks (if enabled)
    "grid_search": True,            # Exhaustive final checks (if enabled)
}

# Function to evaluate the model performance
def evaluate_model(model, X_train, y_train, X_val, y_val):
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, batch_size=64, callbacks=[early_stopping], verbose=1)
    accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
    
    # Confusion Matrix and Classification Report
    y_pred = model.predict(X_val).argmax(axis=1)
    logger.info(f"Confusion Matrix:\n{confusion_matrix(y_val, y_pred)}")
    logger.info(f"Classification Report:\n{classification_report(y_val, y_pred)}")
    
    return accuracy

# Function to save the best bit description and metrics
def save_best_bit_description(best_bit_desc, metrics, file_prefix='best_bit_desc'):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    best_bit_desc_data = {
        'range_min': str(best_bit_desc.range_min),
        'range_max': str(best_bit_desc.range_max),
        'number_bases': [str(base) for base in best_bit_desc.number_bases],
        'metrics': metrics
    }
    directory = f'analysis/UQEBM_v105'
    os.makedirs(directory, exist_ok=True)
    with open(f'{directory}/{file_prefix}_{current_time}.json', 'w') as file:
        json.dump(best_bit_desc_data, file, indent=4)
    logger.info(f"Best bit description saved to {directory}/{file_prefix}_{current_time}.json")

# Updated function to handle optimization without random search
def run_optimizations(X_train, y_train, X_val, y_val):
    best_params = {}
    logger.info("Starting Optimization Process...")

    # Step 1: Start with PSO for continuous variables
    if optimization_flags["pso"]:
        logger.info("Running Particle Swarm Optimization...")
        best_params["pso"] = run_pso_optimization()

    # Step 2: Use PSO results to inform Simulated Annealing
    if optimization_flags["simulated_annealing"]:
        logger.info("Running Simulated Annealing Optimization...")
        best_params["simulated_annealing"] = simulated_annealing_optimization(
            X_train.shape[1:], 
            len(np.unique(y_train)), 
            X_train, y_train, 
            build_combined_model, 
            logger
        )

    # Step 3: Execute Bayesian Optimization for fine-tuning
    if optimization_flags["bayesian"]:
        logger.info("Running Bayesian Optimization...")
        bayesian_starting_params = best_params.get("pso", {})
        best_params["bayesian"] = bayesian_optimization(
            X_train.shape[1:], 
            X_train, 
            y_train, 
            build_combined_model, 
            logger
        )

    # Step 4: Execute Optuna as a final adaptive step if enabled
    if optimization_flags["optuna"]:
        logger.info("Running Optuna Optimization...")
        best_params["optuna"] = optuna_optimization(
            X_train, 
            y_train, 
            X_val, 
            y_val, 
            X_val, 
            y_val
        )

    # Step 5: Run Hyperband and Grid Search for exhaustive final checks
    if optimization_flags["hyperband"]:
        logger.info("Running Hyperband Optimization...")
        best_params["hyperband"] = hyperband_optimization(
            X_train.shape[1:], 
            len(np.unique(y_train)), 
            X_train, 
            y_train, 
            logger
        )

    if optimization_flags["grid_search"]:
        logger.info("Running Grid Search Optimization for final verification...")
        best_params["grid_search"] = grid_search_optimization(X_train, y_train, "grid")

    logger.info("Optimization Process Completed.")
    return best_params

# Main execution function
def main():
    try:
        output_directory = f'analysis/UQEBM_v105/{datetime.now().strftime("%Y%m%d_%H%M%S")}'
        os.makedirs(output_directory, exist_ok=True)

        # Load dataset (example using Iris dataset, replace with appropriate dataset)
        data = load_iris()
        X, y = data.data, data.target

        # Split the data into training, validation, and test sets
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

        # Run selected optimizations
        logger.info("Running selected optimizations...")
        best_params = run_optimizations(X_train, y_train, X_val, y_val)

        # Build, evaluate, and save the best model based on the chosen optimization technique
        for method, params in best_params.items():
            model = build_combined_model(X_train.shape[1:], len(np.unique(y_train)), **params)
            accuracy = evaluate_model(model, X_train, y_train, X_val, y_val)
            logger.info(f"Accuracy for {method}: {accuracy}")

            # Save the best bit description and metrics
            metrics_summary = {"accuracy": accuracy}
            save_best_bit_description(params, metrics_summary, file_prefix=f'best_bit_desc_v105_{method}')

        logger.info("All selected optimizations completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
