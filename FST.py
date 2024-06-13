import numpy as np
from scipy.fft import fft

# Sample data
signal = np.array([0.0, 1.0, 0.0, 1.0])

# Perform FFT (Cooley-Tukey Radix-2)
fft_result = fft(signal)

print("FFT Result (Cooley-Tukey Radix-2):")
print(fft_result)


import numpy as np
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import skcuda.fft as cu_fft

# Sample data
signal = np.array([0.0, 1.0, 0.0, 1.0])

# Transfer data to GPU
gpu_signal = gpuarray.to_gpu(signal.astype(np.complex64))

# Perform GPU-based FFT
cu_fft.fft(gpu_signal, gpu_signal)

# Transfer data back to CPU (if needed)
fft_result = gpu_signal.get()

print("GPU-based FFT Result:")
print(fft_result)
