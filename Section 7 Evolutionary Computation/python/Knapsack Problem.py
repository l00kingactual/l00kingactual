import pulp as plp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Define the data for the knapsack problem
values = [60, 100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290]
weights = [10, 20, 30, 15, 25, 35, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110]
capacity = 500

# Number of items
n_items = len(values)

# Define the problem
knapsack_problem = plp.LpProblem("Knapsack_Problem", plp.LpMaximize)

# Define the decision variables
x = [plp.LpVariable(f'x{i}', cat='Binary') for i in range(n_items)]

# Define the objective function
knapsack_problem += plp.lpSum([values[i] * x[i] for i in range(n_items)]), "Total_Value"

# Define the constraint
knapsack_problem += plp.lpSum([weights[i] * x[i] for i in range(n_items)]) <= capacity, "Total_Weight"

# Solver configuration
solver = plp.PULP_CBC_CMD(msg=False)

# Solve the problem initially to get the optimal solution
knapsack_problem.solve(solver)
selected_values = [values[i] if x[i].varValue == 1 else 0 for i in range(n_items)]
selected_items = [i+1 for i in range(n_items) if x[i].varValue == 1]
optimal_value = sum(selected_values)

# Initialize figure and axis
fig, ax = plt.subplots()
bars = ax.bar(range(1, n_items + 1), [0] * n_items, tick_label=[f"Item {i+1}" for i in range(n_items)])
ax.set_xlabel('Items')
ax.set_ylabel('Values')
ax.set_ylim(0, max(values) + 50)
ax.set_xlim(0, n_items + 1)
ax.set_title('Knapsack Problem Solution Iteration\nObjective: Maximize Total Value\nConstraint: Total Weight ≤ 500', fontsize=10)

# Function to update the bar plot
def update_bars(i):
    ax.clear()
    
    # Select the top i items based on values to simulate iteration
    sorted_indices = np.argsort(selected_values)[::-1]
    current_indices = sorted_indices[:i]
    current_items = [index + 1 for index in current_indices]
    current_values = [selected_values[index] for index in current_indices]
    
    bars = ax.bar(current_items, current_values, color=[plt.cm.viridis(index / n_items) for index in range(len(current_items))])
        
    ax.set_xlabel('Items')
    ax.set_ylabel('Values')
    ax.set_ylim(0, max(values) + 50)
    ax.set_xlim(0, n_items + 1)
    ax.set_title('Knapsack Problem Solution Iteration\nObjective: Maximize Total Value\nConstraint: Total Weight ≤ 500', fontsize=10)
    
    if i >= len(current_items):
        ax.bar(current_items, current_values, color='green')
        ax.text(n_items//2, max(values) + 20, f'Optimal Value: {optimal_value}', ha='center', fontsize=12)
    
    return bars

# Create animation
ani = animation.FuncAnimation(fig, update_bars, frames=n_items, interval=200, blit=False)

# Save the animation
ani.save('knapsack_animation_iterative.gif', writer='pillow')

plt.show()
