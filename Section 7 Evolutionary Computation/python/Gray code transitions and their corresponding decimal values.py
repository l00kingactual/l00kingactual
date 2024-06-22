import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import plot

# Function to generate Gray code
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

# Function to convert Gray code to binary
def gray_code_to_binary(gray):
    binary = gray[0]
    for i in range(1, len(gray)):
        if gray[i] == '0':
            binary += binary[i-1]
        else:
            binary += str(1 - int(binary[i-1]))
    return binary

# Function to convert binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# Function to convert Gray code to decimal
def gray_code_to_decimal(gray):
    binary = gray_code_to_binary(gray)
    return binary_to_decimal(binary)

# Function to simulate transitions and create the plot
def simulate_transitions(n):
    gray_code_sequence = generate_gray_code(n)
    decimal_sequence = [gray_code_to_decimal(code) for code in gray_code_sequence]

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=('Gray Code Sequence', 'Decimal Sequence'))

    fig.add_trace(go.Scatter(x=list(range(len(gray_code_sequence))), y=gray_code_sequence, mode='lines+markers', name='Gray Code Sequence', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=list(range(len(decimal_sequence))), y=decimal_sequence, mode='lines+markers', name='Decimal Sequence', line=dict(color='red')), row=2, col=1)

    fig.update_layout(height=600, width=800, title_text="Gray Code and Corresponding Decimal Sequence", showlegend=False)
    fig.update_xaxes(title_text='Index')
    fig.update_yaxes(title_text='Gray Code', row=1, col=1)
    fig.update_yaxes(title_text='Decimal Value', row=2, col=1)

    return fig

# Example usage:
fig = simulate_transitions(3)
plot(fig, filename='gray_code_transitions.html')
