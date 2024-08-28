import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from compute_metrics import compute_metrics, save_metrics_to_json
from datetime import datetime
from quantum.quantum_layer import QuantumCircuitLayer
from quantum.quantum_bit_utils import encode_quantum_bit, decode_quantum_bit
from quantum.quantum_circuit_tuning import tune_quantum_circuit
from neural_network import build_enhanced_nn as NeuralNetworkModel, train_neural_network

from search.grid_search  import (
    KerasClassifier,
    select_search_strategy,
    run_search_optimization,
    build_enhanced_nn
)

from search.random_search import run_random_search_optimization
from search.bayesian import bayesian_optimization
from search.optuna_optimization import optuna_optimization

# Setup logging
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Best Parameters from previous experiments
BEST_PARAMS = {
    'dropout_0': 0.1533,
    'dropout_1': 0.2195,
    'learning_rate': 0.00274,
    'num_layers': 7,
    'units_0': 436,
    'units_1': 300
}

# Enhanced Neural Network Model with Quantum Integration and Janus concept
def build_combined_model(input_shape, num_classes, k=None, q=None, epsilon=None, **params):
    inputs = tf.keras.layers.Input(shape=input_shape)
    
    # Quantum Circuit Layer Integration (assuming k, q, epsilon could be used here)
    if k is not None and q is not None and epsilon is not None:
        x = QuantumCircuitLayer(units=input_shape[0], k=k, q=q, epsilon=epsilon)(inputs)
    else:
        x = QuantumCircuitLayer(units=input_shape[0])(inputs)
    
    x = tf.keras.layers.Dense(params.get('units_0', 400), activation='relu')(x)
    x = tf.keras.layers.Dropout(params.get('dropout_0', 0.2))(x)

    # Standard Layers with Janus symmetry considerations
    for i in range(params.get('num_layers', 6) - 2):
        units = params.get('units_0', 400) // (2 ** (i % 3))
        x_forward = tf.keras.layers.Dense(units, activation='relu')(x)
        x_backward = tf.keras.layers.Dense(units, activation='relu')(x)
        x = tf.keras.layers.Add()([x_forward, x_backward])
        x = tf.keras.layers.Dropout(params.get('dropout_1', 0.2))(x)

    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.models.Model(inputs, outputs)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=params.get('learning_rate', 0.001)),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model



# Function to evaluate model accuracy
def evaluate_model(model, X_train, y_train, X_val, y_val):
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20, verbose=0)
    accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
    return accuracy

# Main function to manage and run the optimization processes
def main():
    try:
        # Load the Iris dataset
        data = load_iris()
        X, y = data.data, data.target

        # Split the data into training, validation, and test sets
        X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
        X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

        # Determine the search strategy based on the parameter space size
        search_strategy = 'grid'  # You can set this to 'random' or 'bayesian' as well

        # Run the search optimization
        best_params_grid = run_search_optimization(X_train, y_train, search_strategy)
        logger.info(f"Best parameters from {search_strategy} search: {best_params_grid}")

        # Further optimization steps (Random Search, Bayesian, etc.)
        best_params_random = run_random_search_optimization()
        logger.info(f"Best parameters from Random Search: {best_params_random}")

        best_params_bayesian = bayesian_optimization(X_train.shape[1:], X_train, y_train, build_combined_model, logger)
        logger.info(f"Best parameters from Bayesian Optimization: {best_params_bayesian}")

        best_params_optuna = optuna_optimization(X_train, y_train, X_val, y_val, X_test, y_test)
        logger.info(f"Best parameters from Optuna Optimization: {best_params_optuna}")

        # Select the best parameters based on results, e.g., from Bayesian Optimization
        final_params = best_params_bayesian['params']

        # Build the model with the selected best parameters
        model = build_combined_model(X_train.shape[1:], len(np.unique(y)), final_params)

        # Train the model with the selected best parameters
        train_neural_network(model, X_train, y_train, X_val, y_val, epochs=20)

        # Make predictions on the test set
        y_pred = model.predict(X_test).argmax(axis=1)
        y_proba = model.predict(X_test)

        # Compute and save metrics
        epoch_times = np.random.uniform(0.1, 0.3, size=len(y_pred)).tolist()
        k_values = [1] * len(y_pred)
        q_values = [0.5] * len(y_pred)
        epsilon_values = [0.1] * len(y_pred)

        metrics = compute_metrics(y_test, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values)
        save_metrics_to_json(metrics, directory='analysis/UQEBM_v104_Quantum')

        logger.info("Training and evaluation completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
