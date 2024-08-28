import pennylane as qml
from pennylane import numpy as np

def tune_quantum_circuit():
    """
    Tune a quantum circuit with different optimization levels using PennyLane.
    """
    results = {}

    # Define a quantum device with 2 qubits
    dev = qml.device('default.qubit', wires=2)

    # Define a quantum circuit
    @qml.qnode(dev)
    def circuit(theta):
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])  # Corrected the wires argument
        qml.RX(theta, wires=0)
        return qml.probs(wires=[0, 1])

    # Define the cost function
    def cost(theta):
        probs = circuit(theta)
        return probs[0]  # Minimize the probability of measuring |00>

    # Initialize the optimizer
    opt = qml.GradientDescentOptimizer(stepsize=0.1)
    theta = np.array(0.0, requires_grad=True)

    # Optimization loop
    for i in range(100):
        theta, cost_val = opt.step_and_cost(cost, theta)
        if i % 10 == 0:
            results[f"Step_{i}"] = cost_val
            print(f"Step {i}: cost = {cost_val:.4f}")

    return results

if __name__ == "__main__":
    tuning_results = tune_quantum_circuit()
    for step, cost_val in tuning_results.items():
        print(f"{step}: cost = {cost_val:.4f}")
