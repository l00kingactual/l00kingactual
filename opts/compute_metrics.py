import numpy as np
import json
import os
import time
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, log_loss,
    mean_squared_error, mean_absolute_error, confusion_matrix,
    matthews_corrcoef, cohen_kappa_score, balanced_accuracy_score,
    jaccard_score, r2_score
)

def compute_metrics(y_true, y_pred, y_proba, epoch_times):
    y_true = np.array(y_true).ravel()
    y_pred = np.array(y_pred).ravel()
    
    y_proba = np.array(y_proba)
    if y_proba.ndim == 1:
        y_proba = y_proba.reshape(-1, 1)
    
    y_proba = y_proba / y_proba.sum(axis=1, keepdims=True)
    
    precision = precision_score(y_true, y_pred, average='weighted')
    log10_precision = np.log10(precision) if precision > 0 else np.nan

    log10_pi2 = np.log10(np.pi ** 2)
    root_c2_root_pi = np.sqrt((3e8) ** 2 * np.sqrt(np.pi))
    planck_time = 5.391e-44

    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision,
        "recall": recall_score(y_true, y_pred, average='weighted'),
        "f1": f1_score(y_true, y_pred, average='weighted'),
        "logloss": log_loss(y_true, y_proba),
        "mse": mean_squared_error(y_true, y_pred),
        "mae": mean_absolute_error(y_true, y_pred),
        "conf_matrix": confusion_matrix(y_true, y_pred).tolist(),
        "specificity": None,  # Specificity calculation can be added if required
        "mcc": matthews_corrcoef(y_true, y_pred),
        "kappa": cohen_kappa_score(y_true, y_pred),
        "balanced_acc": balanced_accuracy_score(y_true, y_pred),
        "jaccard": jaccard_score(y_true, y_pred, average='weighted'),
        "r2": r2_score(y_true, y_pred),
        "log10_accuracy": np.log10(accuracy_score(y_true, y_pred)),
        "root_pi_precision": np.sqrt(np.pi * precision) if not np.isnan(precision) else np.nan,
        #"cube_log10_pi": (np.pi * log10_precision) ** (1/3) if not np.isnan(log10_precision) else np.nan,
        "log10_pi2": log10_pi2,
        "root_c2_root_pi": root_c2_root_pi,
        "planck_time": planck_time,
        "epoch_times": epoch_times
    }
    
    for key, value in metrics.items():
        print(f"{key}: {value}")
    
    return metrics

def save_metrics_to_json(metrics, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(metrics, f, indent=4)

# Example usage
if __name__ == "__main__":
    y_true = [0, 1, 0, 1, 1, 0]  # Example values
    y_pred = [0, 0, 1, 1, 0, 1]  # Example values
    y_proba = [[0.8, 0.2], [0.3, 0.7], [0.6, 0.4], [0.4, 0.6], [0.9, 0.1], [0.2, 0.8]]  # Example values
    epoch_times = [0.1, 0.2, 0.15, 0.12, 0.18, 0.22]  # Example epoch times

    metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times)
   # save_metrics_to_json(metrics, 'metrics.json')

    for key, value in metrics.items():
        print(f"{key}: {value}")
