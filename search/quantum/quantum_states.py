# quantum_states.py

# Define a grid of quantum states within a realm
quantum_states = {
    0: {'n': 2, 'l': 2, 'm_l': 2, 'm_s': -0.25},
    1: {'n': 4, 'l': 2, 'm_l': 2, 'm_s': 0.5},
    2: {'n': 5, 'l': 3, 'm_l': 0, 'm_s': -0.75},
    3: {'n': 6, 'l': 1, 'm_l': -1, 'm_s': 0.35},
    4: {'n': 7, 'l': 2, 'm_l': 3, 'm_s': -0.85},
    5: {'n': 8, 'l': 3, 'm_l': -2, 'm_s': 0.45},
    6: {'n': 9, 'l': 4, 'm_l': 4, 'm_s': -0.95},
    7: {'n': 3, 'l': 1, 'm_l': 1, 'm_s': -0.5},
}

# You could define the 15 realms as a collection of quantum states
realms = []
for i in range(15):
    realm_states = {index: quantum_states[(index + i) % 8] for index in range(8)}
    realms.append(realm_states)

# Export the quantum_states and realms for import in other modules
__all__ = ["quantum_states", "realms"]
