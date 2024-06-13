
import pandas as pd
import numpy as np

def extract_wiki_url(text):
    if pd.isna(text):
        return ''
    wiki_base_url = "https://en.wikipedia.org/wiki/"
    words = text.split()
    urls = [wiki_base_url + word.strip('[]()').replace(' ', '_') for word in words if word.startswith(('[', '(')) and word.endswith((']', ')'))]
    return ', '.join(urls)

# File Paths
input_file_path = "path/to/your/original/constellationStars.xlsx"
output_file_path = "path/to/save/final_constellation_data.xlsx"

# Reading the original Excel file
xl_raw = pd.ExcelFile(input_file_path)
df = pd.read_excel(input_file_path, sheet_name='constellation_stars')

# Constants for conversions
ly_to_parsec = 0.306601
ly_to_m = 9.461e15

# Adding and populating new fields
df['distance (parsec)'] = df['Dist. (ly)'] * ly_to_parsec
df['distance (m)'] = df['Dist. (ly)'] * ly_to_m
df['parallax'] = 1 / df['distance (parsec)']
df['parallax'].replace([np.inf, -np.inf], np.nan, inplace=True)

# Populating the 'wikiStarURL' and 'wikiStarNotesURL' fields using existing link data
df['wikiStarURL'] = df['Name'].apply(extract_wiki_url)
df['wikiStarNotesURL'] = df['Notes'].apply(extract_wiki_url)

# Generating a unique conID for each unique constellation
unique_constellations = df['constellation'].unique()
conID_dict = {constellation: index for index, constellation in enumerate(unique_constellations, 1)}
df['conID'] = df['constellation'].map(conID_dict)

# Creating the 'constellation_index' DataFrame
df_constellation_index = pd.DataFrame({
    'conID': list(conID_dict.values()),
    'Constellation': list(conID_dict.keys()),
    'wikiConstellationURL': [f"https://en.wikipedia.org/wiki/{x.replace(' ', '_')}" for x in list(conID_dict.keys())]
})

# Writing all DataFrames to a new Excel file
with pd.ExcelWriter(output_file_path) as writer:
    df.to_excel(writer, sheet_name='constellation_stars', index=False)
    df_constellation_index.to_excel(writer, sheet_name='constellation_index', index=False)

print("Excel file has been successfully generated.")
