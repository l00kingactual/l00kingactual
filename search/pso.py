from pyswarm import pso
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space

# Sample data for testing
X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)

# Define the objective function
def objective(indices):
    k_index, q_index, epsilon_index = indices
    k = min(max(1, int(k_value_space[int(k_index)])), 1000)  # Ensure k is in a valid range
    q = min(max(1, int(q_value_space[int(q_index)])), 50)  # Ensure q is in a valid range
    epsilon = max(2, int(epsilon_value_space[int(epsilon_index)]))  # Ensure min_samples_split is at least 2

    model = RandomForestClassifier(n_estimators=k, max_depth=q, min_samples_split=epsilon, random_state=42)
    return -np.mean(cross_val_score(model, X_train, y_train, scoring='accuracy'))

# Define the bounds for each parameter
lb = [0, 0, 0]
ub = [len(k_value_space) - 1, len(q_value_space) - 1, len(epsilon_value_space) - 1]

def run_pso_optimization():
    # Perform Particle Swarm Optimization
    best_params_indices, _ = pso(objective, lb, ub, swarmsize=20, maxiter=30)

    best_params = {
        'k': k_value_space[int(best_params_indices[0])],
        'q': q_value_space[int(best_params_indices[1])],
        'epsilon': epsilon_value_space[int(best_params_indices[2])]
    }

    print(best_params)
    return best_params
