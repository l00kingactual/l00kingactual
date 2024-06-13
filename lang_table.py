import pandas as pd

# Read the Excel workbook into a dictionary of DataFrames
xls = pd.ExcelFile('lang_table.xlsx')
sheet_names = xls.sheet_names
dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in sheet_names}

# Merge all DataFrames into a master DataFrame
master_df = pd.concat(dfs.values(), axis=1)

# Reset column names for the master DataFrame (if needed)
# master_df.columns = range(len(master_df.columns))

# Display the master DataFrame
print(master_df)

import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel workbook into a dictionary of DataFrames
try:
    xls = pd.ExcelFile('lang_table.xlsx')
    sheet_names = xls.sheet_names
    dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in sheet_names}
except Exception as e:
    print("Error reading Excel file:", str(e))
    exit()

# Merge all DataFrames into a master DataFrame
try:
    master_df = pd.concat(dfs.values(), axis=1)
except Exception as e:
    print("Error merging DataFrames:", str(e))
    exit()

# Reset column names for the master DataFrame (if needed)
# master_df.columns = range(len(master_df.columns))

# Save the master DataFrame to an Excel sheet
import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the Excel workbook
xl = pd.ExcelFile('lang_table.xlsx')

# Create a dictionary of DataFrames for all sheets
dfs = {sheet_name: xl.parse(sheet_name) for sheet_name in xl.sheet_names}

# Combine all DataFrames into one master DataFrame
master_df = pd.concat(dfs.values(), ignore_index=True)

# Define the list of headings
headings = ['Language', 'Sumerian', 'Babylonian', 'Egyptian', 'Roman Numerals', 'Roman Numerals', 'Greek Numerals', 'Number', 'Sumerian', 'Babylonian']

# Choose a specific column by index
column_index = 0  # Replace 0 with the index of the column you want to use

# Extract the column name from the list of headings using the index
numeric_column = headings[column_index]

# Set "0.0" as headings in string
master_df.columns = ['0.0'] + list(master_df.columns[1:])

import pandas as pd
import numpy as np

# Create an empty DataFrame with 123 rows and 388 columns filled with NaN values
master_df = pd.DataFrame(np.nan, index=range(1, 124), columns=range(388))

# You can access and manipulate the DataFrame 'master_df' as needed.



import pandas as pd

# Create an empty DataFrame with 123 rows
master_df = pd.DataFrame(index=range(1, 124))

# Iterate through your existing DataFrames or data sources and add them as columns
# For demonstration purposes, let's assume you have a list of DataFrames named 'dfs'
# dfs = [df1, df2, df3]  # Replace with your actual DataFrames

for idx, df in enumerate(dfs, start=1):
    column_name = f"Column_{idx}"  # Replace with appropriate column names
    master_df[column_name] = df

# Now, 'master_df' contains 123 rows and 388 columns with data from your existing DataFrames.


# Create "0.1" headings and rows as strings, characters, symbols, and digits
for i in range(1, len(master_df.columns)):
    if i % 2 == 0:
        # Even columns (0-based index) are for "0.1" headings
        master_df.iloc[0, i] = "0.1"
    else:
        # Odd columns are for rows as strings, characters, symbols, and digits
        master_df.iloc[:, i] = master_df.iloc[:, i].astype(str)

# Display the modified DataFrame
print(master_df)

# Save the DataFrame to an Excel file
master_df.to_excel("description_00.xlsx", index=False)


import pandas as pd

# Create an empty DataFrame
master_df = pd.DataFrame()

# Dictionary of DataFrames (Replace with your actual DataFrames)
dfs = {
    'Sheet1': pd.DataFrame({'Language': ['English', 'Spanish', 'French', 'German', 'Chinese'],
                            0: ['Zero', 'Cero', 'Zéro', 'Null', '零'],
                            1: ['One', 'Uno', 'Un', 'Eins', '一']}),
    'Sheet2': pd.DataFrame({'Language': ['English', 'Spanish', 'French', 'German', 'Chinese'],
                            0: ['Zero', 'Cero', 'Zéro', 'Null', '零'],
                            1: ['One', 'Uno', 'Un', 'Eins', '一']})
}

try:
    # Concatenate DataFrames from the dictionary
    master_df = pd.concat(dfs.values(), ignore_index=True)

    # Handle column names
    column_names = master_df.columns
    if not column_names.empty:
        # Set the first column to 0.0
        master_df.iloc[0, 0] = 0.0

        # Set the remaining columns as headings
        master_df.iloc[0, 1:] = column_names[1:]

        # Reset column names
        master_df.columns = range(len(column_names))
    else:
        print("No column names found.")

    # Save the DataFrame to an Excel file
    master_df.to_excel("description_00.xlsx", index=False)

    # Print success message
    print("Master DataFrame saved to description_00.xlsx")

except Exception as e:
    # Handle exceptions and print error message
    print(f"An error occurred: {e}")

# Now you have master_df with 388 columns and 123 rows, you can work with it as needed.

import pandas as pd

# Read all sheets from the Excel file into a dictionary of DataFrames
xls = pd.ExcelFile('lang_table.xlsx')
dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}

try:
    # Concatenate DataFrames from the dictionary
    master_df = pd.concat(dfs.values(), ignore_index=True)

    # Handle column names
    column_names = master_df.columns
    if not column_names.empty:
        # Set the first column to 0.0
        master_df.iloc[0, 0] = 0.0

        # Set the remaining columns as headings
        master_df.iloc[0, 1:] = column_names[1:]

        # Reset column names
        master_df.columns = range(len(column_names))
    else:
        print("No column names found.")

    # Save the DataFrame to an Excel file
    master_df.to_excel("description_01.xlsx", index=False)

    # Print success message
    print("Master DataFrame saved to description_00.xlsx")

except Exception as e:
    # Handle exceptions and print error message
    print(f"An error occurred: {e}")

# Now you have master_df with data from all sheets, you can work with it as needed.

''' 

# Check if the selected column exists in the DataFrame
if numeric_column in master_df.columns:
    try:
        # Attempt to plot the selected column, excluding the header row
        plt.plot(master_df.iloc[1:, master_df.columns.get_loc(numeric_column)].astype(float))
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title(f"Plot of {numeric_column}")
        plt.show()
    except (TypeError, ValueError) as e:
        print(f"Error plotting column '{numeric_column}': {str(e)}")
else:
    print(f"Column '{numeric_column}' not found in the DataFrame.")

    '''