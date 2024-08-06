import numpy as np
import datetime
import pandas as pd
import json
import os
import matplotlib.pyplot as plt
from compute_metrics import compute_metrics, save_metrics_to_json
from epsilon_greedy import epsilon_greedy
from k_value_space import k_value_space
from q_value_space import q_value_space
from epsilon_value_space import epsilon_value_space

# Initialize Q-table with given actions and states
def init_q_table(actions, states):
    print("Initializing Q-table for reinforcement learning...")
    if not actions or not states:
        print("Error: Actions and states must be non-empty lists.")
        return None
    q_table = pd.DataFrame(columns=actions, index=states, data=0.0)
    print(f"Q-table successfully initialized with {len(states)} states and {len(actions)} actions.")
    print("Snippet of the initialized Q-table:")
    print(q_table.head())
    return q_table

# Q-learning update
def q_learning(q_table, state, action, reward, next_state, lr=0.1, gamma=0.9):
    print(f"Performing Q-learning update for state-action pair ({state}, {action})...")
    if state not in q_table.index or action not in q_table.columns:
        print(f"Error: State {state} or action {action} not found in Q-table.")
        return q_table
    current_q_value = q_table.loc[state, action]
    if next_state not in q_table.index:
        print(f"Error: Next state {next_state} not found in Q-table.")
        return q_table
    max_next_q_value = q_table.loc[next_state].max()
    target_q_value = reward + gamma * max_next_q_value
    q_table.loc[state, action] += lr * (target_q_value - current_q_value)
    print(f"Q-value updated from {current_q_value} to {q_table.loc[state, action]}")
    return q_table

# Function to load and clean JSON data from the analysis directory
def load_and_clean_data(analysis_dir='analysis/'):
    data = []
    for root, _, files in os.walk(analysis_dir):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    try:
                        file_data = json.load(f)
                        if isinstance(file_data, list):
                            data.extend(file_data)
                        else:
                            data.append(file_data)
                    except json.JSONDecodeError as e:
                        print(f"Error reading {file_path}: {e}")
    return data

# Function to compile data into a DataFrame
def compile_data_to_df(data):
    compiled_data = []
    for entry in data:
        if isinstance(entry, dict):
            for step in entry.get('steps', []):
                compiled_data.append({
                    'episode': entry['episode'],
                    'state': step.get('state', None),
                    'action': step.get('action', None),
                    'reward': step.get('reward', None),
                    'next_state': step.get('next_state', None),
                    'q_value': step.get('q_value', None)
                })
    df = pd.DataFrame(compiled_data)
    return df

# Function to convert numpy data types to native Python types
def convert_to_native(data):
    if isinstance(data, np.generic):
        return data.item()
    return data

# Function to create directories if they do not exist
def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Example setup and execution
if __name__ == "__main__":
    actions = ['action1', 'action2', 'action3', 'action4']
    states = ['state1', 'state2', 'state3', 'state4', 'state5']

    q_table = init_q_table(actions, states)

    # Import values from value space files
    epsilon_values = epsilon_value_space  # Correct usage as a list
    k_values = k_value_space  # Correct usage as a list
    q_values = q_value_space  # Correct usage as a list

    lr = 0.1
    gamma = 0.9
    num_episodes = 10

    all_metrics = []

    for episode in range(num_episodes):
        print(f"\nEpisode {episode + 1}/{num_episodes}")
        state = np.random.choice(states)
        print(f"Starting in state {state}")

        episode_metrics = {
            'episode': convert_to_native(episode + 1),
            'steps': []
        }

        for step in range(5):  # Arbitrary number of steps per episode
            epsilon = float(np.random.choice(epsilon_values))  # Ensure epsilon is a float
            action = epsilon_greedy(q_table, state, epsilon)
            reward = np.random.rand()  # Simulated reward
            next_state = np.random.choice(states)
            print(f"Action {action} taken, received reward {reward}, transitioning to next state {next_state}")
            q_table = q_learning(q_table, state, action, reward, next_state, lr, gamma)

            step_metrics = {
                'state': state,
                'action': action,
                'reward': convert_to_native(reward),
                'next_state': next_state,
                'q_value': convert_to_native(q_table.loc[state, action]) if state in q_table.index and action in q_table.columns else None
            }

            episode_metrics['steps'].append(step_metrics)
            state = next_state

        all_metrics.append(episode_metrics)

    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    metrics_filename = f'analysis/q_learning/q-learning_metrics_{current_time}.json'
    ensure_dir_exists(os.path.dirname(metrics_filename))

    with open(metrics_filename, 'w') as file:
        json.dump(all_metrics, file, indent=4, default=convert_to_native)

    print("\nFinal Q-table:")
    print(q_table)
    print(f"Metrics saved to {metrics_filename}")

    # Load and compile data from the analysis directory
    data = load_and_clean_data()
    df = compile_data_to_df(data)
    print("\nCompiled DataFrame:")
    print(df.head())

    # Ensure directory exists for plot saving
    chart_dir = 'analysis/epsilon_greedy/charts'
    ensure_dir_exists(chart_dir)
    plot_save_path = f'{chart_dir}/epsilon_greedy_2d_results_{current_time}.png'
    plt.figure()
    plt.plot(epsilon_values, [0] * len(epsilon_values), 'bo')  # Placeholder plot
    plt.savefig(plot_save_path)
    print(f"Plot saved to {plot_save_path}")
