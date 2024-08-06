import numpy as np

k_value_space = [
    0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001,
    np.pi / 10, np.pi / 100, np.pi / 1000,
    (np.pi**2) / 10, (np.pi**2) / 100, (np.pi**2) / 1000,
    (np.pi**3) / 10, (np.pi**3) / 100, (np.pi**3) / 1000,
    (np.pi**5) / 10, (np.pi**5) / 100, (np.pi**5) / 1000,
    (np.pi**8) / 10, (np.pi**8) / 100, (np.pi**8) / 1000,
    (np.pi**10) / 10, (np.pi**10) / 100, (np.pi**10) / 1000,
    (np.pi**13) / 10, (np.pi**13) / 100, (np.pi**13) / 1000,
    (np.pi**15) / 10, (np.pi**15) / 100, (np.pi**15) / 1000,
    (np.pi**16) / 10, (np.pi**16) / 100, (np.pi**16) / 1000,
    (np.pi**32) / 10, (np.pi**32) / 100, (np.pi**32) / 1000,
    (np.pi**64) / 10, (np.pi**64) / 100, (np.pi**64) / 1000,
    (np.pi**128) / 10, (np.pi**128) / 100, (np.pi**128) / 1000,
    299792458 / 10**9, 299792458 / 10**10, 299792458 / 10**11
]