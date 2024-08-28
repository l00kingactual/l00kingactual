import logging
import numpy as np
import json
import os
from datetime import datetime
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, log_loss,
    mean_squared_error, mean_absolute_error, confusion_matrix,
    matthews_corrcoef, cohen_kappa_score, balanced_accuracy_score,
    jaccard_score, r2_score
)

def ensure_list(value):
    if isinstance(value, np.ndarray):
        return value.tolist()
    elif not isinstance(value, list):
        return [value]
    return value

def compute_metrics(y_true, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values):
    y_true = np.array(y_true).ravel()
    y_pred = np.array(y_pred).ravel()
    
    if y_true.dtype != int:
        y_true = y_true.astype(int)
    if y_pred.dtype != int:
        y_pred = y_pred.astype(int)
    
    if y_true.size == 0 or y_pred.size == 0:
        raise ValueError("Found array with 0 sample(s) (shape=(0,)) while a minimum of 1 is required.")
    
    y_proba = np.array(y_proba)
    if y_proba.ndim == 1:
        y_proba = y_proba.reshape(-1, 1)
    
    # Normalize probabilities and handle division by zero
    row_sums = y_proba.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1  # Avoid division by zero
    y_proba = y_proba / row_sums
    
    # Compute precision and log10 precision
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    log10_precision = np.log10(precision) if precision > 0 else np.nan

    log10_pi2 = np.log10(np.pi ** 2)
    root_c2_root_pi = np.sqrt((3e8) ** 2 * np.sqrt(np.pi))
    planck_time = 5.391e-44

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision,
        "recall": recall_score(y_true, y_pred, average='weighted', zero_division=0),
        "f1": f1_score(y_true, y_pred, average='weighted', zero_division=0),
        "logloss": np.nan if len(np.unique(y_true)) < 2 else log_loss(y_true, y_proba),
        "mse": mean_squared_error(y_true, y_pred),
        "mae": mean_absolute_error(y_true, y_pred),
        "conf_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "specificity": None,
        "mcc": matthews_corrcoef(y_true, y_pred),
        "kappa": cohen_kappa_score(y_true, y_pred),
        "balanced_acc": balanced_accuracy_score(y_true, y_pred),
        "jaccard": jaccard_score(y_true, y_pred, average='weighted'),
        "r2": r2_score(y_true, y_pred),
        "log10_accuracy": np.log10(accuracy_score(y_true, y_pred)),
        "root_pi_precision": np.sqrt(np.pi * precision) if not np.isnan(precision) else np.nan,
        "log10_pi2": log10_pi2,
        "root_c2_root_pi": root_c2_root_pi,
        "planck_time": planck_time,
        "epoch_times": epoch_times,
        "k_values": ensure_list(k_values),
        "q_values": ensure_list(q_values),
        "epsilon_values": ensure_list(epsilon_values)
    }
    
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    return metrics


def save_metrics_to_json(metrics, directory='analysis/compute_metrics'):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f'metrics_{timestamp}.json')
    
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, 'w') as f:
        json.dump(metrics, f, indent=4)
    
    print(f"Metrics saved to {filename}")

def read_metrics_from_directory(directory):
    metrics_list = []
    required_keys = {
        "accuracy", "precision", "recall", "f1", "logloss", "mse", "mae", 
        "conf_matrix", "specificity", "mcc", "kappa", "balanced_acc", "jaccard", 
        "r2", "log10_accuracy", "root_pi_precision", "log10_pi2", "root_c2_root_pi", 
        "planck_time", "epoch_times", "k_values", "q_values", "epsilon_values"
    }
    default_values = {key: 0 for key in required_keys}

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                try:
                    with open(file_path, 'r') as file:
                        for line in file:
                            try:
                                data = json.loads(line.strip())
                                if isinstance(data, dict):
                                    metrics = {key: data.get(key, default_values[key]) for key in required_keys}
                                    metrics_list.append([metrics[key] for key in required_keys])
                                else:
                                    logging.warning(f"File {file_path} does not contain a dictionary. Skipping line.")
                            except json.JSONDecodeError as e:
                                logging.error(f"Error reading JSON object in file {file_path}: {e.msg} at line {e.lineno} column {e.colno}")
                except Exception as e:
                    logging.error(f"Unexpected error reading JSON file {file_path}: {e}")
    return metrics_list
