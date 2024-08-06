import matplotlib.pyplot as plt
import numpy as np

# Number sequence
scales = [  
    0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
]

# Print the scales
for scale in scales:
    print(scale)

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(scales, marker='o')
plt.title("Scales Plot")
plt.xlabel("Index")
plt.ylabel("Scale Value")
plt.grid(True)
plt.show()

# Calculate statistics
sum_scales = sum(scales)
min_scale = min(scales)
max_scale = max(scales)
median_scale = np.median(scales)
average_scale = np.mean(scales)

# Print statistics to console
print(f"Sum of scales: {sum_scales}")
print(f"Minimum scale: {min_scale}")
print(f"Maximum scale: {max_scale}")
print(f"Median scale: {median_scale}")
print(f"Average scale: {average_scale}")

# Create charts for statistics
plt.figure(figsize=(12, 6))

# Bar chart for sum
plt.subplot(1, 2, 1)
plt.bar(["Sum"], [sum_scales], color='skyblue')
plt.title("Sum of Scales")
plt.grid(True)

# Bar chart for min, max, median, and average
plt.subplot(1, 2, 2)
stats_labels = ["Min", "Max", "Median", "Average"]
stats_values = [min_scale, max_scale, median_scale, average_scale]
plt.bar(stats_labels, stats_values, color=['lightcoral', 'lightgreen', 'lightblue', 'lightyellow'])
plt.title("Statistics of Scales")
plt.grid(True)

plt.tight_layout()
plt.show()

# Original unsorted scales list
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Sort the scales list in ascending order
sorted_scales = sorted(scales)

# Print the sorted scales
for scale in sorted_scales:
    print(scale)

# Sort the scales list in descending order
sorted_scales_desc = sorted(scales, reverse=True)

# Print the sorted scales in descending order
for scale in sorted_scales_desc:
    print(scale)
import matplotlib.pyplot as plt

# Original unsorted scales list
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Sort the scales list in ascending order
sorted_scales_asc = sorted(scales)

# Sort the scales list in descending order
sorted_scales_desc = sorted(scales, reverse=True)

# Create a figure with two subplots
plt.figure(figsize=(12, 6))

# Plot the original unsorted scales
plt.subplot(1, 3, 1)
plt.plot(scales, marker='o', label="Original")
plt.title("Original Scales")
plt.xlabel("Index")
plt.ylabel("Scale")
plt.grid(True)
plt.legend()

# Plot the sorted scales in ascending order
plt.subplot(1, 3, 2)
plt.plot(sorted_scales_asc, marker='o', color='orange', label="Ascending")
plt.title("Ascending Sorted Scales")
plt.xlabel("Index")
plt.ylabel("Scale")
plt.grid(True)
plt.legend()

# Plot the sorted scales in descending order
plt.subplot(1, 3, 3)
plt.plot(sorted_scales_desc, marker='o', color='green', label="Descending")
plt.title("Descending Sorted Scales")
plt.xlabel("Index")
plt.ylabel("Scale")
plt.grid(True)
plt.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()
