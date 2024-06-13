from qiskit import QuantumCircuit, Aer, transpile
from qiskit.circuit import Parameter
from qiskit.providers.aer import AerSimulator
from common_imports import *

class QuantumCircuitLayer:
    def __init__(self, n_qubits, backend='qasm_simulator'):
        """
        Initialize the QuantumCircuitLayer class.
        
        Parameters:
        n_qubits (int): Number of qubits in the circuit.
        backend (str): The backend simulator to use. Default is 'qasm_simulator'.
        """
        self.n_qubits = n_qubits
        self.circuit = QuantumCircuit(n_qubits)
        self.parameters = [Parameter(f'θ{i}') for i in range(self.n_qubits)]
        self.backend = Aer.get_backend(backend)
        
        # Console output for debugging
        print(f"QuantumCircuitLayer initialized with {n_qubits} qubits.")

    def apply_gate(self, gate_type, qubit_idx):
        """
        Apply a quantum gate to a specific qubit.
        
        Parameters:
        gate_type (str): The type of the gate ('x', 'y', 'z', 'h').
        qubit_idx (int): The index of the qubit to apply the gate to.
        """
        if gate_type == 'x':
            self.circuit.x(qubit_idx)
        elif gate_type == 'y':
            self.circuit.y(qubit_idx)
        elif gate_type == 'z':
            self.circuit.z(qubit_idx)
        elif gate_type == 'h':
            self.circuit.h(qubit_idx)
        else:
            print("Invalid gate type.")
            return
        
        # Console output for debugging
        print(f"Applied {gate_type}-gate to qubit {qubit_idx}.")

    def apply_rotation(self, qubit_idx):
        """
        Apply a rotation gate to a specific qubit.
        
        Parameters:
        qubit_idx (int): The index of the qubit to apply the rotation to.
        """
        self.circuit.rx(self.parameters[qubit_idx], qubit_idx)
        
        # Console output for debugging
        print(f"Applied rotation to qubit {qubit_idx} with parameter θ{qubit_idx}.")

    def run_circuit(self, parameter_values):
        """
        Run the quantum circuit with specific parameter values.
        
        Parameters:
        parameter_values (list): List of parameter values to be used in the circuit.
        
        Returns:
        dict: Results of the quantum circuit execution.
        """
        if len(parameter_values) != self.n_qubits:
            print("Parameter values do not match the number of qubits.")
            return
        
        # Bind parameters to values
        parameter_binds = {self.parameters[i]: parameter_values[i] for i in range(self.n_qubits)}
        
        # Transpile the circuit for the simulator
        t_qc = transpile(self.circuit.bind_parameters(parameter_binds), self.backend)
        
        # Run the circuit
        job = self.backend.run(t_qc)
        result = job.result().get_counts(self.circuit)
        
        # Console output for debugging
        print(f"Ran circuit with parameters {parameter_values}. Result: {result}")
        
        return result

# Example usage
'''
if __name__ == "__main__":
    qcl = QuantumCircuitLayer(2)
    qcl.apply_gate('x', 0)
    qcl.apply_rotation(1)
    qcl.run_circuit([0.5, 1.2])
'''
