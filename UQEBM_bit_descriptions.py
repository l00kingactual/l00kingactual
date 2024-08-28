import os
import json
import numpy as np
from datetime import datetime
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import logging

# Custom imports for your specific modules
from UQEBM_BitDescriptionModel import BitDescriptionModel
from compute_metrics import compute_metrics, save_metrics_to_json
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_greedy_vaule_space import create_epsilon_greedy_space
from neural_network import build_enhanced_nn, train_neural_network, save_model_snapshots

# Hyperparameter tuning imports
from hypertunning.hyperparameter_tuning import (
    load_past_metrics, 
    identify_best_configurations, 
    bayesian_optimization,
    genetic_algorithm_optimization,
    hyperband_optimization,
    hill_climbing_optimization,
    simulated_annealing_optimization
)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def force_open_file(filepath):
    """Attempt to force read a file with specific exception handling."""
    try:
        with open(filepath, 'r', errors='ignore') as file:
            data = json.load(file)
            return data
    except PermissionError:
        logger.error(f"Permission denied: {filepath}. Attempting to change permissions.")
        try:
            os.chmod(filepath, 0o777)  # Change permissions to read-write for all
            with open(filepath, 'r', errors='ignore') as file:
                data = json.load(file)
                return data
        except Exception as e:
            logger.error(f"Failed to read file {filepath} after changing permissions: {e}")
            return None
    except Exception as e:
        logger.error(f"Failed to read file {filepath}: {e}")
        return None

def load_past_metrics(directory):
    """Load past metrics JSON files from a directory."""
    metrics = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            filepath = os.path.join(directory, file_name)
            data = force_open_file(filepath)
            if data:
                metrics.append(data)
    return metrics

def get_best_past_hyperparameters(metrics_directory):
    """Load past metrics and identify best configurations."""
    past_metrics = load_past_metrics(metrics_directory)

    if not past_metrics:
        logger.error("No valid metrics files could be loaded.")
        raise ValueError("Failed to load any valid metrics files.")

    best_past_config = identify_best_configurations(past_metrics)

    best_hyperparameters = {
        'num_layers': best_past_config.get('num_layers', 5),
        'units_0': best_past_config.get('units_0', 64),
        'dropout_0': best_past_config.get('dropout_0', 0.2),
        'units_1': best_past_config.get('units_1', 32),
        'dropout_1': best_past_config.get('dropout_1', 0.2),
        'learning_rate': best_past_config.get('learning_rate', 0.001)
    }
    return best_hyperparameters

def main():
    # Load dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=68)

    # Define epsilon_greedy space
    epsilon_values = create_epsilon_greedy_space()

    # Directory for saving metrics and loading past results
    metrics_directory = 'analysis/UQEBM_bit_descriptions'
    os.makedirs(metrics_directory, exist_ok=True)

    # Get the best hyperparameters from past runs
    try:
        best_hyperparameters = get_best_past_hyperparameters(metrics_directory)
    except ValueError:
        logger.error("No valid metrics files could be loaded. Please check file permissions and paths.")
        return

    # Loop over each idea space configuration
    for i, space in enumerate([{"k_values": k_value_space, "q_values": q_value_space, "epsilon_values": epsilon_values}]):
        # Initialize the model with the best hyperparameters
        model = BitDescriptionModel(
            range_min=space.get("range_min", 0),
            range_max=space.get("range_max", 100),
            number_bases=space.get("number_bases", [1, np.pi, np.e]),
            scales=space.get("scales", [1, 2, 3, 4, 5])
        )
        model.initialize_neural_net(
            input_shape=(X_train.shape[1],), 
            num_classes=len(np.unique(y_train)),
            num_layers=best_hyperparameters['num_layers'],
            units_0=best_hyperparameters['units_0'],
            dropout_0=best_hyperparameters['dropout_0'],
            units_1=best_hyperparameters['units_1'],
            dropout_1=best_hyperparameters['dropout_1'],
            learning_rate=best_hyperparameters['learning_rate']
        )
        
        # Train the model using the selected hyperparameter optimization method
        best_bayesian = bayesian_optimization(
            X_train.shape[1], len(np.unique(y_train)), X_train, y_train, 
            build_enhanced_nn, num_layers=best_hyperparameters['num_layers'], 
            units_0=best_hyperparameters['units_0'], dropout_0=best_hyperparameters['dropout_0'], 
            units_1=best_hyperparameters['units_1'], dropout_1=best_hyperparameters['dropout_1'], 
            learning_rate=best_hyperparameters['learning_rate']
        )
        
        # Predictions
        y_pred = model.predict(X_test)

        # Ensure y_pred contains class indices and not probabilities or one-hot encoded labels
        if y_pred.ndim > 1 and y_pred.shape[1] > 1:
            y_pred = np.argmax(y_pred, axis=1)  # Convert probabilities or one-hot encoded predictions to class indices

        y_proba = model.predict_proba(X_test)  # This should return the class probabilities

        # Compute metrics with k, q, epsilon values
        metrics = compute_metrics(y_test, y_pred, y_proba, epoch_times=None, k_values=k_value_space, q_values=q_value_space, epsilon_values=epsilon_values)

        # Save metrics to three distinct JSON files
        for j in range(1, 4):
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"metrics_{i+1}_file{j}_{current_time}.json"
            filepath = os.path.join(metrics_directory, filename)
            save_metrics_to_json(metrics, directory=filepath)
            logger.info(f"Metrics for idea space {i+1}, file {j} saved to {filepath}")

if __name__ == "__main__":
    main()
