# quantum_bit_utils.py

def encode_quantum_bit(quantum_state):
    n = quantum_state.get('n', 1)
    l = quantum_state.get('l', 0)
    m_l = quantum_state.get('m_l', 0)
    m_s = int(quantum_state.get('m_s', 0) * 2)  # Convert -0.5 or 0.5 to -1 or 1

    # Janus: Include a 'handedness' bit to represent forward or backward (past/future)
    handedness = quantum_state.get('handedness', 0)  # 0 for forward, 1 for backward

    encoded_value = (handedness << 4) | (n << 3) | (l << 2) | (m_l << 1) | (m_s & 0b1)
    return encoded_value

def decode_quantum_bit(encoded_value):
    handedness = (encoded_value >> 4) & 0b1
    quantum_state = {
        'n': (encoded_value >> 3) & 0b111,
        'l': (encoded_value >> 2) & 0b1,
        'm_l': (encoded_value >> 1) & 0b1,
        'm_s': ((encoded_value & 0b1) * 2 - 1) / 2,  # Convert back to -0.5 or 0.5
        'handedness': handedness  # 0 for forward, 1 for backward
    }
    return quantum_state
