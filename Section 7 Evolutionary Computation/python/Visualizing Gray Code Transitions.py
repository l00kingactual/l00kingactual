import matplotlib.pyplot as plt
import numpy as np
import logging
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.gridspec import GridSpec

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def binary_to_gray(binary):
    """Converts a binary number (as a string) to its Gray code equivalent (as a string)."""
    try:
        gray = binary[0]  # The first bit is the same
        for i in range(1, len(binary)):
            # XOR the current bit with the previous bit
            gray += str(int(binary[i-1]) ^ int(binary[i]))
        return gray
    except Exception as e:
        logger.error(f"Error in binary_to_gray: {e}")
        raise

def generate_binary_sequences(n):
    """Generates a list of binary sequences of length n."""
    try:
        return [format(i, f'0{n}b') for i in range(2**n)]
    except Exception as e:
        logger.error(f"Error in generate_binary_sequences: {e}")
        raise

def plot_gray_conversion(ax, binary_sequences, gray_codes, bit_length):
    """Plots binary and Gray code sequences for a given bit length."""
    try:
        x = list(range(len(binary_sequences)))
        
        ax.plot(x, [int(b, 2) for b in binary_sequences], 'b-', label='Binary')
        ax.plot(x, [int(g, 2) for g in gray_codes], 'r-', label='Gray Code')
        ax.set_title(f'{bit_length}-Bit Conversion', fontsize=10)
        ax.set_xlabel('Index', fontsize=8)
        ax.set_ylabel('Value', fontsize=8)
        ax.legend(fontsize=8)
    except Exception as e:
        logger.error(f"Error in plot_gray_conversion: {e}")
        raise

def plot_lumpy_cube(ax, n):
    """Plots a 3D lumpy cube for a given bit length."""
    try:
        binary_sequences = generate_binary_sequences(n)
        gray_codes = [binary_to_gray(binary) for binary in binary_sequences]
        
        x = np.arange(len(binary_sequences))
        y = np.array([int(b, 2) for b in binary_sequences])
        z = np.array([int(g, 2) for g in gray_codes])

        ax.plot(x, y, z, 'o-', label='Gray Code', color='purple')
        ax.set_title(f'{n}-Bit Lumpy Cube', fontsize=10)
        ax.set_xlabel('Index', fontsize=8)
        ax.set_ylabel('Binary Value', fontsize=8)
        ax.set_zlabel('Gray Code Value', fontsize=8)
        ax.legend(fontsize=8)
    except Exception as e:
        logger.error(f"Error in plot_lumpy_cube: {e}")
        raise

def visualize_higher_order_bits(bit_lengths):
    """Generates and visualizes binary and Gray code sequences for multiple bit lengths."""
    try:
        # Plotting the 2D conversion plots
        num_plots = len(bit_lengths)
        fig = plt.figure(figsize=(12, 10))
        fig.suptitle('Binary to Gray Code Conversions', fontsize=16)
        gs = GridSpec(3, 2, figure=fig)

        for i, bit_length in enumerate(bit_lengths):
            row, col = divmod(i, 2)
            ax = fig.add_subplot(gs[row, col])
            logger.info(f"Generating sequences for {bit_length}-bit length.")
            binary_sequences = generate_binary_sequences(bit_length)
            gray_codes = [binary_to_gray(binary) for binary in binary_sequences]
            logger.info(f"Binary Sequences ({bit_length} bits): {binary_sequences[:5]}...")  # Display only first 5 for brevity
            logger.info(f"Gray Codes ({bit_length} bits): {gray_codes[:5]}...")  # Display only first 5 for brevity
            plot_gray_conversion(ax, binary_sequences, gray_codes, bit_length)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

        # Plotting the 3D lumpy cubes
        fig_3d = plt.figure(figsize=(12, 10))
        fig_3d.suptitle('3D Visualization of Gray Code Sequences', fontsize=16)
        gs_3d = GridSpec(3, 2, figure=fig_3d)

        for i, bit_length in enumerate(bit_lengths):
            row, col = divmod(i, 2)
            ax = fig_3d.add_subplot(gs_3d[row, col], projection='3d')
            plot_lumpy_cube(ax, bit_length)

        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    except Exception as e:
        logger.error(f"Error in visualize_higher_order_bits: {e}")
        raise

if __name__ == "__main__":
    try:
        bit_lengths = [2, 3, 5, 7, 11, 13]  # You can add more bit lengths (e.g., 32, 64, 128, 256, 512)
        visualize_higher_order_bits(bit_lengths)
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        raise
