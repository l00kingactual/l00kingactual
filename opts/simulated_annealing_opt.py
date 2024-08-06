import numpy as np
import random
from neural_network import build_enhanced_nn
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space
import random
from scipy.optimize import dual_annealing

def simulated_annealing_optimization(input_shape, num_classes, x_train, y_train, build_fn, logger):
    def evaluate(params):
        num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate, k, q, epsilon = params
        model = build_fn(
            input_shape=(input_shape,),
            num_classes=num_classes,
            num_layers=int(num_layers),
            units_0=int(units_0),
            dropout_0=dropout_0,
            units_1=int(units_1),
            dropout_1=dropout_1,
            learning_rate=learning_rate,
            k=k,
            q=q,
            epsilon=epsilon
        )
        history = model.fit(x_train, y_train, epochs=10, validation_split=0.2, verbose=0)
        accuracy = history.history['val_accuracy'][-1]
        return -accuracy

    bounds = [
        (2, 10),  # num_layers
        (16, 1024),  # units_0
        (0.0, 0.75),  # dropout_0
        (32, 512),  # units_1
        (0.0, 0.25),  # dropout_1
        (1e-6, 1e-1),  # learning_rate
        (0, len(k_value_space) - 1),  # k
        (0, len(q_value_space) - 1),  # q
        (0, len(epsilon_value_space) - 1)  # epsilon
    ]

    logger.debug("Starting Simulated Annealing Optimization")
    result = dual_annealing(evaluate, bounds)

    logger.debug(f"Best Simulated Annealing Optimization: {result}")
    return result
