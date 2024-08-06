class QuantumState:
    def __init__(self, n, l, m_l, m_s, E_P, G_P, t_P, XYZ, pi_P):
        self.n = n
        self.l = l
        self.m_l = m_l
        self.m_s = m_s
        self.E_P = E_P  # Energy in Planck units
        self.G_P = G_P  # Gravity at Planck scale
        self.t_P = t_P  # Time in Planck units
        self.XYZ = XYZ  # Spatial dimensions in Planck lengths
        self.pi_P = pi_P  # Pi at Planck scale
    
    def display(self):
        print(f"Quantum State: n={self.n}, l={self.l}, m_l={self.m_l}, m_s={self.m_s}")
        print(f"Planck Scale Properties: E_P={self.E_P}, G_P={self.G_P}, t_P={self.t_P}, XYZ={self.XYZ}, pi_P={self.pi_P}")

# Example instantiation
quantum_state_example = QuantumState(1, 0, 0, 0.5, 1.956e9, 1, 5.391e-44, (1.616e-35, 1.616e-35, 1.616e-35), 3.14159)
quantum_state_example.display()
