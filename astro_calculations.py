import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.fftpack import fft
from scipy.constants import gravitational_constant as G

# 1. Kepler's Laws
def keplers_third_law(semi_major_axis):
    """ Calculate orbital period using Kepler's Third Law. """
    # Assuming Sun's mass as the central mass (solar mass in kg)
    solar_mass = 1.989e30  
    period_squared = (4 * np.pi**2 * semi_major_axis**3) / (G * solar_mass)
    return np.sqrt(period_squared) / (60 * 60 * 24)  # Return period in days

# 2. Light Curve Analysis
def model_light_curve(time, max_brightness, drop, width, center_time):
    """ Simple model for a transit light curve (box model) """
    return max_brightness - drop * ((np.abs(time - center_time) < width))

def analyze_light_curve(time, brightness):
    """ Fit a model to light curve data to extract parameters. """
    params, cov = curve_fit(model_light_curve, time, brightness, p0=[1, 0.1, 0.1, 0])
    return params

# 3. Doppler Effect for Radial Velocity
def calculate_radial_velocity(wavelength_observed, wavelength_emitted):
    """ Calculate radial velocity from redshift/blueshift """
    return ((wavelength_observed - wavelength_emitted) / wavelength_emitted) * 299792.458  # Speed of light in km/s

# 4. Orbital Mechanics using Newton's Laws
def gravitational_force(m1, m2, distance):
    """ Calculate gravitational force between two masses """
    return G * m1 * m2 / distance**2

# 5. Fourier Analysis for Light Curves
def perform_fourier_analysis(data):
    """ Perform Fourier analysis on light curve data """
    N = len(data)
    T = 1.0  # Assuming sampling period is 1 day
    x = np.linspace(0.0, N*T, N, endpoint=False)
    yf = fft(data)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.grid()
    plt.show()

# Example Usage
semi_major_axis = 1.496e11  # 1 AU in meters
period = keplers_third_law(semi_major_axis)
print(f"Orbital Period of Earth: {period} days")

# Simulated light curve data (example)
time = np.linspace(-1, 1, 100)
brightness = model_light_curve(time, 1.0, 0.1, 0.1, 0)
observed_params = analyze_light_curve(time, brightness)
print(f"Observed Parameters: {observed_params}")

# Doppler effect example
v_radial = calculate_radial_velocity(656.3, 656.28)  # Example wavelengths in nm
print(f"Radial Velocity: {v_radial} km/s")

# Gravitational force example
force = gravitational_force(5.972e24, 1.989e30, semi_major_axis)  # Earth and Sun
print(f"Gravitational Force between Earth and Sun: {force} N")

# Perform Fourier analysis on a simple sine wave
perform_fourier_analysis(np.sin(2.0*np.pi*time))
