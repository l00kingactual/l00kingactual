import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import plot

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

def gray_code_to_binary(gray):
    binary = gray[0]
    for i in range(1, len(gray)):
        if gray[i] == '0':
            binary += binary[i-1]
        else:
            binary += str(1 - int(binary[i-1]))
    return binary

def binary_to_decimal(binary):
    return int(binary, 2)

def gray_code_to_decimal(gray):
    binary = gray_code_to_binary(gray)
    return binary_to_decimal(binary)

def create_animated_gray_code_plot(n):
    gray_code_sequence = generate_gray_code(n)
    decimal_sequence = [gray_code_to_decimal(code) for code in gray_code_sequence]

    fig = go.Figure()

    # Add traces for initial frame
    fig.add_trace(go.Scatter(x=list(range(len(gray_code_sequence))), y=gray_code_sequence, mode='lines+markers', name='Gray Code Sequence', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=list(range(len(decimal_sequence))), y=decimal_sequence, mode='lines+markers', name='Decimal Sequence', line=dict(color='red')))

    # Create frames
    frames = []
    for i in range(len(gray_code_sequence)):
        frame = go.Frame(data=[
            go.Scatter(x=list(range(i+1)), y=gray_code_sequence[:i+1], mode='lines+markers', line=dict(color='blue')),
            go.Scatter(x=list(range(i+1)), y=decimal_sequence[:i+1], mode='lines+markers', line=dict(color='red'))
        ], name=str(i))
        frames.append(frame)

    fig.frames = frames

    # Add animation settings
    fig.update_layout(updatemenus=[{
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}],
                "label": "Play",
                "method": "animate"
            },
            {
                "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 87},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": 0,
        "yanchor": "top"
    }])

    fig.update_layout(height=600, width=800, title_text="Animated Gray Code Transitions")
    fig.update_xaxes(title_text='Index')
    fig.update_yaxes(title_text='Value')

    return fig

# Example usage:
fig = create_animated_gray_code_plot(3)
plot(fig, filename='animated_gray_code_transitions.html')
