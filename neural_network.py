import tensorflow as tf
import numpy as np
import pandas as pd
import time
import os
import json
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from compute_metrics import compute_metrics, save_metrics_to_json
from data_return_df import df as imported_df
from q_value_space import q_value_space
from k_value_space import k_value_space
from epsilon_value_space import epsilon_value_space
from epsilon_greedy import epsilon_greedy

def build_enhanced_nn(input_shape, num_classes, num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate):
    inputs = tf.keras.layers.Input(shape=input_shape)
    x = tf.keras.layers.Dense(units_0, activation='relu')(inputs)
    x = tf.keras.layers.Dropout(dropout_0)(x)

    # Implementing "sine wave" architecture with additional trigonometric functions
    for i in range(num_layers - 2):
        if i % 4 == 0:
            units = units_0 // 2
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Lambda(lambda x: tf.sin(x))(x)
        elif i % 4 == 1:
            units = units_1
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Lambda(lambda x: tf.cos(x))(x)
        elif i % 4 == 2:
            units = units_1 // 2
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Lambda(lambda x: tf.tan(x))(x)
        else:
            units = units_0
            x = tf.keras.layers.Dense(units, activation='relu')(x)
            x = tf.keras.layers.Dropout(dropout_1)(x)

    outputs = tf.keras.layers.Dense(num_classes, activation='softmax')(x)

    model = tf.keras.models.Model(inputs, outputs)
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def train_neural_network(model, x_train, y_train, x_val, y_val, epochs=50, batch_size=32):
    epoch_times = []
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    lr_scheduler = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)
    for epoch in range(epochs):
        start_time = time.time()
        model.fit(x_train, y_train, epochs=1, batch_size=batch_size, validation_data=(x_val, y_val), callbacks=[early_stopping, lr_scheduler])
        epoch_time = time.time() - start_time
        epoch_times.append(epoch_time)
    return model, epoch_times

def save_model_snapshots(model, epochs, directory):
    os.makedirs(directory, exist_ok=True)
    for epoch in range(epochs):
        model.save(os.path.join(directory, f'model_epoch_{epoch}.keras'))
        print(f"Saved model snapshot for epoch {epoch} at {directory}/model_epoch_{epoch}.keras")

def compile_data_to_df(imported_df, metrics, k_values, q_values, epsilon_values):
    # Adding scalar metrics to the DataFrame
    for key, value in metrics.items():
        if isinstance(value, (int, float)):
            imported_df[key] = value

    # Handling array-like metrics
    conf_matrix = metrics.get('conf_matrix', None)
    if conf_matrix is not None:
        imported_df['conf_matrix'] = [conf_matrix] * len(imported_df)

    # Assuming there is an appropriate column to map k, q, and epsilon values
    mapping_column = 'appropriate_column'  # Replace with actual column name
    k_values_dict = {i: k for i, k in enumerate(k_values)}
    q_values_dict = {i: q for i, q in enumerate(q_values)}
    epsilon_values_dict = {i: epsilon for i, epsilon in enumerate(epsilon_values)}

    imported_df['k_value'] = imported_df[mapping_column].map(k_values_dict)
    imported_df['q_value'] = imported_df[mapping_column].map(q_values_dict)
    imported_df['epsilon_value'] = imported_df[mapping_column].map(epsilon_values_dict)

    print("Compiled DataFrame:")
    print(imported_df.head())  # Debugging print
    return imported_df

if __name__ == "__main__":
    x_train = np.random.rand(100, 10)
    y_train = np.random.randint(0, 3, 100)
    x_test = np.random.rand(20, 10)
    y_test = np.random.randint(0, 3, 20)

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    # Ensure k, q, and epsilon value spaces have the same length as x_train and x_test
    total_samples = len(x_train) + len(x_test)
    k_values = np.array(k_value_space)[:total_samples]
    q_values = np.array(q_value_space)[:total_samples]
    epsilon_values = np.array(epsilon_value_space)[:total_samples]

    if len(k_values) < total_samples:
        k_values = np.pad(k_values, (0, total_samples - len(k_values)), 'constant')
    if len(q_values) < total_samples:
        q_values = np.pad(q_values, (0, total_samples - len(q_values)), 'constant')
    if len(epsilon_values) < total_samples:
        epsilon_values = np.pad(epsilon_values, (0, total_samples - len(epsilon_values)), 'constant')

    x_train_combined = np.hstack((x_train, k_values[:len(x_train)].reshape(-1, 1), q_values[:len(x_train)].reshape(-1, 1), epsilon_values[:len(x_train)].reshape(-1, 1)))
    x_test_combined = np.hstack((x_test, k_values[len(x_train):].reshape(-1, 1), q_values[len(x_train):].reshape(-1, 1), epsilon_values[len(x_train):].reshape(-1, 1)))

    input_shape = (x_train_combined.shape[1],)
    num_classes = len(np.unique(y_train))

    model = build_enhanced_nn(input_shape, num_classes, num_layers=5, units_0=256, dropout_0=0.3, units_1=128, dropout_1=0.3, learning_rate=1e-3)
    model.summary()

    model, epoch_times = train_neural_network(model, x_train_combined, y_train, x_test_combined, y_test, epochs=10)

    y_pred = model.predict(x_test_combined).argmax(axis=1)
    y_proba = model.predict(x_test_combined)
    metrics = compute_metrics(y_test, y_pred, y_proba, epoch_times)

    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_filename = f'analysis/neural_network/neural_network_meaningful_metrics_{current_time}.json'
    save_metrics_to_json(metrics, json_filename)

    print(f"Model evaluation metrics saved to {json_filename}")

    df = compile_data_to_df(imported_df, metrics, k_values, q_values, epsilon_values)
    csv_filename = f'analysis/neural_network/compiled_data_{current_time}.csv'
    df.to_csv(csv_filename, index=False)

    print(f"Compiled data saved to {csv_filename}")
