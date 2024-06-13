time_concepts = {
    "The Arrow of Time": "Refers to the unidirectional flow of time from the past to the future, highlighting its irreversible nature.",
    "The Arrow of Time from a Point": "Focuses on the observation of time's progression from a specific moment, emphasizing the directional flow from that point.",
    "Linear Time": "Views time as a sequence of events in a constant, straight progression, where each moment follows the previous one at a uniform rate.",
    "Non-Linear Time": "Suggests that the flow of time is not uniform; it can vary, allowing for a perception of time that can speed up or slow down.",
    "Dynamic Time": "Represents a model of time that is fluid and changeable, acknowledging that the flow and perception of time can be influenced by various factors."
}

arrow_of_time = "Refers to the unidirectional flow of time from the past to the future, highlighting its irreversible nature."

arrow_of_time_from_a_point = "Focuses on the observation of time's progression from a specific moment, emphasizing the directional flow from that point."

linear_time = "Views time as a sequence of events in a constant, straight progression, where each moment follows the previous one at a uniform rate."

non_linear_time = "Suggests that the flow of time is not uniform; it can vary, allowing for a perception of time that can speed up or slow down."

dynamic_time = "Represents a model of time that is fluid and changeable, acknowledging that the flow and perception of time can be influenced by various factors."


print(f"Linear Time: {linear_time} hours")
print(f"Non-Linear Time: {non_linear_time} hours")
print(f"Dynamic Time: {dynamic_time} hours")


import matplotlib.pyplot as plt
import numpy as np

# Planck time (in seconds), the smallest measurable unit of time according to quantum mechanics
planck_time = 5.391247e-44

# Linear time: Simply progresses, e.g., adding 5 Planck times
linear_time = planck_time + 5 * planck_time

# Non-Linear time: Time progression is squared to simulate acceleration
non_linear_time = planck_time**2

# Dynamic time: Time progression is adjusted by a dynamic factor (e.g., time slows down)
dynamic_factor = 0.5
dynamic_time = planck_time * dynamic_factor

# Arrow of Time: Represented by a single progression in Planck time for simplicity
arrow_of_time = planck_time

# Arrow of Time from a Point: Similar to Arrow of Time, but emphasized as a starting point
arrow_of_time_from_a_point = planck_time

# List all time variables
time_variables = {
    "Planck Time": planck_time,
    "Linear Time": linear_time,
    "Non-Linear Time": non_linear_time,
    "Dynamic Time": dynamic_time,
    "Arrow of Time": arrow_of_time,
    "Arrow of Time from a Point": arrow_of_time_from_a_point
}

# Print the time variables
for name, value in time_variables.items():
    print(f"{name}: {value} seconds")

# Plotting
names = list(time_variables.keys())
values = list(time_variables.values())

plt.figure(figsize=(10, 6))
plt.bar(names, values, color='skyblue')
plt.yscale('log')  # Using logarithmic scale due to the vast range of values
plt.ylabel('Time (seconds, log scale)')
plt.title('Representation of Time Concepts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
