import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Number of channels for the equalizer
num_channels = 31
sampling_rate = 44100  # Sampling rate of the audio device
block_size = 1024  # Block size for FFT

# Define some presets
presets = {
    'Flat': np.ones(num_channels),
    'Bass Boost': np.array([2 if i < num_channels // 3 else 1 for i in range(num_channels)]),
    'Treble Boost': np.array([1 if i < num_channels // 3 else 2 for i in range(num_channels)]),
    'V-Shape': np.array([2 if i < num_channels // 3 or i > 2 * num_channels // 3 else 1 for i in range(num_channels)])
}

# Initialize the equalizer gains
gains = np.ones(num_channels)
sliders = []

# Function to update the bar heights based on audio input
def update_bars(frame, bars):
    audio_block = sd.rec(block_size, samplerate=sampling_rate, channels=1, dtype='float32')
    sd.wait()

    # Apply FFT and calculate the magnitude
    fft_result = np.fft.rfft(audio_block[:, 0])
    fft_magnitude = np.abs(fft_result)
    fft_magnitude = fft_magnitude[:num_channels]

    # Apply the equalizer gains
    fft_magnitude *= gains

    # Scale the FFT magnitudes to fit within the range 0-10
    fft_magnitude = np.interp(fft_magnitude, (fft_magnitude.min(), fft_magnitude.max()), (0, 10))

    # Update bar heights
    for bar, new_height in zip(bars, fft_magnitude):
        bar.set_height(new_height)
    return bars

# Function to update the gains from sliders
def update_gains(val):
    global gains
    for i in range(num_channels):
        gains[i] = sliders[i].val

# Function to apply a preset
def apply_preset(label):
    global gains
    gains = presets[label]
    for i in range(num_channels):
        sliders[i].set_val(gains[i])

# Function to visualize the graphic equalizer
def visualize_equalizer(num_channels):
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.subplots_adjust(bottom=0.3)  # Adjust to make space for sliders

    # Initialize bar positions and heights
    x = np.arange(num_channels)
    heights = np.zeros(num_channels)

    # Create bars with different colors for different bands
    colors = plt.cm.viridis(np.linspace(0, 1, num_channels))
    bars = ax.bar(x, heights, color=colors)

    # Set the limits for the x and y axes
    ax.set_xlim(-0.5, num_channels - 0.5)
    ax.set_ylim(0, 10)
    ax.set_xlabel('Channel')
    ax.set_ylabel('Level')
    ax.set_title('Graphic Equalizer Visualization')

    # Create the sliders for each channel
    slider_width = 0.03
    slider_height = 0.2
    slider_spacing = (1 - (slider_width * num_channels)) / (num_channels + 1)
    
    for i in range(num_channels):
        ax_slider = plt.axes([slider_spacing + i * (slider_width + slider_spacing), 0.1, slider_width, slider_height], facecolor='lightgoldenrodyellow')
        slider = Slider(ax_slider, f'CH{i+1}', 0.1, 2.0, valinit=1.0, orientation='vertical')
        slider.on_changed(update_gains)
        sliders.append(slider)

    # Create the preset button
    ax_preset = plt.axes([0.9, 0.025, 0.08, 0.04], facecolor='lightgoldenrodyellow')
    preset_button = Button(ax_preset, 'Preset')
    preset_button.on_clicked(lambda x: apply_preset('V-Shape'))

    # Create the animation
    ani = animation.FuncAnimation(fig, update_bars, fargs=(bars,), interval=50, blit=False, cache_frame_data=False)

    plt.show()

# Visualize the graphic equalizer with the specified number of channels
visualize_equalizer(num_channels)
