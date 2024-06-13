import numpy as np
import matplotlib.pyplot as plt

def apply_rule(rule_number, neighborhood):
    """Apply a given rule to a 3-cell neighborhood."""
    rule_binary = f"{rule_number:08b}"[::-1]
    index = int("".join(map(str, neighborhood)), 2)
    return int(rule_binary[index])

def update_state(state, rule_number):
    """Update the state of the cellular automaton based on the rule."""
    new_state = np.zeros_like(state)
    for i in range(1, len(state) - 1):
        neighborhood = state[i-1:i+2]
        new_state[i] = apply_rule(rule_number, neighborhood)
    return new_state

def run_eca(initial_state, rule_number, steps):
    """Run the elementary cellular automaton for a given number of steps."""
    state = initial_state
    history = [state]
    for _ in range(steps):
        state = update_state(state, rule_number)
        history.append(state)
    return history

def plot_eca(history, rule_number):
    """Plot the evolution of the elementary cellular automaton."""
    plt.figure(figsize=(12, 6))
    plt.imshow(history, cmap='binary')
    plt.title(f"Elementary Cellular Automaton (Rule {rule_number})")
    plt.xlabel("Cell Index")
    plt.ylabel("Time Step")
    plt.show()

# Parameters
initial_state = np.zeros(101, dtype=int)
initial_state[50] = 1  # Single 1 in the center
steps = 50

# Run and plot ECA for Rule 110
history = run_eca(initial_state, 110, steps)
plot_eca(history, 110)
