import math

def represent_bit_with_pi(bit_state):
    certainty = bit_state
    value = bit_state * math.pi
    return (certainty, value)

# Example Usage
bit_states = [-1, 0, 1]
for bit_state in bit_states:
    certainty, value = represent_bit_with_pi(bit_state)
    print(f"Bit State: {bit_state}, Certainty: {certainty}, Value: {value}")
