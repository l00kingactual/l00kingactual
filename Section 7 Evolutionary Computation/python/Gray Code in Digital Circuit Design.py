import numpy as np
import matplotlib.pyplot as plt

def generate_gray_code(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['0', '1']
    else:
        previous_gray_code = generate_gray_code(n - 1)
        result = []
        # Prefix '0' to the first half
        for code in previous_gray_code:
            result.append('0' + code)
        # Prefix '1' to the second half (reflected)
        for code in reversed(previous_gray_code):
            result.append('1' + code)
        return result

def simulate_transitions(n):
    binary_sequence = [format(i, f'0{n}b') for i in range(2**n)]
    gray_code_sequence = generate_gray_code(n)

    fig, ax = plt.subplots(2, 1, figsize=(10, 5), sharex=True)
    ax[0].set_title('Binary Transitions')
    ax[1].set_title('Gray Code Transitions')
    
    for i in range(len(binary_sequence) - 1):
        binary_transition = np.sum([a != b for a, b in zip(binary_sequence[i], binary_sequence[i+1])])
        gray_transition = np.sum([a != b for a, b in zip(gray_code_sequence[i], gray_code_sequence[i+1])])

        ax[0].plot([i, i + 1], [binary_transition, binary_transition], 'b')
        ax[1].plot([i, i + 1], [gray_transition, gray_transition], 'r')

    ax[0].set_yticks([0, 1, 2, 3, 4])
    ax[1].set_yticks([0, 1])
    ax[1].set_xticks(range(len(binary_sequence)))
    ax[1].set_xticklabels(binary_sequence, rotation=90, fontfamily='monospace')

    plt.show()

# Example usage:
simulate_transitions(3)
