import os
import tensorflow as tf
from keras_tuner import RandomSearch
import time

def build_enhanced_nn(input_shape, num_classes, num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate, k, q, epsilon):
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.InputLayer(shape=input_shape))
    model.add(tf.keras.layers.Dense(units_0, activation='relu'))
    model.add(tf.keras.layers.Dropout(dropout_0))

    for _ in range(num_layers - 2):
        model.add(tf.keras.layers.Dense(units_1, activation='relu'))
        model.add(tf.keras.layers.Dropout(dropout_1))

    model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

def perform_hyperparameter_tuning(model_builder, input_shape, num_classes, x_train, y_train):
    def build_model(hp):
        return model_builder(
            input_shape=input_shape,
            num_classes=num_classes,
            num_layers=hp.Int('num_layers', 2, 5, step=1),
            units_0=hp.Int('units_0', 32, 256, step=32),
            dropout_0=hp.Float('dropout_0', 0.0, 0.5, step=0.1),
            units_1=hp.Int('units_1', 32, 256, step=32),
            dropout_1=hp.Float('dropout_1', 0.0, 0.5, step=0.1),
            learning_rate=hp.Float('learning_rate', 1e-4, 1e-2, sampling='log')
        )

    tuner = RandomSearch(
        build_model,
        objective='val_accuracy',
        max_trials=512,
        executions_per_trial=1,
        directory='hyperparameter_tuning',
        project_name='enhanced_bit_description'
    )
    tuner.search(x_train, y_train, epochs=500, validation_split=0.2)
    return tuner

def train_neural_network(model, x_train, y_train, epochs=500, batch_size=16):
    epoch_times = []
    for epoch in range(epochs):
        start_time = time.time()
        model.fit(x_train, y_train, epochs=1, batch_size=batch_size, validation_split=0.2)
        epoch_time = time.time() - start_time
        epoch_times.append(epoch_time)
    return model, epoch_times

def save_model_snapshots(model, epochs, directory):
    os.makedirs(directory, exist_ok=True)
    for epoch in range(epochs):
        model.save(os.path.join(directory, f'model_epoch_{epoch}.keras'))
        print(f"Saved model snapshot for epoch {epoch} at {directory}/model_epoch_{epoch}.keras")
