import optuna
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from bayes_opt import BayesianOptimization
from pyswarm import pso

from neural_network import build_enhanced_nn as NeuralNetworkModel, train_neural_network
from compute_metrics import compute_metrics, save_metrics_to_json
from sklearn.cluster import KMeans
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to create the model with given parameters
def create_model(dropout_0, dropout_1, learning_rate, num_layers, units_0, units_1):
    input_shape = (4,)  # Example input shape for the Iris dataset
    num_classes = 3  # Number of classes in the Iris dataset

    model = NeuralNetworkModel(
        input_shape=input_shape,
        num_classes=num_classes,
        dropout_0=dropout_0,
        dropout_1=dropout_1,
        learning_rate=learning_rate,
        num_layers=num_layers,
        units_0=units_0,
        units_1=units_1
    )
    return model

# Function to evaluate the model
def evaluate_model(model, X_train, y_train, X_val, y_val):
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=50, callbacks=[early_stopping], verbose=0)
    accuracy = model.evaluate(X_val, y_val, verbose=0)[1]
    return accuracy

# Function to dynamically optimize all metrics
def dynamic_metric_optimization(metrics):
    # Define which metrics to maximize and which to minimize
    metrics_to_maximize = ['accuracy', 'precision', 'recall', 'f1', 'balanced_acc', 'jaccard', 'r2']
    metrics_to_minimize = ['logloss', 'mse', 'mae']

    best_scores = {}
    for metric in metrics_to_maximize:
        best_scores[metric] = max(metrics.get(metric, 0), best_scores.get(metric, 0))
    for metric in metrics_to_minimize:
        best_scores[metric] = min(metrics.get(metric, float('inf')), best_scores.get(metric, float('inf')))
    
    return best_scores

# Optuna optimization function
def optuna_optimization(X_train, y_train, X_val, y_val, X_test, y_test, n_trials=100):
    metrics_summary = []  # List to store metrics from each trial

    def objective(trial):
        params = {
            'dropout_0': trial.suggest_float('dropout_0', 0.1, 0.5),
            'dropout_1': trial.suggest_float('dropout_1', 0.1, 0.5),
            'learning_rate': trial.suggest_float('learning_rate', 1e-4, 1e-2, log=True),
            'num_layers': trial.suggest_int('num_layers', 5, 10),
            'units_0': trial.suggest_int('units_0', 200, 600),
            'units_1': trial.suggest_int('units_1', 200, 400),
            'k_value': trial.suggest_float('k_value', 0.1, 1.0),
            'q_value': trial.suggest_float('q_value', 0.1, 1.0),
            'epsilon_value': trial.suggest_float('epsilon_value', 0.01, 0.1)
        }

        # Create and train the model using the sampled hyperparameters
        model = create_model(**params)
        train_neural_network(model, X_train, y_train, X_val, y_val, epochs=20)
        
        # Evaluate the model and compute metrics
        y_pred = model.predict(X_val).argmax(axis=1)
        y_proba = model.predict(X_val)
        
        epoch_times = np.random.uniform(0.1, 0.3, size=len(y_pred)).tolist()

        metrics = compute_metrics(y_val, y_pred, y_proba, epoch_times, 
                                  k_values=[params['k_value']] * len(y_val), 
                                  q_values=[params['q_value']] * len(y_val), 
                                  epsilon_values=[params['epsilon_value']] * len(y_val))
        
        # Optimize based on dynamic metric selection
        optimized_metrics = dynamic_metric_optimization(metrics)
        return sum(optimized_metrics.values())

    # Set up the Optuna study for optimization
    study = optuna.create_study(direction='maximize', sampler=optuna.samplers.TPESampler())
    study.optimize(objective, n_trials=n_trials)

    # Log the best parameters and their corresponding metrics
    logger.info(f"Best hyperparameters: {study.best_params}")
    logger.info(f"Best trial value: {study.best_value}")
    
    # Save the best metrics to JSON
    save_metrics_to_json(study.best_params, directory='analysis/optuna_optimization')
    return study.best_params, study.best_value

# Integration with Bayesian Optimization
def bayesian_optimization(X_train, y_train, X_val, y_val, build_fn):
    def evaluate(dropout_0, dropout_1, learning_rate, num_layers, units_0, units_1, k_value, q_value, epsilon_value):
        model = build_fn(
            dropout_0=dropout_0,
            dropout_1=dropout_1,
            learning_rate=learning_rate,
            num_layers=int(num_layers),
            units_0=int(units_0),
            units_1=int(units_1),
            k_value=k_value,
            q_value=q_value,
            epsilon_value=epsilon_value
        )
        return evaluate_model(model, X_train, y_train, X_val, y_val)

    pbounds = {
        'dropout_0': (0.1, 0.5),
        'dropout_1': (0.1, 0.5),
        'learning_rate': (1e-4, 1e-2),
        'num_layers': (5, 10),
        'units_0': (200, 600),
        'units_1': (200, 400),
        'k_value': (0.1, 1.0),
        'q_value': (0.1, 1.0),
        'epsilon_value': (0.01, 0.1)
    }

    optimizer = BayesianOptimization(f=evaluate, pbounds=pbounds, random_state=42)
    optimizer.maximize(init_points=10, n_iter=30)
    return optimizer.max

# Integration with Particle Swarm Optimization (PSO)
def pso_optimization(X_train, y_train, X_val, y_val, build_fn):
    def evaluate(params):
        model = build_fn(**params)
        return evaluate_model(model, X_train, y_train, X_val, y_val)

    pso = PSO(evaluate, param_bounds={
        'dropout_0': (0.1, 0.5),
        'dropout_1': (0.1, 0.5),
        'learning_rate': (1e-4, 1e-2),
        'num_layers': (5, 10),
        'units_0': (200, 600),
        'units_1': (200, 400),
        'k_value': (0.1, 1.0),
        'q_value': (0.1, 1.0),
        'epsilon_value': (0.01, 0.1)
    })
    pso.run_optimization(n_iterations=50)
    return pso.best_solution

# Clustering and AI-driven Techniques
def cluster_based_optimization(X_train, y_train):
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X_train)
    clusters = kmeans.predict(X_train)
    logger.info(f"Clusters identified: {np.unique(clusters)}")
    return clusters

# Main function to run all optimization techniques
def main():
    try:
        # Load a dataset (e.g., Iris)
        data = load_iris()
        X, y = data.data, data.target

        # Split the data
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        # Cluster-based optimization
        clusters = cluster_based_optimization(X_train, y_train)

        # Perform Optuna optimization
        best_params_optuna, best_value_optuna = optuna_optimization(X_train, y_train, X_val, y_val, X_val, y_val)

        # Perform Bayesian Optimization
        best_params_bayes = bayesian_optimization(X_train, y_train, X_val, y_val, create_model)

        # Perform PSO Optimization
        best_params_pso = pso_optimization(X_train, y_train, X_val, y_val, create_model)

        # Log and compare results from all optimization techniques
        logger.info(f"Optuna best params: {best_params_optuna}, best value: {best_value_optuna}")
        logger.info(f"Bayesian Optimization best params: {best_params_bayes}")
        logger.info(f"PSO best params: {best_params_pso}")

        # Final model build and evaluation with the best parameters from each method
        final_model = create_model(**best_params_optuna)
        final_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20)

        # Predict and save metrics for the final model
        y_pred = final_model.predict(X_val).argmax(axis=1)
        y_proba = final_model.predict(X_val)

        metrics = compute_metrics(
            y_val, y_pred, y_proba,
            epoch_times=[],  # Timing metrics, if available
            k_values=[best_params_optuna['k_value']] * len(y_val), 
            q_values=[best_params_optuna['q_value']] * len(y_val), 
            epsilon_values=[best_params_optuna['epsilon_value']] * len(y_val)
        )
        save_metrics_to_json(metrics, directory='analysis/optimized_model')

        logger.info("Optimization and training completed successfully.")

    except Exception as e:
        logger.error(f"An error occurred during the optimization process: {e}")
        raise

if __name__ == "__main__":
    main()
