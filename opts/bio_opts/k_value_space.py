import numpy as np

k_value_space = [
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946,
    np.pi, np.e, np.sqrt(2), np.sqrt(3), np.sqrt(5),
    1.6180339887,  # Golden ratio
    299792458 / 10**7, 299792458 / 10**8, 299792458 / 10**9,
    6.67430e-11 * 10**10, 6.67430e-11 * 10**9,  # Adjusted gravitational constant scales
    6.62607015e-34 * 10**34, 6.62607015e-34 * 10**33,  # Adjusted Planck constant scales
    1.616255e-35 * 10**35, 1.616255e-35 * 10**34  # Adjusted Planck length scales
]
