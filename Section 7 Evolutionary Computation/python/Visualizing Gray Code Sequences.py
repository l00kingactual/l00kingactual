import matplotlib.pyplot as plt

def generate_gray_code(n):
    if n == 0:
        return ['0']
    else:
        prev_gray_code = generate_gray_code(n - 1)
        reversed_prev_gray_code = [code[::-1] for code in prev_gray_code]
        gray_code = prev_gray_code + ['1' + code for code in reversed_prev_gray_code]
        return gray_code

def visualize_gray_code_sequence(n):
    gray_code_sequence = generate_gray_code(n)
    fig, ax = plt.subplots()
    ax.axis('off')
    
    for i, code in enumerate(gray_code_sequence):
        ax.text(0.1, 1 - i * 0.1, code, fontsize=12, fontfamily='monospace')

    plt.title(f"{n}-bit Gray Code Sequence")
    plt.show()

# Example usage:
visualize_gray_code_sequence(3)