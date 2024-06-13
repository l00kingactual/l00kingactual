def encode(n, l, m_l, m_s):
    """
    Hypothetical function to encode quantum numbers into a format compatible with TetraLogix.
    
    Parameters:
    - n: Principal quantum number
    - l: Azimuthal quantum number
    - m_l: Magnetic quantum number
    - m_s: Spin quantum number
    
    Returns:
    A representation of the quantum state (for simplicity, encoded as a dictionary here).
    """
    quantum_state = {
        'n': n,
        'l': l,
        'm_l': m_l,
        'm_s': m_s
    }
    return quantum_state

# Example usage of the encode function
encoded_quantum_state = encode(1, 0, 0, 0.5)
print(encoded_quantum_state)
