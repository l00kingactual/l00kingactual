import matplotlib.pyplot as plt
import numpy as np

# Define your scales and corresponding dates
# Define the scales list
scales = [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360]

# Calculate statistics
count = len(scales)
total_sum = sum(scales)
min_value = min(scales)
max_value = max(scales)
median_value = np.median(scales)
average_value = np.mean(scales)

import matplotlib.pyplot as plt

# Create a dictionary to map column names to their corresponding data
data_dict = {
    "Distance (meters)": [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360],
    "Time (seconds)": [0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25, 28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64, 94, 171, 206, 345, 360],
    "Volume (cubic meters)": [3.141592654, 3.141592654, 9.02902E+26, 3.04729E+29, 7.22322E+29, 1.41078E+29, 5.77857E+29, 1.12863E+30, 1.5022E+30, 1.95027E+30, 2.4796E+30, 3.80912E+30, 4.62286E+30, 7.74126E+30, 1.20176E+31, 1.76348E+31, 2.47756E+31, 3.36229E+31, 3.69829E+31, 4.05595E+31, 4.43596E+31, 4.83899E+31, 5.71684E+31, 1.02846E+32, 1.41078E+32, 1.49714E+32, 1.77718E+32, 2.09014E+32, 2.43784E+32, 2.95863E+32, 9.3742E+32, 5.64338E+33, 9.86626E+33, 4.63455E+34, 5.26573E+34],
    "Pi": [3.141592654] * 35  # All values are the same
}

# Create and save plots for each column
for column_name, data in data_dict.items():
    plt.figure(figsize=(8, 6))
    plt.plot(scales, data, marker='o')
    plt.title(f"{column_name} vs. Scale")
    plt.xlabel("Scale")
    plt.ylabel(column_name)
    plt.grid(True)
    plt.savefig(f"plots\\{column_name}.png")  # Save the plot
    print(f"Saved plot: plots\\{column_name}.png")  # Print the saved file path

    plt.show()  # Display the plot

