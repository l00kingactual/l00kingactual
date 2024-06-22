import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

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

def interactive_gray_code(n):
    binary_sequence = [format(i, f'0{n}b') for i in range(2**n)]
    gray_code_sequence = generate_gray_code(n)

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=('Binary Transitions', 'Gray Code Transitions'))

    binary_transitions = [np.sum([a != b for a, b in zip(binary_sequence[i], binary_sequence[i+1])]) for i in range(len(binary_sequence) - 1)]
    gray_transitions = [np.sum([a != b for a, b in zip(gray_code_sequence[i], gray_code_sequence[i+1])]) for i in range(len(gray_code_sequence) - 1)]

    fig.add_trace(go.Scatter(x=list(range(len(binary_transitions))), y=binary_transitions, mode='lines+markers', name='Binary Transitions'), row=1, col=1)
    fig.add_trace(go.Scatter(x=list(range(len(gray_transitions))), y=gray_transitions, mode='lines+markers', name='Gray Code Transitions'), row=2, col=1)

    fig.update_layout(height=600, width=800, title_text="Transitions in Binary and Gray Code Sequences", showlegend=False)
    fig.update_xaxes(title_text='Transition Index')
    fig.update_yaxes(title_text='Number of Bit Changes', row=1, col=1)
    fig.update_yaxes(title_text='Number of Bit Changes', row=2, col=1)

    fig.show()

# Example usage:
interactive_gray_code(3)
