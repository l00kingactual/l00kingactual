from decimal import Decimal
import os
import glob
import json
import logging
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer
from compute_metrics import compute_metrics, save_metrics_to_json, read_metrics_from_directory
from UQEBM import IntegratedBitDescription, save_best_bit_description
from search.grid_search import run_grid_search_optimization
from search.random_search import run_random_search_optimization
from search.bayesian import bayesian_optimization
from search.hyperband import hyperband_optimization

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

# Required keys for the JSON data
required_keys = {'f1', 'kappa', 'logloss', 'precision', 'accuracy', 'balanced_acc', 'jaccard', 'r2', 'mcc', 'mae', 'mse', 'recall'}

# List to enable/disable specific search methods
search_methods = {
    'grid_search': False,
    'random_search': True,
    'bayesian_search': True,
    'hyperband_search': True
}

def check_and_fill_missing_keys(data, required_keys):
    for key in required_keys:
        if key not in data:
            data[key] = np.nan
    return data

def load_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        if isinstance(data, list):
            data = data[0]  # Assuming the first element is the dictionary if it's a list
        data = check_and_fill_missing_keys(data, required_keys)
        data['planck_time'] = datetime.fromtimestamp(os.path.getmtime(file_path)).timestamp()
        return data
    except json.JSONDecodeError as e:
        logging.error(f'Error reading JSON file {file_path}: {e}')
        return None

def enhanced_metrics_calculation(data):
    logging.debug("Calculating enhanced metrics.")
    numerical_values = [value for key, value in data.items() if key in required_keys and value is not None and not np.isnan(value)]
    if numerical_values:
        data['new_metric'] = np.nanmean(numerical_values)
    else:
        data['new_metric'] = np.nan
        logging.warning("No numerical values found for enhanced metrics calculation.")
    return data

def read_json_files_from_directory(directory):
    logging.info(f"Reading JSON files from directory: {directory}")
    file_paths = glob.glob(os.path.join(directory, '**/*.json'), recursive=True)
    logging.info(f"Found {len(file_paths)} JSON files.")
    json_data = []
    
    for file_path in file_paths:
        data = load_json_file(file_path)
        if data:
            enhanced_data = enhanced_metrics_calculation(data)
            json_data.append(enhanced_data)
        else:
            logging.warning(f"Skipping file {file_path} due to load error.")
    
    return json_data

def create_dataframe(json_data):
    if not json_data:
        logging.warning("No JSON data to create dataframe.")
        return pd.DataFrame()
    df = pd.DataFrame(json_data)
    df = df.sort_values(by='planck_time')
    return df

def perform_clustering(data, integrated_bit_desc):
    if data.shape[0] < 3:
        logging.error("Not enough samples for clustering. Skipping clustering.")
        return []
    
    imputer = SimpleImputer(strategy='mean')
    data_imputed = imputer.fit_transform(data)
    
    if data_imputed.shape[0] < 3:
        logging.error("Not enough samples for clustering after imputation. Skipping clustering.")
        return []

    kmeans = KMeans(n_clusters=3, random_state=0).fit(data_imputed)
    cluster_centers = kmeans.cluster_centers_
    best_cluster_index = np.argmax([np.mean(center) for center in cluster_centers])
    best_cluster_metrics = cluster_centers[best_cluster_index]

    logging.debug(f"Cluster centers: {cluster_centers}")
    logging.debug(f"Best cluster index: {best_cluster_index}")
    logging.debug(f"Best cluster metrics: {best_cluster_metrics}")

    return best_cluster_metrics.tolist()

def convert_to_serializable(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def save_json(data, directory, prefix):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f'{prefix}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json')
    with open(file_path, 'w') as f:
        json.dump(data, f, default=convert_to_serializable, indent=4)
    logging.info(f"Data saved to {file_path}")
    return file_path

def search_and_save(root_dir):
    logging.info(f"Processing all JSON files in directory: {root_dir}")
    
    json_data = read_json_files_from_directory(root_dir)
    df = create_dataframe(json_data)
    numerical_data = df.select_dtypes(include=[np.number])
    
    integrated_bit_desc = IntegratedBitDescription(range_min=0, range_max=100, number_bases=[360, 60, 50], quantum_states={
        0: {'n': 3, 'l': 1, 'm_l': 1, 'm_s': -0.5},
        1: {'n': 4, 'l': 2, 'm_l': 2, 'm_s': 0.5},
        2: {'n': 5, 'l': 3, 'm_l': 0, 'm_s': -0.5},
        3: {'n': 6, 'l': 1, 'm_l': -1, 'm_s': 0.5},
        4: {'n': 7, 'l': 2, 'm_l': 3, 'm_s': -0.5},
        5: {'n': 8, 'l': 3, 'm_l': -2, 'm_s': 0.5},
        6: {'n': 9, 'l': 4, 'm_l': 4, 'm_s': -0.5},
    })

    if not numerical_data.empty:
        best_cluster_metrics = perform_clustering(numerical_data, integrated_bit_desc)
    else:
        best_cluster_metrics = []

    # Ensure df has the necessary columns for metrics
    if {'y_true', 'y_pred', 'y_proba'}.issubset(df.columns):
        y_true = df['y_true'].fillna(0).values
        y_pred = df['y_pred'].fillna(0).values
        y_proba = df['y_proba'].apply(lambda x: [0.5, 0.5] if pd.isnull(x) else x).tolist()
        epoch_times = [0.1] * len(y_true)  # Example epoch times
        metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times)
        save_metrics_to_json(metrics, 'analysis/enhanced_clustering')
    else:
        logging.error("Required columns for metrics calculation are missing.")
        metrics = {}

    # Perform searches based on the enabled search methods
    summary_metrics = {}

    if search_methods['random_search']:
        logging.info("Running Random Search Optimization...")
        best_random_result = run_random_search_optimization()
        best_random_params, best_random_score = best_random_result if isinstance(best_random_result, tuple) else (best_random_result, None)
        summary_metrics['best_random_params'] = best_random_params
        summary_metrics['best_random_score'] = best_random_score

    if search_methods['grid_search']:
        logging.info("Running Grid Search Optimization...")
        best_grid_result = run_grid_search_optimization()
        best_grid_params, best_grid_score = best_grid_result if isinstance(best_grid_result, tuple) else (best_grid_result, None)
        summary_metrics['best_grid_params'] = best_grid_params
        summary_metrics['best_grid_score'] = best_grid_score

    if search_methods['bayesian_search']:
        logging.info("Running Bayesian Optimization...")
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense
        
        def create_model(input_shape):
            model = Sequential()
            model.add(Dense(128, input_dim=input_shape[0], activation='relu'))
            model.add(Dense(64, activation='relu'))
            model.add(Dense(1, activation='sigmoid'))
            model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
            return model
        
        best_bayesian_params = bayesian_optimization(numerical_data.shape[1], numerical_data.values, df['balanced_acc'].fillna(0).values, create_model, logging.getLogger('Bayesian'))
        summary_metrics['best_bayesian_params'] = best_bayesian_params


    if search_methods['hyperband_search']:
        logging.info("Running Hyperband Optimization...")
        best_hyperband_params = hyperband_optimization(numerical_data.shape[1], 2, numerical_data.values, df['balanced_acc'].fillna(0).values, logging.getLogger('Hyperband'))
        summary_metrics['best_hyperband_params'] = best_hyperband_params

    # Save results
    summary_file_path = save_json(summary_metrics, 'analysis/search', 'search_metrics')
    
    # Save best bit description
    save_best_bit_description(integrated_bit_desc, summary_metrics, file_prefix='best_bit_desc')

    logging.info(f"Search and save process completed. Summary file: {summary_file_path}")

# Example usage
root_dir = 'analysis'
search_and_save(root_dir)

