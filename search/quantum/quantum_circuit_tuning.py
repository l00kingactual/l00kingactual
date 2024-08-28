import pennylane as qml
from pennylane import numpy as np
from skopt import gp_minimize
from skopt.space import Real

# Define quantum circuit functions
def qaoa_circuit(params, wires):
    for i in range(len(wires)):
        qml.RX(2 * params[0], wires=i)
        qml.CNOT(wires=[i, (i+1) % len(wires)])
    for i in range(len(wires)):
        qml.RX(2 * params[1], wires=i)

def vqe_circuit(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[1])
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0) @ qml.PauliZ(1))

def quantum_kernel_circuit(params, x1, x2):
    qml.Hadamard(wires=0)
    qml.RX(params[0] * (x1 - x2), wires=0)
    return qml.probs(wires=0)

def qpca_circuit(params, wires):
    qml.Hadamard(wires=0)
    qml.RX(params[0], wires=wires[0])
    qml.CNOT(wires=[0, 1])
    return qml.probs(wires=[0, 1])

def qnn_circuit(params, wires):
    qml.RX(params[0], wires=wires[0])
    qml.RY(params[1], wires=wires[1])
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

def grover_operator(params, wires):
    qml.Hadamard(wires=wires)
    qml.PauliX(wires=wires)
    qml.Hadamard(wires=wires)
    qml.PauliX(wires=wires)

def amplitude_amplification_circuit(params, wires):
    qml.Hadamard(wires=wires)
    qml.RX(params[0], wires=wires)
    qml.RY(params[1], wires=wires)

def qft_circuit(params, wires):
    qml.Hadamard(wires=wires[0])
    for i in range(1, len(wires)):
        qml.CNOT(wires=[wires[0], wires[i]])
        qml.RZ(params[i], wires=wires[i])

# Circuit Selector
def quantum_circuit_selector(circuit_type, params, wires):
    if circuit_type == "qaoa":
        qaoa_circuit(params, wires)
    elif circuit_type == "vqe":
        return vqe_circuit(params, wires)
    elif circuit_type == "quantum_kernel":
        x1, x2 = params[-2], params[-1]
        return quantum_kernel_circuit(params[:-2], x1, x2)
    elif circuit_type == "qpca":
        return qpca_circuit(params, wires)
    elif circuit_type == "qnn":
        return qnn_circuit(params, wires)
    elif circuit_type == "grover":
        grover_operator(params, wires)
    elif circuit_type == "amplitude_amplification":
        amplitude_amplification_circuit(params, wires)
    elif circuit_type == "qft":
        qft_circuit(params, wires)
    else:
        raise ValueError("Unknown circuit type")

def tune_quantum_circuit(circuit_type="qaoa"):
    results = {}

    # Define a quantum device with 2 qubits
    dev = qml.device('default.qubit', wires=2)

    @qml.qnode(dev)
    def circuit(theta, phi):
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0, 1])
        quantum_circuit_selector(circuit_type, [theta, phi], wires=[0, 1])
        return qml.probs(wires=[0, 1])

    def cost_forward(theta):
        probs = circuit(theta, theta)
        return probs[0]  # Return the ArrayBox directly

    def cost_backward(phi):
        probs = circuit(phi, phi)
        return probs[1]  # Return the ArrayBox directly

    opt = qml.GradientDescentOptimizer(stepsize=0.1)
    theta = np.array(0.0, requires_grad=True)
    phi = np.array(0.0, requires_grad=True)

    for i in range(100):
        theta, cost_val_forward = opt.step_and_cost(cost_forward, theta)
        phi, cost_val_backward = opt.step_and_cost(cost_backward, phi)
        
        if i % 10 == 0:
            results[f"Step_{i}"] = {
                "cost_forward": cost_val_forward,
                "cost_backward": cost_val_backward
            }
            print(f"Step {i}: cost_forward = {cost_val_forward:.4f}, cost_backward = {cost_val_backward:.4f}")

    def objective(params):
        theta, phi = params
        total_cost = cost_forward(theta) + cost_backward(phi)
        return float(total_cost)  # Convert to a float scalar

    search_space = [Real(-np.pi, np.pi, name='theta'), Real(-np.pi, np.pi, name='phi')]
    result = gp_minimize(objective, search_space, n_calls=50, random_state=42)

    optimal_theta = result.x[0]
    optimal_phi = result.x[1]

    print(f"Optimal theta: {optimal_theta:.4f}, Optimal phi: {optimal_phi:.4f}")

    results["Optimal Parameters"] = {
        "theta": optimal_theta,
        "phi": optimal_phi
    }

    return results

if __name__ == "__main__":
    circuit_type = "qaoa"  # Select the quantum circuit type
    tuning_results = tune_quantum_circuit(circuit_type)
    for step, costs in tuning_results.items():
        if step != "Optimal Parameters":
            print(f"{step}: cost_forward = {costs['cost_forward']:.4f}, cost_backward = {costs['cost_backward']:.4f}")
    print(f"Optimal Parameters: {tuning_results['Optimal Parameters']}")
