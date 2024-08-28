# hyperparameter_config.py

# This configuration file defines the ranges for hyperparameters
# used for tuning AI/ML models. These ranges will be used to explore
# different combinations of hyperparameters to find the optimal settings
# for the models.

HYPERPARAMETERS = {
    'learning_rate': [0.0001, 0.001, 0.01, 0.000001, 0.002, 0.003, 0.004, 0.05],
    'batch_size': [16, 32, 64, 128, 256, 512, 1024, 2048, 8192],
    'num_epochs': [50, 100, 150, 200, 250, 500, 750, 1000],
    'num_layers': [2, 3, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096],
    'hidden_units': [64, 128, 256, 512, 1024, 2048, 4096],
    'dropout_rate': [0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007],
    # Add a key for the best hyperparameters
    'best_hparams': {
        'learning_rate': 0.0001,
        'batch_size': 64,
        'num_epochs': 500,
        'num_layers': 8,
        'hidden_units': 256,
        'dropout_rate': 0.0005
    }
}
