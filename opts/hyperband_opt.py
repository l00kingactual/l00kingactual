from keras_tuner import Hyperband
import tensorflow as tf

from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space
from neural_network import build_enhanced_nn


def build_model(hp, input_shape, num_classes):
    num_layers = hp.Int('num_layers', 2, 10)
    units_0 = hp.Int('units_0', 16, 1024)
    dropout_0 = hp.Float('dropout_0', 0.0, 0.75)
    units_1 = hp.Int('units_1', 32, 512)
    dropout_1 = hp.Float('dropout_1', 0.0, 0.25)
    learning_rate = hp.Float('learning_rate', 1e-6, 1e-1)
    k = hp.Choice('k', k_value_space)
    q = hp.Choice('q', q_value_space)
    epsilon = hp.Choice('epsilon', epsilon_value_space)
    
    model = build_enhanced_nn(
        input_shape=(input_shape,),
        num_classes=num_classes,
        num_layers=num_layers,
        units_0=units_0,
        dropout_0=dropout_0,
        units_1=units_1,
        dropout_1=dropout_1,
        learning_rate=learning_rate,
        k=k,
        q=q,
        epsilon=epsilon
    )
    return model

def hyperband_optimization(input_shape, num_classes, x_train, y_train, logger):
    tuner = Hyperband(
        hypermodel=lambda hp: build_model(hp, input_shape, num_classes),
        objective='val_accuracy',
        max_epochs=30,
        directory='hyperband',
        project_name='hyperband_optimization'
    )

    logger.debug("Starting Hyperband Optimization")
    tuner.search(x_train, y_train, epochs=10, validation_split=0.2)

    best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]
    logger.debug(f"Best Hyperband Optimization: {best_hp.values}")
    return best_hp
