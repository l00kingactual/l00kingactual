def generate_python_script(data):
    with open("generated_class_instances.py", "w") as f:
        f.write("from class_definition import ArchaeologicalSites, Continent, Age\n\n")
        
        # Instantiate Age objects
        for continent, ages in data.items():
            for age, sites in ages.items():
                sites_list = ", ".join([f'"{site}"' for site in sites])
                f.write(f"{age.replace(' ', '_').replace('-', '_')} = Age('{age}', [{sites_list}])\n")

        # Instantiate Continent objects
        for continent, ages in data.items():
            age_objects = ", ".join([age.replace(' ', '_').replace('-', '_') for age in ages.keys()])
            f.write(f"{continent.replace(' ', '_').replace('-', '_')} = Continent('{continent}', [{age_objects}])\n")

        # Instantiate the main ArchaeologicalSites object
        continent_objects = ", ".join([continent.replace(' ', '_').replace('-', '_') for continent in data.keys()])
        f.write(f"archaeological_sites = ArchaeologicalSites([{continent_objects}])\n")

# Assume 'scraped_data' is a nested dictionary representing the scraped data
# E.g., {'Africa': {'Stone Age': ['Site 1', 'Site 2'], 'Bronze Age': ['Site 3']}, 'Europe': {'Iron Age': ['Site 4']}}
scraped_data = {
    'Africa': {'Stone Age': ['Site 1', 'Site 2'], 'Bronze Age': ['Site 3']},
    'Europe': {'Iron Age': ['Site 4']}
}
generate_python_script(scraped_data)
