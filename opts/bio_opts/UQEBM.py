import numpy as np
import json
import os
from datetime import datetime
from decimal import Decimal, getcontext
import logging

from compute_metrics import compute_metrics, save_metrics_to_json
from quantum_states import quantum_states

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

getcontext().prec = 100

class EnhancedBitDescription:
    def __init__(self, range_min, range_max, number_bases):
        self.range_min = Decimal(range_min)
        self.range_max = Decimal(range_max)
        self.number_bases = [Decimal(b) for b in number_bases if b != 0]
        self.max_value = Decimal(1)
        for base in self.number_bases:
            self.max_value *= base
        logging.debug(f"Initialized with range_min={self.range_min}, range_max={self.range_max}, max_value={self.max_value}")

    def decimal_to_bit(self, decimal_value):
        decimal_value = Decimal(decimal_value)
        normalized_value = (decimal_value - self.range_min) / (self.range_max - self.range_min)
        scaled_value = normalized_value * self.max_value
        return self._convert_to_layers(scaled_value)

    def bit_to_decimal(self, bit_coordinates):
        scaled_value = self._convert_from_layers(bit_coordinates)
        normalized_value = scaled_value / self.max_value
        decimal_value = normalized_value * (self.range_max - self.range_min) + self.range_min
        return float(decimal_value)

    def _convert_to_layers(self, value):
        coordinates = []
        remaining_value = value
        for base in self.number_bases:
            coordinates.append((remaining_value % base).quantize(Decimal('1.')))
            remaining_value = (remaining_value // base).quantize(Decimal('1.'))
        return coordinates

    def _convert_from_layers(self, coordinates):
        value = Decimal(0)
        multiplier = Decimal(1)
        for coord, base in zip(coordinates, self.number_bases):
            value += coord * multiplier
            multiplier *= base
        return value

class IntegratedBitDescription(EnhancedBitDescription):
    def __init__(self, range_min, range_max, number_bases, quantum_states):
        super().__init__(range_min, range_max, number_bases)
        self.quantum_states = quantum_states

    def encode_with_quantum(self, decimal_value):
        bit_coordinates = self.decimal_to_bit(decimal_value)
        layer_quantum_states = self.quantum_states[0]  # Adjust as needed
        quantum_encoded_bit = encode_quantum_bit(layer_quantum_states)
        return bit_coordinates, quantum_encoded_bit

    def decode_with_quantum(self, bit_coordinates, quantum_encoded_bit):
        decimal_value = self.bit_to_decimal(bit_coordinates)
        quantum_states = decode_quantum_bit(quantum_encoded_bit)
        return decimal_value, quantum_states

    def describe_layers(self):
        descriptions = []
        ranges = [
            (-1, 0, 1), (-np.pi, 0, np.pi), (-5, 0, 5), (-10, 0, 10),
            (-13, 0, 13), (-60, 0, 60), (-360, 0, 360)
        ]
        for i, base in enumerate(self.number_bases):
            descriptions.append({
                'layer': i,
                'range': ranges[i] if i < len(ranges) else (-base, 0, base),
                'quantum_description': self.quantum_states.get(i, {})
            })
        return descriptions

def encode_quantum_bit(quantum_states):
    required_keys = ['n', 'l', 'm_l', 'm_s']
    for key in required_keys:
        if key not in quantum_states:
            raise KeyError(f"Quantum state is missing the key: {key}")
    m_s = int(quantum_states['m_s'] * 2)  # Convert 1/2 to 1
    encoded_value = (quantum_states['n'] << 3) | (quantum_states['l'] << 2) | (quantum_states['m_l'] << 1) | m_s
    return encoded_value

def decode_quantum_bit(encoded_value):
    quantum_states = {
        'n': (encoded_value >> 3) & 0b111,
        'l': (encoded_value >> 2) & 0b1,
        'm_l': (encoded_value >> 1) & 0b1,
        'm_s': (encoded_value & 0b1) / 2  # Convert back to 1/2
    }
    return quantum_states

def save_best_bit_description(best_bit_desc, metrics, file_prefix='best_bit_desc'):
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    best_bit_desc_data = {
        'range_min': str(best_bit_desc.range_min),
        'range_max': str(best_bit_desc.range_max),
        'number_bases': [str(base) for base in best_bit_desc.number_bases],
        'metrics': metrics
    }
    os.makedirs('analysis/UQEBM', exist_ok=True)
    with open(f'analysis/UQEBM/{file_prefix}_{current_time}.json', 'w') as file:
        json.dump(best_bit_desc_data, file, indent=4)
    print(f"Best bit description saved to analysis/UQEBM/{file_prefix}_{current_time}.json")

def load_previous_best(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        return None

def main():
    default_bases = [1, np.pi, 5, 10, 13, 60, 360]

    previous_best_file = 'path_to_previous_best_file.json'
    previous_best = load_previous_best(previous_best_file)
    
    if previous_best:
        bases = [Decimal(base) for base in previous_best['number_bases']]
    else:
        bases = default_bases

    integrated_bit_desc = IntegratedBitDescription(range_min=0, range_max=100, number_bases=bases, quantum_states=quantum_states)
    decimal_value = 1234567890
    bit_coords, quantum_bit = integrated_bit_desc.encode_with_quantum(decimal_value)
    reconstructed_decimal, reconstructed_quantum_states = integrated_bit_desc.decode_with_quantum(bit_coords, quantum_bit)

    print("Original decimal value:", decimal_value)
    print("Bit coordinates:", bit_coords)
    print("Quantum encoded bit:", quantum_bit)
    print("Reconstructed decimal value:", reconstructed_decimal)
    print("Reconstructed quantum states:", reconstructed_quantum_states)

    layer_descriptions = integrated_bit_desc.describe_layers()
    for description in layer_descriptions:
        print(f"Layer {description['layer']} range: {description['range']} quantum description: {description['quantum_description']}")

    y_true = [0, 1, 0, 1, 1, 0]
    y_pred = [0, 0, 1, 1, 0, 1]
    y_proba = [[0.8, 0.2], [0.3, 0.7], [0.6, 0.4], [0.4, 0.6], [0.9, 0.1], [0.2, 0.8]]
    epoch_times = [0.1, 0.2, 0.15, 0.12, 0.18, 0.22]

    metrics = compute_metrics(y_true, y_pred, y_proba, epoch_times)
    save_metrics_to_json(metrics)

    metrics_summary = {"accuracy": metrics['accuracy'], "precision": metrics['precision']}
    save_best_bit_description(integrated_bit_desc, metrics_summary)

    print("\n--- Detailed Metrics Report ---")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\n--- Bit Description ---")
    print(f"Range Min: {integrated_bit_desc.range_min}")
    print(f"Range Max: {integrated_bit_desc.range_max}")
    print(f"Number Bases: {integrated_bit_desc.number_bases}")

if __name__ == "__main__":
    main()
