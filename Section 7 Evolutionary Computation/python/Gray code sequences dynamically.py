import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def generate_gray_code(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['0', '1']
    else:
        previous_gray_code = generate_gray_code(n - 1)
        result = []
        for code in previous_gray_code:
            result.append('0' + code)
        for code in reversed(previous_gray_code):
            result.append('1' + code)
        return result

def update(frame, gray_code_sequence, text):
    text.set_text(gray_code_sequence[frame])

def animate_gray_code(n):
    gray_code_sequence = generate_gray_code(n)
    fig, ax = plt.subplots()
    text = ax.text(0.5, 0.5, '', ha='center', va='center', fontsize=24, fontfamily='monospace')
    ax.set_axis_off()

    ani = animation.FuncAnimation(fig, update, frames=len(gray_code_sequence), fargs=(gray_code_sequence, text), interval=500, repeat=True)
    plt.show()

# Example usage:
animate_gray_code(3)
