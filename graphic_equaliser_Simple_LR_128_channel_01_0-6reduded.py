import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import matplotlib.animation as animation

# Number of channels for the equalizer
num_channels = 128
sampling_rate = 44100  # Sampling rate of the audio device
block_size = 1024  # Block size for FFT

# Function to update the bar heights based on audio input
def update_bars(frame, bars_left, bars_right):
    audio_block = sd.rec(block_size, samplerate=sampling_rate, channels=2, dtype='float32')
    sd.wait()

    # Apply FFT and calculate the magnitude for both channels
    fft_result_left = np.fft.rfft(audio_block[:, 0])
    fft_result_right = np.fft.rfft(audio_block[:, 1])
    fft_magnitude_left = np.abs(fft_result_left)
    fft_magnitude_right = np.abs(fft_result_right)
    fft_magnitude_left = fft_magnitude_left[:num_channels]
    fft_magnitude_right = fft_magnitude_right[:num_channels]

    # Apply 20% reduction to the first 6 channels
    fft_magnitude_left[:6] *= 0.8
    fft_magnitude_right[:6] *= 0.8

    # Scale the FFT magnitudes to fit within the range 0-100
    fft_magnitude_left = np.interp(fft_magnitude_left, (fft_magnitude_left.min(), fft_magnitude_left.max()), (0, 100))
    fft_magnitude_right = np.interp(fft_magnitude_right, (fft_magnitude_right.min(), fft_magnitude_right.max()), (0, 100))

    # Update bar heights
    for bar, new_height in zip(bars_left, fft_magnitude_left):
        bar.set_height(new_height)
    for bar, new_height in zip(bars_right, fft_magnitude_right):
        bar.set_height(new_height)
    return bars_left + bars_right

# Function to visualize the graphic equalizer
def visualize_equalizer(num_channels):
    fig, (ax_left, ax_right) = plt.subplots(1, 2, figsize=(20, 8))

    # Initialize bar positions and heights
    x = np.arange(num_channels)
    heights = np.zeros(num_channels)

    # Create bars with different colors for different bands
    colors_left = plt.cm.viridis(np.linspace(0, 1, num_channels))
    bars_left = ax_left.bar(x, heights, color=colors_left)
    colors_right = plt.cm.viridis(np.linspace(0, 1, num_channels))
    bars_right = ax_right.bar(x, heights, color=colors_right)

    # Set the limits for the x and y axes
    ax_left.set_xlim(-0.5, num_channels - 0.5)
    ax_left.set_ylim(0, 100)
    ax_left.set_xticks(np.arange(0, num_channels, 2))
    ax_left.set_xlabel('Channel')
    ax_left.set_ylabel('Level')
    ax_left.set_title('Left Channel')
    ax_right.set_xlim(-0.5, num_channels - 0.5)
    ax_right.set_ylim(0, 100)
    ax_right.set_xticks(np.arange(0, num_channels, 2))
    ax_right.set_xlabel('Channel')
    ax_right.set_ylabel('Level')
    ax_right.set_title('Right Channel')

    # Add grid lines at intervals of 2.5
    ax_left.set_yticks(np.arange(0, 101, 2.5))
    ax_left.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)
    ax_right.set_yticks(np.arange(0, 101, 2.5))
    ax_right.grid(True, which='both', axis='y', linestyle='--', linewidth=0.5)

    # Create the animation
    ani = animation.FuncAnimation(fig, update_bars, fargs=(bars_left, bars_right), interval=100, blit=False)

    plt.show()

# Visualize the graphic equalizer with the specified number of channels
visualize_equalizer(num_channels)
