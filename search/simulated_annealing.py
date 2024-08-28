import numpy as np
from neural_network import build_enhanced_nn
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space
from scipy.optimize import dual_annealing
import logging
import random

# Sample data for testing
X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def drunk_kangaroo_step(params, bounds, step_size=0.1):
    """
    Introduces randomness to the parameter set, simulating a 'drunk kangaroo' step.
    """
    new_params = []
    for i, (param, bound) in enumerate(zip(params, bounds)):
        if random.random() < 0.5:
            # Random jump within a step_size fraction of the parameter's range
            jump = (random.random() - 0.5) * step_size * (bound[1] - bound[0])
            new_param = param + jump
            # Ensure new_param is within bounds
            new_param = max(bound[0], min(new_param, bound[1]))
            new_params.append(new_param)
        else:
            new_params.append(param)
    return new_params

def simulated_annealing_optimization(input_shape, num_classes, x_train, y_train, build_fn, logger, kangaroo_step=True):
    def evaluate(params):
        num_layers, units_0, dropout_0, units_1, dropout_1, learning_rate, k, q, epsilon = params
        k = k_value_space[int(k)]
        q = q_value_space[int(q)]
        epsilon = epsilon_value_space[int(epsilon)]
        
        logger.debug(f"Evaluating with params: num_layers={num_layers}, units_0={units_0}, dropout_0={dropout_0}, "
                     f"units_1={units_1}, dropout_1={dropout_1}, learning_rate={learning_rate}, k={k}, q={q}, epsilon={epsilon}")
        
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
        
        logger.debug(f"Accuracy: {accuracy}")
        
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

    logger.debug("Starting Simulated Annealing Optimization with Drunk Kangaroo Steps")
    result = dual_annealing(evaluate, bounds)

    if kangaroo_step:
        logger.info("Introducing Drunk Kangaroo Steps...")
        for _ in range(10):  # Adjust the number of steps as needed
            params = drunk_kangaroo_step(result.x, bounds)
            new_score = evaluate(params)
            if new_score < result.fun:  # Better solution found
                result.x = params
                result.fun = new_score
                logger.info(f"New best found with Kangaroo Step: {params}, score: {-new_score}")

    best_params = result.x
    logger.info(f"Best Parameters: num_layers={best_params[0]}, units_0={best_params[1]}, dropout_0={best_params[2]}, "
                f"units_1={best_params[3]}, dropout_1={best_params[4]}, learning_rate={best_params[5]}, "
                f"k={k_value_space[int(best_params[6])]}, q={q_value_space[int(best_params[7])]}, "
                f"epsilon={epsilon_value_space[int(best_params[8])]} with accuracy: {-result.fun}")

    return {
        'num_layers': int(best_params[0]),
        'units_0': int(best_params[1]),
        'dropout_0': best_params[2],
        'units_1': int(best_params[3]),
        'dropout_1': best_params[4],
        'learning_rate': best_params[5],
        'k': k_value_space[int(best_params[6])],
        'q': q_value_space[int(best_params[7])],
        'epsilon': epsilon_value_space[int(best_params[8])],
        'accuracy': -result.fun
    }

if __name__ == "__main__":
    best_sa = simulated_annealing_optimization(X_train.shape[1], len(set(y_train)), X_train, y_train, build_enhanced_nn, logger)
    print("\nSummary Table")
    print("-------------")
    print(f"Best Parameters: {best_sa}")
    print(f"Best Accuracy: {best_sa['accuracy']}")
