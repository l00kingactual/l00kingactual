fundamental_constants = {
    "Planck_constant_h": 6.62607015e-34,  # Joule seconds (Js)
    "Reduced_Planck_constant_hbar": 1.0545718e-34,  # Joule seconds (Js)
    "Speed_of_light_c": 3.00e8,  # meters per second (m/s)
    "Elementary_charge_e": 1.602176634e-19,  # Coulombs (C)
    "Electron_mass_me": 9.10938356e-31,  # kilograms (kg)
    "Boltzmann_constant_kB": 1.380649e-23,  # Joules per Kelvin (J/K)
    "Avogadro_constant_NA": 6.02214076e23,  # per mole (mol^-1)
    "Gravitational_constant_G": 6.67430e-11,  # m^3 kg^-1 s^-2
    "Fine_structure_constant_alpha": 1/137.035999,  # dimensionless
    "Planck_length": 1.616255e-35,  # meters (m)
    "Planck_time": 5.391247e-44,  # seconds (s)
}


physics_formulas = {
    "Energy_of_photon": "E = h * frequency",  # E is energy, h is Planck constant, frequency is the frequency of the photon
    "Einstein_energy_mass_equivalence": "E = mc^2",  # E is energy, m is mass, c is the speed of light
    "de_Broglie_wavelength": "wavelength = h / (mass * velocity)",  # h is Planck constant, mass is the mass of the particle, velocity is the particle's velocity
    "Coulomb_law": "F = k * (q1 * q2) / r^2",  # F is force, k is Coulomb's constant, q1 and q2 are charges, r is distance between charges
    "Bohr_radius": "a_0 = (4 * pi * epsilon_0 * hbar^2) / (mass_e * e^2)",  # a_0 is Bohr radius, pi is Pi, epsilon_0 is vacuum permittivity, hbar is reduced Planck constant, mass_e is electron mass, e is elementary charge
    "Rydberg_formula": "1/lambda = R * (1/n1^2 - 1/n2^2)",  # lambda is wavelength of light, R is Rydberg constant, n1 and n2 are principal quantum numbers
    "Planck_Energy": "E = hbar * omega",  # E is energy, hbar is reduced Planck constant, omega is angular frequency
}

# Note: This dictionary contains the formulae as strings for educational purposes. For actual computations, 
# you would define functions that implement these equations, substituting in the values of the constants 
# and any variables as required.
