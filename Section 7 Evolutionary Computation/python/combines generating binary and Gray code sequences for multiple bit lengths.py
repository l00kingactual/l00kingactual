import matplotlib.pyplot as plt
import numpy as np
import logging

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
        ax.set_title(f'{bit_length}-Bit Conversion')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        ax.legend()
    except Exception as e:
        logger.error(f"Error in plot_gray_conversion: {e}")
        raise

def visualize_higher_order_bits(bit_lengths):
    """Generates and visualizes binary and Gray code sequences for multiple bit lengths."""
    try:
        fig, axs = plt.subplots(len(bit_lengths), 1, figsize=(10, len(bit_lengths) * 5))
        if len(bit_lengths) == 1:
            axs = [axs]
        
        for ax, bit_length in zip(axs, bit_lengths):
            logger.info(f"Generating sequences for {bit_length}-bit length.")
            binary_sequences = generate_binary_sequences(bit_length)
            gray_codes = [binary_to_gray(binary) for binary in binary_sequences]
            logger.info(f"Binary Sequences ({bit_length} bits): {binary_sequences[:5]}...")  # Display only first 5 for brevity
            logger.info(f"Gray Codes ({bit_length} bits): {gray_codes[:5]}...")  # Display only first 5 for brevity
            plot_gray_conversion(ax, binary_sequences, gray_codes, bit_length)
        
        plt.tight_layout()
        plt.show()
    except Exception as e:
        logger.error(f"Error in visualize_higher_order_bits: {e}")
        raise

if __name__ == "__main__":
    try:
        bit_lengths = [3, 4, 5, 6, 7]  # You can add more bit lengths (e.g., 32, 64, 128, 256, 512)
        visualize_higher_order_bits(bit_lengths)
    except Exception as e:
        logger.error(f"Unhandled error: {e}")
        raise
