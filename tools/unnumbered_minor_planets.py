import pandas as pd

# Step 1: Read the Excel sheet
df = pd.read_excel('wikipeadia\\cleaned_missing_data_v1.xlsx', sheet_name='unnumbered_minor_planets', header=None)

# Step 2: Identify rows containing year ranges
mask = df[0].str.contains('^\d{4}–\d{4}$', na=False, regex=True)

# Create a separate DataFrame to keep track of the year_range
year_range_df = pd.DataFrame(index=df.index)
year_range_df['year_range'] = None
year_range_df.loc[mask, 'year_range'] = df.loc[mask, 0]

# Step 3: Forward-fill the 'year_range' column
year_range_df['year_range'] = year_range_df['year_range'].ffill()

# Step 4: Create a 'integrate_U_E' column (assuming 'U' and 'E' are in columns 0 and 1)
integrate_U_E = df.iloc[:, 0].astype(str) + " & " + df.iloc[:, 1].astype(str)

# Step 5: Construct the unified header
header_1 = df.iloc[0, :].fillna('')
header_2 = df.iloc[1, :].fillna('')
header_unified = [f"{h1} {h2}".strip() for h1, h2 in zip(header_1, header_2)]

# Remove rows that contributed to header and set the new header
df.columns = header_unified
df = df.drop(index=[0, 1]).reset_index(drop=True)

# Add new columns
df['year_range'] = year_range_df['year_range']
df['integrate_U_E'] = integrate_U_E

# Step 6: Reorder columns
columns_reordered = ['year_range', 'integrate_U_E'] + [col for col in df.columns if col not in ['year_range', 'integrate_U_E']]
df = df[columns_reordered]

# Write the cleaned DataFrame to a new Excel file
df.to_excel('wikipeadia\\cleaned_missing_data_v2.xlsx', sheet_name='unnumbered_minor_planets', index=False)
