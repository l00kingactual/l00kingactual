import numpy as np
import scipy.io.wavfile as wav
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def apply_low_pass_filter(input_wav_path, output_wav_path, cutoff_freq):
    """
    Applies a low-pass filter to an audio file.
    
    Parameters:
    input_wav_path (str): Path to the input .wav file.
    output_wav_path (str): Path to save the output .wav file.
    cutoff_freq (float): Cutoff frequency for the low-pass filter.
    """
    try:
        # Read the input audio file
        logging.info(f"Reading input audio file: {input_wav_path}")
        sample_rate, data = wav.read(input_wav_path)
        logging.debug(f"Sample rate: {sample_rate}, Data shape: {data.shape}")

        # Apply low-pass filter
        logging.info("Applying low-pass filter")
        fft_data = np.fft.rfft(data)
        frequencies = np.fft.rfftfreq(len(data), d=1/sample_rate)
        logging.debug(f"Frequencies array shape: {frequencies.shape}")

        # Zero out frequencies above the cutoff
        fft_data[frequencies > cutoff_freq] = 0
        filtered_data = np.fft.irfft(fft_data)

        # Save the filtered audio to a new file
        logging.info(f"Saving filtered audio to: {output_wav_path}")
        wav.write(output_wav_path, sample_rate, filtered_data.astype(np.int16))
        logging.info("Low-pass filtering completed successfully")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except ValueError as e:
        logging.error(f"Value error: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
input_wav_path = 'path_to_input_audio.wav'
output_wav_path = 'path_to_output_audio.wav'
cutoff_freq = 5000.0  # Cutoff frequency in Hz

apply_low_pass_filter(input_wav_path, output_wav_path, cutoff_freq)
