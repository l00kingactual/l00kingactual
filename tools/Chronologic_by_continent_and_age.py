import os
import pandas as pd

# Initial lists
geographical_regions = ["African", "American", "Asian", "Australian", "Oceanian", "Egyptian", "Mesopotamian", "Near Eastern", "Nubian"]
archaeological_sub_disciplines = ["Aerial", "Bioarchaeology", "Archaeogenetics", "Medieval", "Near Eastern", "Osteology", "Paleopathology", "Calceology", "Digital", "Archaeogaming", "Computational", "Virtual", "Environmental", "Geoarchaeology", "Paleoethnobotany", "Zooarchaeology", "Experimental", "Underwater"]
archaeological_paradigms = ["Archaeoastronomy", "Archaeometry", "Battlefield", "Conflict", "Feminist", "Funerary", "Gender", "Indigenous", "Industrial", "Landscape", "Maritime", "Mortuary", "Music", "Nazi", "Phenomenology", "Pseudoarchaeology", "Queer"]

# Directory and output file
input_dir = 'wikipeadia\\arch\\'
output_file = 'combined_data.xlsx'

# DataFrames holder
dfs = {}

# Read each CSV file into a DataFrame and store it in a dictionary
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        sheet_name = filename[:-4].replace('List_of_', '')  # Remove 'List_of_' prefix and '.csv' suffix
        dfs[sheet_name] = pd.read_csv(os.path.join(input_dir, filename))

# Add new data as separate sheets
dfs['Chronologicby_continent_and_age'] = pd.DataFrame({'Geographical Regions': geographical_regions})
dfs['Archaeological Sub-disciplines'] = pd.DataFrame({'Archaeological Sub-disciplines': archaeological_sub_disciplines})
dfs['Archaeological Paradigms'] = pd.DataFrame({'Archaeological Paradigms': archaeological_paradigms})

# Write to Excel
with pd.ExcelWriter(output_file) as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
