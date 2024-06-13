import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import matplotlib.animation as animation

# Number of channels for the equalizer
num_channels = 31
sampling_rate = 44100  # Sampling rate of the audio device
block_size = 1024  # Block size for FFT

# Function to update the bar heights based on audio input
def update_bars(frame, bars):
    audio_block = sd.rec(block_size, samplerate=sampling_rate, channels=1, dtype='float32')
    sd.wait()

    # Apply FFT and calculate the magnitude
    fft_result = np.fft.rfft(audio_block[:, 0])
    fft_magnitude = np.abs(fft_result)
    fft_magnitude = fft_magnitude[:num_channels]

    # Scale the FFT magnitudes to fit within the range 0-20
    fft_magnitude = np.interp(fft_magnitude, (fft_magnitude.min(), fft_magnitude.max()), (0, 100))

    # Update bar heights
    for bar, new_height in zip(bars, fft_magnitude):
        bar.set_height(new_height)
    return bars

# Function to visualize the graphic equalizer
def visualize_equalizer(num_channels):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Initialize bar positions and heights
    x = np.arange(num_channels)
    heights = np.zeros(num_channels)

    # Create bars with different colors for different bands
    colors = plt.cm.viridis(np.linspace(0, 1, num_channels))
    bars = ax.bar(x, heights, color=colors)

    # Set the limits for the x and y axes
    ax.set_xlim(-0.5, num_channels - 0.5)
    ax.set_ylim(0, 100)
    ax.set_xlabel('Channel')
    ax.set_ylabel('Level')
    ax.set_title('Graphic Equalizer Visualization')

    # Add grid lines at intervals of 2.5
    ax.set_yticks(np.arange(0, 100, 2.5))
    ax.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

    # Create the animation
    ani = animation.FuncAnimation(fig, update_bars, fargs=(bars,), interval=100, blit=False)

    plt.show()

# Visualize the graphic equalizer with the specified number of channels
visualize_equalizer(num_channels)