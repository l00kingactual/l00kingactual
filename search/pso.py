import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from pyswarm import pso
import random
import logging
from sklearn.metrics import accuracy_score, f1_score, log_loss

from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space

from compute_metrics import compute_metrics, save_metrics_to_json

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample data for testing (replace with complex synth data as the actual data)
X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)

# Dynamic Metric Selection
def select_metric(metric_name):
    if metric_name == "accuracy":
        return accuracy_score
    elif metric_name == "f1":
        return f1_score
    elif metric_name == "log_loss":
        return log_loss
    else:
        raise ValueError(f"Unknown metric: {metric_name}")

# Define the objective function for PSO with dynamic metrics
def objective(indices, metric_name="accuracy"):
    metric_function = select_metric(metric_name)

    k_index, q_index, epsilon_index = indices
    k = min(max(1, int(k_value_space[int(k_index)])), 10000)  # Ensure k is in a valid range
    q = min(max(1, int(q_value_space[int(q_index)])), 500)  # Ensure q is in a valid range
    epsilon = max(10, int(epsilon_value_space[int(epsilon_index)]))  # Ensure epsilon is in a valid range

    classifiers = {
        "RandomForest": RandomForestClassifier(n_estimators=k, max_depth=q, min_samples_split=epsilon, random_state=42),
        "GradientBoosting": GradientBoostingClassifier(n_estimators=k, max_depth=q, min_samples_split=epsilon, random_state=42),
        "LogisticRegression": LogisticRegression(C=epsilon / 100, max_iter=k, solver='lbfgs', random_state=42)
    }

    classifier_name = random.choice(list(classifiers.keys()))
    model = classifiers[classifier_name]

    scores = cross_val_score(model, X_train, y_train, scoring='accuracy')  # Modify scoring based on metric
    score = -np.mean(scores)  # Negate because PSO minimizes
    logger.info(f"Tested params: k={k}, q={q}, epsilon={epsilon}, score={-score}")
    return score

# Define the bounds for each parameter
lb = [0, 0, 0]
ub = [len(k_value_space) - 1, len(q_value_space) - 1, len(epsilon_value_space) - 1]

def run_pso_optimization(starting_params=None, metric_name="accuracy"):
    logger.info("Starting PSO optimization...")
    if starting_params:
        logger.info(f"Using starting params: {starting_params}")

    best_params_indices, _ = pso(objective, lb, ub, swarmsize=30, maxiter=50, args=(metric_name,))

    best_params = {
        'k': k_value_space[int(best_params_indices[0])],
        'q': q_value_space[int(best_params_indices[1])],
        'epsilon': epsilon_value_space[int(best_params_indices[2])]
    }

    logger.info(f"Best PSO Optimization: {best_params}")
    return best_params

if __name__ == "__main__":
    # Example of running PSO with accuracy as the metric
    best_params = run_pso_optimization(metric_name="accuracy")

    # Ensure metrics are computed and JSON is saved
    try:
        metrics = compute_metrics(y_train, y_train, y_train, [], [best_params['k']], [best_params['q']], [best_params['epsilon']])
        save_metrics_to_json(metrics, directory='analysis/pso_optimization')
        logger.info("Metrics successfully saved to JSON.")
    except Exception as e:
        logger.error(f"Failed to save metrics: {e}")
