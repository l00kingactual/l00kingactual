import os
import json
import numpy as np
import pandas as pd
import logging
from datetime import datetime
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from compute_metrics import compute_metrics, save_metrics_to_json
from neural_network import build_enhanced_nn, train_neural_network, save_model_snapshots

# Import optimization methods
from opts.bayesian_opt import bayesian_optimization
from opts.genetic_opt import genetic_algorithm_optimization
from opts.hyperband_opt import hyperband_optimization
from opts.hill_climbing_opt import hill_climbing_optimization
from opts.simulated_annealing_opt import simulated_annealing_optimization

# Setup logging
log_file = 'hyperparameter_tuning.log'
logging.basicConfig(level=logging.DEBUG, handlers=[logging.FileHandler(log_file, 'w'), logging.StreamHandler()])
logger = logging.getLogger(__name__)

def load_past_metrics(directory):
    """Load past metrics JSON files from a directory."""
    metrics = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            with open(os.path.join(directory, file_name), 'r') as f:
                metrics.append(json.load(f))
    return metrics

def identify_best_configurations(metrics_list):
    """Identify the best configurations based on a primary metric (e.g., accuracy)."""
    sorted_metrics = sorted(metrics_list, key=lambda x: x.get('accuracy', 0), reverse=True)
    best_configs = sorted_metrics[0]  # Select the best configuration based on accuracy
    return best_configs

def handle_class_imbalance(x, y):
    """Handle class imbalance using SMOTE."""
    unique, counts = np.unique(y, return_counts=True)
    class_counts = dict(zip(unique, counts))
    min_class_samples = min(class_counts.values())
    smote = SMOTE(k_neighbors=min(5, max(1, min_class_samples - 1)))
    x_resampled, y_resampled = smote.fit_resample(x, y)
    return x_resampled, y_resampled

def add_interaction_terms(df):
    """Add interaction terms between features."""
    feature_cols = df.columns
    for i in range(len(feature_cols)):
        for j in range(i + 1, len(feature_cols)):
            df[f'interaction_{i}_{j}'] = df[feature_cols[i]] * df[feature_cols[j]]
    return df

def ensemble_predictions(x_train, y_train, x_val, y_val):
    """Train multiple models and return ensemble predictions."""
    models = [
        ('lr', LogisticRegression()),
        ('rf', RandomForestClassifier(n_estimators=100)),
        ('gb', GradientBoostingClassifier(n_estimators=100))
    ]
    
    for name, model in models:
        model.fit(x_train, y_train)
        y_pred = model.predict(x_val)
        logger.info(f"{name} Accuracy: {accuracy_score(y_val, y_pred)}")
    
    predictions = [model.predict(x_val) for name, model in models]
    ensemble_pred = np.array(predictions).mean(axis=0).round()
    ensemble_acc = accuracy_score(y_val, ensemble_pred)
    logger.info(f"Ensemble Accuracy: {ensemble_acc}")
    return ensemble_pred

if __name__ == "__main__":
    try:
        # Load past metrics and identify best configurations
        metrics_directory = 'analysis/UQEBM_bit_descriptions'
        past_metrics = load_past_metrics(metrics_directory)
        best_past_config = identify_best_configurations(past_metrics)

        # Use best configurations to update hyperparameters
        num_layers = best_past_config.get('num_layers', 5)
        units_0 = best_past_config.get('units_0', 64)
        dropout_0 = best_past_config.get('dropout_0', 0.2)
        units_1 = best_past_config.get('units_1', 32)
        dropout_1 = best_past_config.get('dropout_1', 0.2)
        learning_rate = best_past_config.get('learning_rate', 0.001)

        # Sample training and validation data
        x_train = np.random.rand(100, 9)
        y_train = np.random.randint(0, 3, 100)
        x_val = np.random.rand(20, 9)
        y_val = np.random.randint(0, 3, 20)

        x_train_balanced, y_train_balanced = handle_class_imbalance(x_train, y_train)
        x_val_balanced, y_val_balanced = handle_class_imbalance(x_val, y_val)

        df = pd.DataFrame(x_train_balanced, columns=[f'feature{i}' for i in range(1, 10)])
        df = add_interaction_terms(df)
        x_train = df.values

        # Run hyperparameter optimization methods using best configurations as starting points
        best_bayesian = bayesian_optimization(x_train.shape[1], 3, x_train, y_train_balanced, build_enhanced_nn, 
                                              num_layers=num_layers, units_0=units_0, dropout_0=dropout_0,
                                              units_1=units_1, dropout_1=dropout_1, learning_rate=learning_rate)
        logger.info(f"Best Bayesian Optimization: {best_bayesian}")

        best_genetic = genetic_algorithm_optimization(x_train.shape[1], 3, x_train, y_train_balanced, build_enhanced_nn, logger,
                                                      num_layers=num_layers, units_0=units_0, dropout_0=dropout_0,
                                                      units_1=units_1, dropout_1=dropout_1, learning_rate=learning_rate)
        logger.info(f"Best Genetic Algorithm Optimization: {best_genetic}")

        best_hyperband = hyperband_optimization(x_train.shape[1], 3, x_train, y_train_balanced, build_enhanced_nn, 
                                                num_layers=num_layers, units_0=units_0, dropout_0=dropout_0,
                                                units_1=units_1, dropout_1=dropout_1, learning_rate=learning_rate)
        logger.info(f"Best Hyperband Optimization: {best_hyperband}")

        best_hill_climbing = hill_climbing_optimization(x_train.shape[1], 3, x_train, y_train_balanced, build_enhanced_nn, 
                                                        num_layers=num_layers, units_0=units_0, dropout_0=dropout_0,
                                                        units_1=units_1, dropout_1=dropout_1, learning_rate=learning_rate)
        logger.info(f"Best Hill Climbing Optimization: {best_hill_climbing}")

        best_simulated_annealing = simulated_annealing_optimization(x_train.shape[1], 3, x_train, y_train_balanced, build_enhanced_nn, 
                                                                     num_layers=num_layers, units_0=units_0, dropout_0=dropout_0,
                                                                     units_1=units_1, dropout_1=dropout_1, learning_rate=learning_rate)
        logger.info(f"Best Simulated Annealing Optimization: {best_simulated_annealing}")

        ensemble_pred = ensemble_predictions(x_train, y_train_balanced, x_val, y_val_balanced)

        # Train neural network with best hyperparameters from Bayesian optimization
        best_model_params = {
            'num_layers': int(best_bayesian['num_layers']),
            'units_0': int(best_bayesian['units_0']),
            'dropout_0': best_bayesian['dropout_0'],
            'units_1': int(best_bayesian['units_1']),
            'dropout_1': best_bayesian['dropout_1'],
            'learning_rate': best_bayesian['learning_rate']
        }

        best_model = build_enhanced_nn(
            input_shape=(x_train.shape[1],),
            num_classes=3,
            **best_model_params
        )

        best_model, epoch_times = train_neural_network(best_model, x_train, y_train_balanced, epochs=10)

        metrics = compute_metrics(best_model, x_val, y_val_balanced)
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        save_metrics_to_json(metrics, f'analysis/genetic_algorithm_optimization/genetic_algorithm_optimization_{current_time}.json')
        logger.info(f'Metrics saved at analysis/genetic_algorithm_optimization/genetic_algorithm_optimization_{current_time}.json')

        snapshot_directory = f'results/hyperparameter_tuning/snapshots_{current_time}'
        save_model_snapshots(best_model, 10, snapshot_directory)
        logger.info(f"Model snapshots saved at {snapshot_directory}")

        print("Hyperparameter tuning completed.")
    
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
