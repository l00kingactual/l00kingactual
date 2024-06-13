import pandas as pd

# Create an empty DataFrame with 123 rows
master_df = pd.DataFrame(index=range(1, 124))

# Iterate through your existing DataFrames or data sources and add them as columns
# For demonstration purposes, let's assume you have a list of DataFrames named 'dfs'
dfs = [df1, df2, df3]  # Replace with your actual DataFrames

for idx, df in enumerate(dfs, start=1):
    column_name = f"Column_{idx}"  # Replace with appropriate column names
    master_df[column_name] = df

# Now, 'master_df' contains 123 rows and 388 columns with data from your existing DataFrames.
