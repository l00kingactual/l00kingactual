import pandas as pd
import json

class_code = '''
import json

class ArchaeologicalSitesStatic:
    def __init__(self, static_description):
        self.static_description = static_description

    def __str__(self):
        return json.dumps(self.static_description, indent=4)
'''

def generate_archaeological_sites_py(excel_file_path, py_file_path):
    xls = pd.ExcelFile(excel_file_path)
    static_description = {}  # This dictionary will contain a unified description of all data

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name)
        df = df.where(pd.notna(df), None)  # Replace NaN with None
        static_description[sheet_name] = {
            "columns": list(df.columns),
            "data_types": [str(df[col].dtype) for col in df.columns],
            "head": df.head().to_dict(orient='records')
        }

    with open(py_file_path, 'w') as py_file:
        py_file.write(f'{class_code}\n')
        py_file.write(f'static_description = {json.dumps(static_description, indent=4)}\n')
        py_file.write('\narchaeological_sites = ArchaeologicalSitesStatic(static_description)\n')
        py_file.write('print(archaeological_sites)\n')

# Generate the Python file with the class definition and static description
generate_archaeological_sites_py("wikipeadia\\arch\\combined_data.xlsx", "archaeological_sites.py")
