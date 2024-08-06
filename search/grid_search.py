import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space

# Sample data for testing (replace with your actual data)
X_train = np.random.rand(100, 10)
y_train = np.random.randint(0, 2, 100)

def objective(k, q, epsilon):
    k = min(max(1, int(k)), 1000)  # Ensure k is in a valid range
    q = min(max(1, int(q)), 50)  # Ensure q is in a valid range
    epsilon = max(2, int(epsilon))  # Ensure min_samples_split is at least 2

    model = RandomForestClassifier(n_estimators=k, max_depth=q, min_samples_split=epsilon, random_state=42)
    accuracy = cross_val_score(model, X_train, y_train, scoring='accuracy').mean()
    return accuracy

def run_grid_search_optimization():
    best_score = 0.0
    best_params = None

    for k in k_value_space:
        for q in q_value_space:
            for epsilon in epsilon_value_space:
                score = objective(k, q, epsilon)
                if score > best_score:
                    best_score = score
                    best_params = {'k': k, 'q': q, 'epsilon': epsilon}
                    print(f"New best score: {best_score} with params: {best_params}")

    print(f"Best Grid Search Optimization: {best_params}")
    return best_params
