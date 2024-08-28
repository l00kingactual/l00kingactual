import json
import os
import numpy as np
import tensorflow as tf
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold, KFold, LeaveOneOut, GroupKFold, TimeSeriesSplit, train_test_split
from sklearn.datasets import load_iris
from sklearn.exceptions import NotFittedError
from datetime import datetime

from compute_metrics import compute_metrics, save_metrics_to_json
from neural_network import build_enhanced_nn as NeuralNetworkModel
from search.bayesian import bayesian_optimization

# Example configurations (idea space flags)
use_cv = True
use_stratified = True
use_leave_one_out = False
use_group_cv = False
use_time_series_split = False
use_random_search = False
parallelize_search = True
use_custom_scoring = False
refit_best_model = True
use_verbose_output = True
use_error_score_raise = False
shuffle_data = True

# Custom wrapper to mimic KerasClassifier functionality
class KerasClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, build_fn=None, **params):
        self.build_fn = build_fn
        self.params = params
        self.model = None
        self.classes_ = None

    def set_params(self, **params):
        self.params.update(params)
        return self

    def build_model(self):
        try:
            input_shape = (4,)  # Example input shape for the Iris dataset
            num_classes = 3  # Number of classes in the Iris dataset

            # Log the parameters used to build the model
            print(f"Building model with parameters: {self.params}")

            model = self.build_fn(
                input_shape=input_shape,
                num_classes=num_classes,
                **self.params
            )

            print(f"Model built successfully with parameters: {self.params}")
            return model
        except Exception as e:
            print(f"Error building the model with parameters: {self.params}")
            raise e

    def fit(self, X, y, **fit_params):
        self.model = self.build_model()
        self.model.fit(X, y, **fit_params)
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        if self.model is None:
            raise NotFittedError("This KerasClassifier instance is not fitted yet.")
        return np.argmax(self.model.predict(X), axis=-1)

    def predict_proba(self, X):
        if self.model is None:
            raise NotFittedError("This KerasClassifier instance is not fitted yet.")
        return self.model.predict(X)

    def score(self, X, y):
        return np.mean(self.predict(X) == y)


# Function to select search strategy based on parameter space size
def select_search_strategy(parameter_space_size):
    if parameter_space_size <= 100:
        return 'grid'
    elif 100 < parameter_space_size <= 1000:
        return 'random'
    else:
        return 'bayesian'

# Function to run search optimization
def run_search_optimization(X_train, y_train, search_strategy):
    param_grid = {
        'dropout_0': [0.1, 0.2, 0.3],
        'dropout_1': [0.1, 0.2, 0.3],
        'learning_rate': [0.001, 0.002, 0.003],
        'num_layers': [6, 7, 8],
        'units_0': [400, 450, 500],
        'units_1': [300, 350, 400]
    }
    
    parameter_space_size = np.prod([len(values) for values in param_grid.values()])
    search_strategy = select_search_strategy(parameter_space_size)
    
    # Set up cross-validation strategy based on flags
    if use_leave_one_out:
        cv_strategy = LeaveOneOut()
    elif use_group_cv:
        cv_strategy = GroupKFold(n_splits=5)
    elif use_time_series_split:
        cv_strategy = TimeSeriesSplit(n_splits=5)
    elif use_stratified:
        cv_strategy = StratifiedKFold(n_splits=5, shuffle=shuffle_data)
    else:
        cv_strategy = KFold(n_splits=5, shuffle=shuffle_data)

    if search_strategy == 'grid':
        model = KerasClassifier(build_fn=NeuralNetworkModel)
        grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='accuracy' if not use_custom_scoring else 'f1',
                                   cv=cv_strategy, n_jobs=-1 if parallelize_search else 1, verbose=2 if use_verbose_output else 0,
                                   refit=refit_best_model, error_score='raise' if use_error_score_raise else 'warn')
        grid_search.fit(X_train, y_train)
        best_params = grid_search.best_params_

    elif search_strategy == 'random':
        model = KerasClassifier(build_fn=NeuralNetworkModel)
        random_search = RandomizedSearchCV(estimator=model, param_distributions=param_grid, scoring='accuracy' if not use_custom_scoring else 'f1',
                                           cv=cv_strategy, n_iter=100, n_jobs=-1 if parallelize_search else 1, verbose=2 if use_verbose_output else 0,
                                           refit=refit_best_model, error_score='raise' if use_error_score_raise else 'warn')
        random_search.fit(X_train, y_train)
        best_params = random_search.best_params_

    elif search_strategy == 'bayesian':
        best_params = bayesian_optimization(X_train, y_train, model.build_model)

    else:
        raise ValueError("Invalid search strategy selected.")

    return best_params

# Function to build the enhanced neural network
def build_enhanced_nn(input_shape, num_classes, dropout_0=0.2, dropout_1=0.2, learning_rate=0.001, num_layers=6, units_0=400, units_1=300):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=units_0, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dropout(rate=dropout_0),
        # Add additional layers based on num_layers, units_1, etc.
        tf.keras.layers.Dense(units=units_1, activation='relu'),
        tf.keras.layers.Dropout(rate=dropout_1),
        tf.keras.layers.Dense(units=num_classes, activation='softmax')
    ])

    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# Main function to execute search and train model
def main():
    try:
        # Load the Iris dataset
        data = load_iris()
        X, y = data.data, data.target

        # Split the data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        # Determine the optimal search strategy based on parameter space size
        search_strategy = 'grid'  # Start with grid, logic will adjust if needed

        # Run the optimization
        best_params = run_search_optimization(X_train, y_train, search_strategy)

        # Train the final model with the best parameters
        final_model = NeuralNetworkModel(input_shape=(4,), num_classes=3, **best_params)
        final_model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=20)

        # Make predictions
        y_pred = final_model.predict(X_val).argmax(axis=1)
        y_proba = final_model.predict(X_val)

        # Compute and save metrics
        epoch_times = [0.2] * len(y_pred)
        k_values = [1] * len(y_pred)
        q_values = [0.5] * len(y_pred)
        epsilon_values = [0.1] * len(y_pred)

        metrics = compute_metrics(y_val, y_pred, y_proba, epoch_times, k_values, q_values, epsilon_values)
        save_metrics_to_json(metrics, directory='analysis/optimized_model')

        print("Optimization completed successfully.")

    except Exception as e:
        print(f"An error occurred during the optimization process: {e}")
        raise

if __name__ == "__main__":
    main()
