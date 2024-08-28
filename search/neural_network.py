import tensorflow as tf
import numpy as np
import pandas as pd
import time
import os
import json
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, roc_curve, auc, confusion_matrix, ConfusionMatrixDisplay
from imblearn.over_sampling import SMOTE
from sklearn.utils import class_weight
import matplotlib.pyplot as plt

from compute_metrics_clustering import save_metrics_with_timestamp, prepare_data_for_clustering
from compute_metrics import compute_metrics, save_metrics_to_json
from data_return_real_data_df import combined_df as real_data  # Correct import for real data
from data_return_df import combined_df as synthetic_data  # Correct import for synthetic data
from enhanced_nn import build_enhanced_nn

# Combine real and synthetic data
combined_df = pd.concat([real_data, synthetic_data], ignore_index=True)

from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space
from epsilon_greedy_vaule_space import epsilon_greedy_space
from quantum.quantum_layer import QuantumCircuitLayer

# Fetch the DataFrame
imported_df = combined_df

# Function to train the neural network
def train_neural_network(model, x_train, y_train, x_val, y_val, epochs=50, batch_size=32, class_weights=None):
    epoch_times = []
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    lr_scheduler = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)
    for epoch in range(epochs):
        start_time = time.time()
        model.fit(x_train, y_train, epochs=1, batch_size=batch_size, validation_data=(x_val, y_val), 
                  callbacks=[early_stopping, lr_scheduler], class_weight=class_weights)
        epoch_time = time.time() - start_time
        epoch_times.append(epoch_time)
    return model, epoch_times

def invert_metrics(metrics):
    inverted_metrics = {}
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            if key in ['accuracy', 'precision', 'recall', 'f1', 'balanced_acc', 'jaccard']:
                inverted_metrics[key] = 1 - value
            else:
                inverted_metrics[key] = value
        elif isinstance(value, list):
            inverted_metrics[key] = [1 - v if isinstance(v, (int, float)) and key in ['accuracy', 'precision', 'recall', 'f1', 'balanced_acc', 'jaccard'] else v for v in value]
        else:
            inverted_metrics[key] = value
    return inverted_metrics

from sklearn.metrics import roc_curve, auc, roc_auc_score
from sklearn.preprocessing import label_binarize

def analyze_model_performance(y_test, y_pred_proba, num_classes):
    # Binarize the output labels for multi-class ROC analysis
    y_test_binarized = label_binarize(y_test, classes=np.arange(num_classes))

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()

    for i in range(num_classes):
        fpr[i], tpr[i], _ = roc_curve(y_test_binarized[:, i], y_pred_proba[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

    # Plot all ROC curves
    plt.figure()
    colors = ['aqua', 'darkorange', 'cornflowerblue']
    for i, color in zip(range(num_classes), colors):
        plt.plot(fpr[i], tpr[i], color=color, lw=2, 
                 label=f'ROC curve (class {i}) (area = {roc_auc[i]:0.2f})')

    plt.plot([0, 1], [0, 1], 'k--', lw=2)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic for Multi-class')
    plt.legend(loc="lower right")
    plt.show()

    # Compute and display the confusion matrix
    y_pred = np.argmax(y_pred_proba, axis=1)
    conf_matrix = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=conf_matrix)
    disp.plot()
    plt.show()


if __name__ == "__main__":
    x_train = np.random.rand(250, 25)
    y_train = np.random.randint(0, 3, 250)
    x_test = np.random.rand(25, 25)
    y_test = np.random.randint(0, 3, 25)

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Address class imbalance using SMOTE
    smote = SMOTE(random_state=42)
    x_train_resampled, y_train_resampled = smote.fit_resample(x_train, y_train)

    # Ensure k, q, and epsilon value spaces have the same length as x_train and x_test
    total_samples = len(x_train_resampled) + len(x_test)
    k_values = np.array(k_value_space)[:total_samples]
    q_values = np.array(q_value_space)[:total_samples]
    epsilon_values = np.array(epsilon_value_space)[:total_samples]

    if len(k_values) < total_samples:
        k_values = np.pad(k_values, (0, total_samples - len(k_values)), 'constant')
    if len(q_values) < total_samples:
        q_values = np.pad(q_values, (0, total_samples - len(q_values)), 'constant')
    if len(epsilon_values) < total_samples:
        epsilon_values = np.pad(epsilon_values, (0, total_samples - len(epsilon_values)), 'constant')

    x_train_combined = np.hstack((x_train_resampled, k_values[:len(x_train_resampled)].reshape(-1, 1), q_values[:len(x_train_resampled)].reshape(-1, 1), epsilon_values[:len(x_train_resampled)].reshape(-1, 1)))
    x_test_combined = np.hstack((x_test, k_values[len(x_train_resampled):].reshape(-1, 1), q_values[len(x_train_resampled):].reshape(-1, 1), epsilon_values[len(x_train_resampled):].reshape(-1, 1)))

    input_shape = (x_train_combined.shape[1],)
    num_classes = len(np.unique(y_train_resampled))

    
    # Compute class weights for class imbalance handling
    class_weights = class_weight.compute_class_weight('balanced', classes=np.unique(y_train_resampled), y=y_train_resampled)
    class_weights_dict = dict(enumerate(class_weights))

    model = build_enhanced_nn(input_shape, num_classes, num_layers=5, units_0=256, dropout_0=0.3, units_1=128, dropout_1=0.3, learning_rate=1e-3)
    model.summary()

    model, epoch_times = train_neural_network(model, x_train_combined, y_train_resampled, x_test_combined, y_test, epochs=10, class_weights=class_weights_dict)

    y_pred_proba = model.predict(x_test_combined)

    # Analyze model performance for multi-class classification
    analyze_model_performance(y_test, y_pred_proba, num_classes)

    # Compute the metrics and then invert them
    metrics = compute_metrics(y_test, np.argmax(y_pred_proba, axis=1), y_pred_proba, epoch_times, k_values, q_values, epsilon_values)
    inverted_metrics = invert_metrics(metrics)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f'analysis/neural_network_v105/metrics_{current_time}.json'
    save_metrics_to_json(inverted_metrics, json_filename)

    # Clustering on Collected Metrics
    data = prepare_data_for_clustering([inverted_metrics])

    # Ensure data has more than one sample for clustering
    if data.shape[0] > 2:  # Ensure at least 3 samples for 3 clusters
        # Apply K-Means Clustering
        kmeans = KMeans(n_clusters=3, random_state=0)
        labels_kmeans = kmeans.fit_predict(data)
        silhouette_kmeans = silhouette_score(data, labels_kmeans)
        save_metrics_with_timestamp({"clustering_method": "KMeans", "silhouette_score": silhouette_kmeans}, 'analysis/neural_network_v105', 'kmeans_metrics')

        # Apply DBSCAN Clustering
        dbscan = DBSCAN(eps=0.5, min_samples=5)
        labels_dbscan = dbscan.fit_predict(data)
        silhouette_dbscan = silhouette_score(data, labels_dbscan) if len(set(labels_dbscan)) > 1 else -1
        save_metrics_with_timestamp({"clustering_method": "DBSCAN", "silhouette_score": silhouette_dbscan}, 'analysis/neural_network_v105', 'dbscan_metrics')

        # Apply Gaussian Mixture Model Clustering
        gmm = GaussianMixture(n_components=3, random_state=0)
        labels_gmm = gmm.fit_predict(data)
        silhouette_gmm = silhouette_score(data, labels_gmm)
        save_metrics_with_timestamp({"clustering_method": "GMM", "silhouette_score": silhouette_gmm}, 'analysis/neural_network_v105', 'gmm_metrics')
    else:
        print("Not enough samples for clustering. Skipping clustering step.")

    print("Clustering analysis completed and saved.")
