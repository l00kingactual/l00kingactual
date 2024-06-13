import numpy as np
from tabulate import tabulate
import math
from termcolor import colored
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored  # Import colored function from termcolor library for text coloring

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

# Print the results
print(f"Count: {count}")
print(f"Sum: {total_sum}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Median: {median_value}")
print(f"Average: {average_value}")



# Calculate the value using the mathematical expression
pi_value = math.pi
actual_value = 100 - pi_value * 1000

your_dates = [
    '15 billion years ago',
    '13.8 billion years ago',
    '5 billion years ago',
    '1 billion years ago',
    '500 million years ago',
    '10 million years ago',
    '5 million years ago',
    '1 million years ago',
    '100,000 years ago BCE',
    '15,000 years ago BCE',
    '5,000 years ago BCE',
    '0 BCE',
    '10 BCE',
    '100 BCE',
    '1000 BCE',
    '100 BCE + 100',
    '100 BCE + 1000',
    '100 BCE + 2000',
    '100 BCE + 2025',
    '100 BCE + 2050',
    '100 BCE + 2100',
    '100 BCE + 2200',
    '100 BCE + 2300',
    '100 BCE + 2400',
    '100 BCE + 2500',
    '100 BCE + 5000',
    '100 BCE + 7500',
    '100 BCE + 10000',
    '100 BCE + 15000',
    '100 BCE + 20000',
    '100 BCE + 25000',
    '100 BCE + 30000',
    '100 BCE + 50000',
    '100 BCE + 60000',
    f'{actual_value} BCE'
]


# Update the your_dates list
your_dates[-1] = f'{actual_value} BCE'

# Calculate statistics
count = len(your_dates)

# Print the results
print(f"Count: {count}")
print("Dates:")
for date in your_dates:
    print(date)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from termcolor import colored  # You can use 'colored' for colored output

# Create a bar chart to visualize the dates vs. scales
plt.figure(figsize=(12, 6))
plt.bar(scales, range(len(scales)), tick_label=your_dates, color='skyblue')
plt.xlabel('Corresponding Date')
plt.ylabel('Scale')
plt.title('Dates vs. Scales')
plt.xticks(rotation=90)
plt.tight_layout()

# Initialize lists to store statistical results
slopes = []
intercepts = []
correlation_coefficients = []

# Iterate over each date and calculate statistical results
for scale, date in zip(scales, your_dates):
    scale_values = np.array([scale])
    date_values = np.array([scales.index(scale)])

    # Create a Ridge regression model
    ridge = Ridge(alpha=1.0)

    # Fit the model to your data
    ridge.fit(scale_values.reshape(-1, 1), date_values)

    # Get the coefficients
    slope = ridge.coef_[0]
    intercept = ridge.intercept_

    # Calculate correlation coefficient (if needed)
    correlation_coefficient = np.corrcoef(scale_values, date_values)[0, 1]

    # Append results to lists
    slopes.append(slope)
    intercepts.append(intercept)
    correlation_coefficients.append(correlation_coefficient)

    # Print statistical results for each date
    print(colored(f"Statistical Trend Analysis for {date}:", "green"))
    print(f"Linear Regression Slope: {slope:.4f}")
    print(f"Linear Regression Intercept: {intercept:.4f}")
    print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Show the plot with the trend line
plt.show()

# Print overall statistical results
print(colored("Overall Statistical Trend Analysis:", "green"))
print(f"Mean of Scales: {np.mean(scales):.4f}")
print(f"Standard Deviation of Scales: {np.std(scales):.4f}")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from termcolor import colored

# Rescale the x-axis
min_date = min(your_dates)
max_date = max(your_dates)

# Extract the numerical values from the date strings
min_value = float(min_date.split(' ')[0])
max_value = float(max_date.split(' ')[0])

# Define the new minimum and maximum values for the x-axis
new_min = 0.0
new_max = 110000.0  # 110 BCE + 20k

# Rescale the scales to the new range
rescaled_scales = [new_min + (new_max - new_min) * (scale - min_value) / (max_value - min_value) for scale in scales]

# Create a bar chart with rescaled scales
plt.figure(figsize=(12, 6))
plt.bar(rescaled_scales, range(len(scales)), tick_label=your_dates, color='skyblue')
plt.xlabel('Corresponding Date')
plt.ylabel('Rescaled Scale')
plt.title('Rescaled Dates vs. Scales')
plt.xticks(rotation=90)
plt.tight_layout()

# Initialize lists to store statistical results
slopes = []
intercepts = []
correlation_coefficients = []

# Iterate over each date and calculate statistical results
for scale, date in zip(rescaled_scales, your_dates):
    scale_values = np.array([scale])
    date_values = np.array([rescaled_scales.index(scale)])

    # Create a Ridge regression model
    ridge = Ridge(alpha=1.0)

    # Fit the model to your data
    ridge.fit(scale_values.reshape(-1, 1), date_values)

    # Get the coefficients
    slope = ridge.coef_[0]
    intercept = ridge.intercept_

    # Calculate correlation coefficient (if needed)
    correlation_coefficient = np.corrcoef(scale_values, date_values)[0, 1]

    # Append results to lists
    slopes.append(slope)
    intercepts.append(intercept)
    correlation_coefficients.append(correlation_coefficient)

    # Print statistical results for each date
    print(colored(f"Statistical Trend Analysis for {date}:", "green"))
    print(f"Linear Regression Slope: {slope:.4f}")
    print(f"Linear Regression Intercept: {intercept:.4f}")
    print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Show the plot with the trend line
plt.show()

# Print overall statistical results
print(colored("Overall Statistical Trend Analysis:", "green"))
print(f"Mean of Rescaled Scales: {np.mean(rescaled_scales):.4f}")
print(f"Standard Deviation of Rescaled Scales: {np.std(rescaled_scales):.4f}")

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from termcolor import colored

# Define the new minimum and maximum values for the corresponding dates
new_min_date = '0 BCE'
new_max_date = '110 BCE + 20,000'

# Create a function to convert dates to numerical values
def date_to_numerical(date_str):
    parts = date_str.split(' ')
    value = float(parts[0].replace(',', ''))  # Remove commas before converting to float
    if 'billion' in parts[1]:
        value *= 1e9
    elif 'million' in parts[1]:
        value *= 1e6
    elif 'thousand' in parts[1]:
        value *= 1e3
    return value

# Convert the new min and max dates to numerical values
new_min_value = date_to_numerical(new_min_date)
new_max_value = date_to_numerical(new_max_date)

# Initialize lists to store rescaled date values
rescaled_dates = []

# Iterate over each date and rescale it to the new range
for date in your_dates:
    date_value = date_to_numerical(date)
    rescaled_value = new_min_value + (new_max_value - new_min_value) * (date_value - date_to_numerical(min(your_dates))) / (date_to_numerical(max(your_dates)) - date_to_numerical(min(your_dates)))
    rescaled_dates.append(rescaled_value)

# Create a bar chart with rescaled dates
plt.figure(figsize=(12, 6))
plt.bar(scales, range(len(scales)), tick_label=rescaled_dates, color='skyblue')
plt.xlabel('Rescaled Corresponding Date')
plt.ylabel('Scale')
plt.title('Rescaled Dates vs. Scales')
plt.xticks(rotation=90)
plt.tight_layout()

# Initialize lists to store statistical results
slopes = []
intercepts = []
correlation_coefficients = []

# Iterate over each date and calculate statistical results
for scale, rescaled_date in zip(scales, rescaled_dates):
    scale_values = np.array([scale])
    date_values = np.array([rescaled_date])

    # Create a Ridge regression model
    ridge = Ridge(alpha=1.0)

    # Fit the model to your data
    ridge.fit(scale_values.reshape(-1, 1), date_values)

    # Get the coefficients
    slope = ridge.coef_[0]
    intercept = ridge.intercept_

    # Calculate correlation coefficient (if needed)
    correlation_coefficient = np.corrcoef(scale_values, date_values)[0, 1]

    # Append results to lists
    slopes.append(slope)
    intercepts.append(intercept)
    correlation_coefficients.append(correlation_coefficient)

    # Print statistical results for each date
    print(colored(f"Statistical Trend Analysis for {date}:", "green"))
    print(f"Linear Regression Slope: {slope:.4f}")
    print(f"Linear Regression Intercept: {intercept:.4f}")
    print(f"Correlation Coefficient: {correlation_coefficient:.4f}")

# Show the plot with the trend line
plt.show()

# Print overall statistical results
print(colored("Overall Statistical Trend Analysis:", "green"))
print(f"Mean of Scales: {np.mean(scales):.4f}")
print(f"Standard Deviation of Scales: {np.std(scales):.4f}")

import matplotlib.pyplot as plt
from termcolor import colored

# Define the specific number groups and their corresponding date ranges
number_groups = [
    {"name": "Group 1", "start_scale": 0, "end_scale": 10},
    {"name": "Group 2", "start_scale": 11, "end_scale": 25},
    {"name": "Group 3", "start_scale": 26, "end_scale": 50},
    {"name": "Group 4", "start_scale": 51, "end_scale": 94},  # Adjust the end_scale for Group 4
    {"name": "Group 5", "start_scale": 95, "end_scale": 360},  # Adjust the start_scale for Group 5
]





import os
import matplotlib.pyplot as plt
from termcolor import colored  # If not already imported

# Define the "plots" folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Create plots for each number group
for group in number_groups:
    # Filter scales and dates for the current group
    group_scales = scales[group["start_scale"]:group["end_scale"] + 1]
    group_dates = your_dates[group["start_scale"]:group["end_scale"] + 1]

    # Create a bar chart for the group
    plt.figure(figsize=(12, 6))
    plt.bar(group_scales, range(len(group_scales)), tick_label=group_dates, color='skyblue')
    plt.xlabel('Corresponding Date')
    plt.ylabel('Scale')
    plt.title(f'Dates vs. Scales for {group["name"]}')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the plot to the "plots" folder
    plot_filename = f"plots/{group['name']}_plot.png"
    plt.savefig(plot_filename)

    # Show the plot for the current group
    plt.show()

    # Print a message indicating the group's range in the console log
    print(colored(f"Number Group: {group['name']}", "green"))
    print(f"Start Scale: {group['start_scale']}")
    print(f"End Scale: {group['end_scale']}\n")

    # Print the path to the saved plot in the console log
    print(f"Plot saved as: {plot_filename}\n")

import os
import matplotlib.pyplot as plt
import pandas as pd
from termcolor import colored  # If not already imported

# Define the "plots" folder if it doesn't exist
if not os.path.exists("plots"):
    os.makedirs("plots")

# Create an Excel writer to save dataframes to an Excel file
excel_writer = pd.ExcelWriter('group_data.xlsx', engine='xlsxwriter')

# Create plots and save data for each number group
for group in number_groups:
    # Filter scales and dates for the current group
    group_scales = scales[group["start_scale"]:group["end_scale"] + 1]
    group_dates = your_dates[group["start_scale"]:group["end_scale"] + 1]

    # Create a bar chart for the group
    plt.figure(figsize=(12, 6))
    plt.bar(group_scales, range(len(group_scales)), tick_label=group_dates, color='skyblue')
    plt.xlabel('Corresponding Date')
    plt.ylabel('Scale')
    plt.title(f'Dates vs. Scales for {group["name"]}')
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Save the plot to the "plots" folder
    plot_filename = f"plots/{group['name']}_plot.png"
    plt.savefig(plot_filename)

    # Save the data to a CSV file
    data = {'Scale': group_scales, 'Corresponding Date': group_dates}
    df = pd.DataFrame(data)
    csv_filename = f"plots/{group['name']}_data.csv"
    df.to_csv(csv_filename, index=False)

    # Add the data as a new sheet to the Excel workbook
    df.to_excel(excel_writer, sheet_name=group['name'], index=False)

    # Show the plot for the current group
    plt.show()

    # Print a message indicating the group's range in the console log
    print(colored(f"Number Group: {group['name']}", "green"))
    print(f"Start Scale: {group['start_scale']}")
    print(f"End Scale: {group['end_scale']}\n")

    # Print the path to the saved plot and data CSV file in the console log
    print(f"Plot saved as: {plot_filename}")
    print(f"Data saved as: {csv_filename}\n")

import openpyxl

# Create a new Excel workbook
workbook = openpyxl.Workbook()

# Iterate over each number group
for group in number_groups:
    # Filter scales and dates for the current group
    group_scales = scales[group["start_scale"]:group["end_scale"] + 1]
    group_dates = your_dates[group["start_scale"]:group["end_scale"] + 1]

    # Create a new worksheet for the current group
    worksheet = workbook.create_sheet(title=group["name"])

    # Add headers
    worksheet.append(["Scale", "Corresponding Date"])

    # Add data rows
    for scale, date in zip(group_scales, group_dates):
        worksheet.append([scale, date])

# Remove the default sheet created when the workbook was initialized
workbook.remove(workbook.active)

# Save the Excel file
workbook.save('group_data.xlsx')



# Print a message indicating the Excel workbook has been saved
print(colored("Excel workbook saved as: group_data.xlsx", "green"))
