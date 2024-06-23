# Define the parameters for the Ant Colony Optimization algorithm in a dictionary.
# This structure allows for easy adjustment and testing of parameter impacts on the algorithm's performance.

aco_parameters = {
    'alpha': 2.75,       # Alpha (α): Increases the influence of pheromone trails in the decision-making process.
    'beta': 1.75,        # Beta (β): Balances the influence of heuristic information, useful in route decisions.
    'rho': 0.5,          # Rho (ρ): Defines the rate of pheromone evaporation, which prevents rapid convergence to a local optimum.
    'Q': 1.5,            # Q: Sets the quantity of pheromone deposited by ants, influencing the strength of the pheromone trail.
    'elite_factor': 7,   # Elite Factor: Amplifies the pheromone deposit on paths that are part of the globally best solution.
    'decay_factor': 0.025 # Decay Factor: Slows the decay of heuristics, maintaining their influence over longer periods.
}

# Example usage within the ACO algorithm:
def update_pheromones(pheromones, delta_pheromones):
    """
    Update the pheromone levels on the paths based on the current pheromones and the changes in pheromones
    (delta_pheromones) calculated after each ant's tour.

    Parameters:
    - pheromones (dict): Current pheromone levels on paths.
    - delta_pheromones (dict): Calculated pheromone increments based on the tours completed by all ants.
    """
    for path, current_pheromone in pheromones.items():
        # Apply the pheromone decay as per rho and add the delta pheromone for the path
        pheromones[path] = (1 - aco_parameters['rho']) * current_pheromone + delta_pheromones[path]

def calculate_transition_probabilities(pheromones, heuristic_info, allowed_paths):
    """
    Calculate the transition probabilities for moving from one point to another based on the current pheromone levels
    and heuristic information.

    Parameters:
    - pheromones (dict): Current pheromone levels on paths.
    - heuristic_info (dict): Problem-specific heuristic information (like inverse of distance).
    - allowed_paths (list): Paths that are available for traversal from the current node.
    """
    probabilities = {}
    total = sum((pheromones[path]**aco_parameters['alpha'] * heuristic_info[path]**aco_parameters['beta']) for path in allowed_paths)
    for path in allowed_paths:
        # The probability of choosing a path is proportional to the product of pheromone level and heuristic information raised to their respective powers
        probabilities[path] = (pheromones[path]**aco_parameters['alpha'] * heuristic_info[path]**aco_parameters['beta']) / total
    return probabilities

# Additional functions and algorithm implementation would follow similar patterns, utilizing the parameters from aco_parameters.
