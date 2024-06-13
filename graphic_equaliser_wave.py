import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import matplotlib.animation as animation

# Number of channels for the equalizer
num_channels = 31
sampling_rate = 44100  # Sampling rate of the audio device
block_size = 1024  # Block size for FFT

# Function to update the area plot based on audio input
def update_area(frame, ax, x):
    audio_block = sd.rec(block_size, samplerate=sampling_rate, channels=1, dtype='float32')
    sd.wait()

    # Apply FFT and calculate the magnitude
    fft_result = np.fft.rfft(audio_block[:, 0])
    fft_magnitude = np.abs(fft_result)
    fft_magnitude = fft_magnitude[:num_channels]

    # Scale the FFT magnitudes to fit within the range 0-20
    fft_magnitude = np.interp(fft_magnitude, (fft_magnitude.min(), fft_magnitude.max()), (0, 20))

    # Clear the previous area plot and draw the new one
    ax.collections.clear()
    ax.fill_between(x, 0, fft_magnitude, color=plt.cm.viridis(np.linspace(0, 1, num_channels)), alpha=0.7)

    return ax

# Function to visualize the graphic equalizer as a moving area plot
def visualize_equalizer_area(num_channels):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Initialize positions
    x = np.arange(num_channels)

    # Set the limits for the x and y axes
    ax.set_xlim(-0.5, num_channels - 0.5)
    ax.set_ylim(0, 20)
    ax.set_xlabel('Channel')
    ax.set_ylabel('Level')
    ax.set_title('Graphic Equalizer Visualization (Area)')

    # Add grid lines at intervals of 2.5
    ax.set_yticks(np.arange(0, 21, 2.5))
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

    # Create the animation
    ani = animation.FuncAnimation(fig, update_area, fargs=(ax, x), interval=50, blit=False)

    plt.show()

# Visualize the graphic equalizer area with the specified number of channels
visualize_equalizer_area(num_channels)
