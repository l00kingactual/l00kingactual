import os
import sys
import numpy as np
from decimal import Decimal

# Adjust the system path to import from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import necessary functions and classes from UQEBM.py
from UQEBM import EnhancedBitDescription, IntegratedBitDescription, encode_quantum_bit, decode_quantum_bit, save_best_bit_description, load_previous_best, compute_metrics, save_metrics_to_json
from quantum_states import quantum_states

class Environment:
    def __init__(self, temperature, humidity, daylight, wind, tide):
        self.temperature = temperature
        self.humidity = humidity
        self.daylight = daylight
        self.wind = wind
        self.tide = tide

        # Initialize BitDescription and IntegratedSystem
        self.bit_desc = IntegratedBitDescription(range_min=0, range_max=100, number_bases=[1, np.pi, 5, 10, 13, 60, 360], quantum_states=quantum_states)

    def get_environment_vector(self):
        return np.array([self.temperature, self.humidity, self.daylight, self.wind, self.tide], dtype=np.float64)

    def transform_environment(self):
        env_vector = self.get_environment_vector()
        env_bit_vectors = [self.bit_desc.decimal_to_bit(Decimal(float(value))) for value in env_vector]
        transformed_env = [self.bit_desc.bit_to_decimal(bit_vector) for bit_vector in env_bit_vectors]
        return np.array(transformed_env)

# Example usage
if __name__ == '__main__':
    env = Environment(temperature=25, humidity=70, daylight=12, wind=5, tide=2)
    transformed_env = env.transform_environment()
    print(f"Transformed Environment: {transformed_env}")
