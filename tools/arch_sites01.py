import csv

def write_list_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for item in data:
            csvwriter.writerow([item])

# The lists to be written to CSV files
geographical_regions = ["African", "American", "Asian", "Australian", "Oceanian", "Egyptian", "Mesopotamian", "Near Eastern", "Nubian"]
archaeological_sub_disciplines = ["Aerial", "Bioarchaeology", "Archaeogenetics", "Medieval", "Near Eastern", "Osteology", "Paleopathology", "Calceology", "Digital", "Archaeogaming", "Computational", "Virtual", "Environmental", "Geoarchaeology", "Paleoethnobotany", "Zooarchaeology", "Experimental", "Underwater"]
archaeological_paradigms = ["Archaeoastronomy", "Archaeometry", "Battlefield", "Conflict", "Feminist", "Funerary", "Gender", "Indigenous", "Industrial", "Landscape", "Maritime", "Mortuary", "Music", "Nazi", "Phenomenology", "Pseudoarchaeology", "Queer"]

# Writing the lists to CSV files
write_list_to_csv(geographical_regions, 'geographical_regions.csv')
write_list_to_csv(archaeological_sub_disciplines, 'archaeological_sub_disciplines.csv')
write_list_to_csv(archaeological_paradigms, 'archaeological_paradigms.csv')
