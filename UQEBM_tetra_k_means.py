import os
import glob
import json
import logging
from decimal import Decimal
import numpy as np
from datetime import datetime
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from compute_metrics import compute_metrics, save_metrics_to_json, read_metrics_from_directory
from UQEBM import IntegratedBitDescription, save_best_bit_description
from data_return_df import create_dataframe_from_json

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def perform_clustering(data, n_clusters=3):
    if data.shape[0] < 3:
        logging.error("Not enough samples for clustering. Skipping clustering.")
        return []

    imputer = SimpleImputer(strategy='mean')
    data_imputed = imputer.fit_transform(data)
    
    if data_imputed.shape[0] < 3:
        logging.error("Not enough samples for clustering after imputation. Skipping clustering.")
        return []

    # Use advanced clustering algorithm
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_imputed)
    
    # Adjust n_components based on the dataset size
    n_components = min(10, scaled_data.shape[0], scaled_data.shape[1])
    pca = PCA(n_components=n_components)
    reduced_data = pca.fit_transform(scaled_data)
    
    gmm = GaussianMixture(n_components=n_clusters, random_state=0)
    gmm.fit(reduced_data)
    cluster_centers = gmm.means_
    best_cluster_index = np.argmax([np.mean(center) for center in cluster_centers])
    best_cluster_metrics = cluster_centers[best_cluster_index]

    logging.debug(f"Cluster centers: {cluster_centers}")
    logging.debug(f"Best cluster index: {best_cluster_index}")
    logging.debug(f"Best cluster metrics: {best_cluster_metrics}")

    return best_cluster_metrics.tolist()

def main():
    directory = 'analysis/'
    df = create_dataframe_from_json(directory)

    if not df.empty:
        integrated_bit_desc = IntegratedBitDescription(range_min=0, range_max=100, number_bases=[360, 60, 50], quantum_states={})
        numerical_data = df.select_dtypes(include=[np.number])

        if not numerical_data.empty:
            best_cluster_metrics = perform_clustering(numerical_data, n_clusters=3)
            logging.info(f"Best Cluster Metrics: {best_cluster_metrics}")

            y_true = [0, 1, 0, 1, 1, 0]  # Example values
            y_pred = [0, 0, 1, 1, 0, 1]  # Example values
            y_proba = [[0.8, 0.2], [0.3, 0.7], [0.6, 0.4], [0.4, 0.6], [0.9, 0.1], [0.2, 0.8]]  # Example values
            epoch_times = [0.1, 0.2, 0.15, 0.12, 0.18, 0.22]  # Example epoch times

            k_values = df['k_values'] if 'k_values' in df else []
            q_values = df['q_values'] if 'q_values' in df else []
            epsilon_values = df['epsilon_values'] if 'epsilon_values' in df else []

            # Ensure values are lists
            k_values = k_values.tolist() if isinstance(k_values, (pd.Series, np.ndarray)) else k_values
            q_values = q_values.tolist() if isinstance(q_values, (pd.Series, np.ndarray)) else q_values
            epsilon_values = epsilon_values.tolist() if isinstance(epsilon_values, (pd.Series, np.ndarray)) else epsilon_values

            metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values)

            summary_metrics = {
                'best_cluster_metrics': best_cluster_metrics,
                'metrics': metrics
            }

            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            summary_file_path = os.path.join('analysis/UQEBM_tetra_k_means', f'summary_metrics_{current_time}.json')

            with open(summary_file_path, 'w') as summary_file:
                json.dump(summary_metrics, summary_file)

            logging.info(f"Summary metrics saved to {summary_file_path}")
        else:
            logging.error("Numerical data is empty after filtering.")
    else:
        logging.error("DataFrame is empty. No data to process.")

if __name__ == "__main__":
    main()
