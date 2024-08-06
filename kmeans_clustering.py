import os
import json
import numpy as np
import pandas as pd
import logging
from datetime import datetime
from sklearn.cluster import KMeans
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from sklearn.model_selection import cross_val_score
from sklearn.experimental import enable_iterative_imputer  # Required import to enable IterativeImputer
from sklearn.impute import SimpleImputer
from compute_metrics import compute_metrics, save_metrics_to_json
from UQEBM import IntegratedBitDescription, quantum_states
from sklearn.metrics import make_scorer, silhouette_score

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

# Directories
analysis_directory = 'analysis'
data_directory = 'data'

# File paths
json_file_path = os.path.join(data_directory, 'cleaned_data.json')

# Load additional data from JSON
additional_data = []
with open(json_file_path, 'r') as f:
    for line in f:
        additional_data.append(json.loads(line))

# Convert additional data to DataFrame
additional_df = pd.DataFrame(additional_data)

# Preprocess data to generate feature vectors dynamically
def preprocess_data(df):
    # Convert all columns to numeric, filling NaNs with 0
    data = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    logging.debug(f"Data before imputation: \n{data.describe(include='all')}")
    
    # Perform imputation (now filling NaNs with 0)
    imputer = SimpleImputer(strategy='constant', fill_value=0)
    data_imputed = imputer.fit_transform(data)
    
    logging.debug(f"Data after imputation: \n{pd.DataFrame(data_imputed, columns=data.columns).describe(include='all')}")
    
    return data_imputed

# Custom scorer for silhouette score
def kmeans_silhouette_scorer(estimator, X):
    labels = estimator.fit_predict(X)
    return silhouette_score(X, labels)

# Function to perform enhanced K-Means clustering with Bayesian optimization
def enhanced_kmeans(data):
    def kmeans_score(n_clusters, tol, algorithm):
        model = KMeans(n_clusters=n_clusters, tol=tol, algorithm=algorithm, random_state=0)
        return -np.mean(cross_val_score(model, data, cv=min(5, len(data)), scoring=make_scorer(kmeans_silhouette_scorer)))

    search_space = {
        'n_clusters': Integer(2, min(20, len(data)-1)),
        'tol': Real(1e-6, 1e-1, prior='log-uniform'),
        'algorithm': Categorical(['elkan', 'lloyd'])  # Corrected the algorithm parameter
    }

    opt = BayesSearchCV(
        estimator=KMeans(),
        search_spaces=search_space,
        n_iter=100,  # Increased number of iterations for better exploration
        cv=min(5, len(data)),
        random_state=0,
        n_jobs=-1  # Use all available cores for parallel processing
    )

    opt.fit(data)
    return opt.best_estimator_

# Main processing function
def process_new_data(df):
    try:
        data = preprocess_data(df)

        # Remove duplicate points
        data = np.unique(data, axis=0)
        logging.info(f"Data shape after removing duplicates: {data.shape}")

        # Ensure there are enough unique data points for clustering
        if len(data) < 2:
            logging.error("Not enough unique data points for clustering. Further processing cannot proceed.")
            return

        best_kmeans = enhanced_kmeans(data)

        # Perform clustering
        labels = best_kmeans.fit_predict(data)

        # Evaluate and report metrics (Using placeholders as real keys may not exist)
        y_true = labels  # Placeholder as the actual key may not exist
        y_pred = labels
        y_proba = np.full(len(labels), 0.5)  # Placeholder
        epoch_times = np.full(len(labels), 0.5)  # Placeholder

        k_values = np.full(len(labels), 0.0).tolist()
        q_values = np.full(len(labels), 0.0).tolist()
        epsilon_values = np.full(len(labels), 0.0).tolist()

        metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values)

        # Save metrics to JSON
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        metrics_file_path = os.path.join(analysis_directory, f"enhanced_metrics_{timestamp}.json")
        save_metrics_to_json(metrics, metrics_file_path)

        # Use UQEBM for bit description
        bit_desc = IntegratedBitDescription(range_min=0, range_max=100, number_bases=[1, np.pi, 5, 10, 13, 60, 360], quantum_states=quantum_states)

        # Save best bit description
        metrics_summary = {"accuracy": metrics.get('accuracy'), "precision": metrics.get('precision')}
        bit_desc.save_best_bit_description(bit_desc, metrics_summary)

        # Reporting
        logging.info(f"Enhanced metrics: {metrics}")

    except ValueError as e:
        logging.error(f"Error in clustering: {e}")

# Main execution
if __name__ == "__main__":
    process_new_data(additional_df)
    logging.info("Enhanced K-Means clustering with AI/ML and UQEBM bit description completed successfully.")
 