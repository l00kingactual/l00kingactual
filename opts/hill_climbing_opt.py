import random
from neural_network import build_enhanced_nn
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space

import numpy as np

def hill_climbing_optimization(input_shape, num_classes, x_train, y_train, build_fn, logger, max_iter=100):
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
        return accuracy

    params = [random.randint(2, 10), random.randint(16, 1024), random.uniform(0.0, 0.75),
              random.randint(32, 512), random.uniform(0.0, 0.25), random.uniform(1e-6, 1e-1),
              random.choice(k_value_space), random.choice(q_value_space), random.choice(epsilon_value_space)]
    best_score = evaluate(params)

    logger.debug("Starting Hill Climbing Optimization")
    for _ in range(max_iter):
        new_params = [param + random.uniform(-0.1, 0.1) if isinstance(param, float) else param + random.randint(-1, 1) for param in params]
        new_score = evaluate(new_params)
        if new_score > best_score:
            params, best_score = new_params, new_score
            logger.debug(f"New best score: {best_score}")

    logger.debug(f"Best Hill Climbing Optimization: {params}")
    return params
