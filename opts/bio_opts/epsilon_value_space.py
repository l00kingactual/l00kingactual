import numpy as np

epsilon_value_space = [
    0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001,
    np.pi / 10, np.pi / 100, np.pi / 1000,
    1 / np.e, 1 / (np.e**2), 1 / (np.e**3),
    (np.pi**2) / 10, (np.pi**3) / 100, (np.pi**5) / 1000,
    (np.pi**8) / 10, (np.pi**10) / 100, (np.pi**13) / 1000,
    1 / (np.sqrt(2)), 1 / (np.sqrt(3)), 1 / (np.sqrt(5)),
    299792458 / 10**9, 299792458 / 10**10, 299792458 / 10**11,
    6.67430e-11, 6.67430e-12, 6.67430e-13,  # Gravitational constant scales
    6.62607015e-34, 6.62607015e-35, 6.62607015e-36,  # Planck constant scales
    1.616255e-35, 1.616255e-36, 1.616255e-37  # Planck length scales
]
