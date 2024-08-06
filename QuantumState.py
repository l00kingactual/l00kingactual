import numpy as np

class QuantumState:
    def __init__(self, state_vector):
        self.state_vector = state_vector

    def unitary_evolve(self, H, t):
        # Unitary evolution of the state
        evolution_operator = np.exp(-1j * H * t)
        self.state_vector = np.dot(evolution_operator, self.state_vector)

    def measure(self):
        # Simulate measurement and wave function collapse
        probabilities = np.abs(self.state_vector)**2
        outcome = np.random.choice(range(len(probabilities)), p=probabilities)
        # Collapse the wave function to the measured state
        new_state = np.zeros_like(self.state_vector)
        new_state[outcome] = 1
        self.state_vector = new_state
        return outcome
