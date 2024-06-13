import requests
from bs4 import BeautifulSoup
import mysql.connector
import json

# 1. Connect to the MySQL database and test the connection
try:
    conn = mysql.connector.connect(
        host="213.171.200.30",
        user="OuchAstronomy",
        password="@00e54m1sf1t?",
        database="ouchAstronomy"
    )
    cursor = conn.cursor()
    print("Database connection established.")
except Exception as e:
    print(f"Database connection failed: {e}")

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS celestial_objects
                  (name VARCHAR(50) PRIMARY KEY, type VARCHAR(20), data JSON)''')

# 2. Build dictionaries of celestial objects
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
constellation_names = [
    "Andromeda", "Antlia", "Apus", "Aquarius", "Aquila", "Ara", "Aries", "Auriga", "Bootes", "Caelum",
    "Camelopardalis", "Cancer", "Canes Venatici", "Canis Major", "Canis Minor", "Capricornus", "Carina",
    "Cassiopeia", "Centaurus", "Cepheus", "Cetus", "Chamaeleon", "Circinus", "Columba", "Coma Berenices",
    "Corona Australis", "Corona Borealis", "Corvus", "Crater", "Crux", "Cygnus", "Delphinus", "Dorado",
    "Draco", "Equuleus", "Eridanus", "Fornax", "Gemini", "Grus", "Hercules", "Horologium", "Hydra",
    "Hydrus", "Indus", "Lacerta", "Leo", "Leo Minor", "Lepus", "Libra", "Lupus", "Lynx", "Lyra", "Mensa",
    "Microscopium", "Monoceros", "Musca", "Norma", "Octans", "Ophiuchus", "Orion", "Pavo", "Pegasus",
    "Perseus", "Phoenix", "Pictor", "Pisces", "Piscis Austrinus", "Puppis", "Pyxis", "Reticulum", "Sagitta",
    "Sagittarius", "Scorpius", "Sculptor", "Scutum", "Serpens", "Sextans", "Taurus", "Telescopium",
    "Triangulum", "Triangulum Australe", "Tucana", "Ursa Major", "Ursa Minor", "Vela", "Virgo", "Volans", "Vulpecula"
]

moon_names = [
    # Moons of Mercury (None)
    
    # Moons of Venus (None)
    
    # Moons of Earth
    "Moon",
    
    # Moons of Mars
    "Phobos", "Deimos",
    
    # Moons of Jupiter (79)
    "Io", "Europa", "Ganymede", "Callisto", "Adrastea", "Metis", "Amalthea", "Thebe", "Elara", "Himalia", "Leda", "Lysithea", "Erinome", "S/2003 J12", "S/2003 J16", "S/2003 J18", "S/2003 J24", "S/2003 J3", "S/2003 J10", "Taygete", "S/2011 J1", "Carpo", "Kalliope", "Eukelade", "Herse", "S/2003 J15", "S/2003 J9", "Orthosie", "Euporie", "Thelxinoe", "S/2003 J17", "S/2003 J5", "S/2003 J19", "Praxidike", "Mneme", "Cyllene", "S/2003 J4", "Elara (moon)", "S/2003 J14", "S/2003 J2", "Pasiphae", "Ananke", "Iocaste", "S/2011 J2", "Elara (moon)", "Hegemone", "S/2003 J13", "Autonoe", "Sponde", "Megaclite", "Themisto", "S/2003 J23", "Aitne", "Hermippe", "S/2003 J6", "Echephros", "Euanthe", "Eukelade (moon)", "Orthosie (moon)", "S/2003 J11", "S/2003 J7", "Callirrhoe", "Carme", "S/2003 J8", "S/2003 J20", "S/2003 J21", "S/2003 J22", "S/2010 J1",
    
    # Moons of Saturn (82)
    "Titan", "Rhea", "Iapetus", "Dione", "Tethys", "Enceladus", "Mimas", "Hyperion", "Phoebe", "Janus", "Epimetheus", "Atlas", "Prometheus", "Pandora", "Calypso", "Telesto", "E ring", "Aegaeon", "Methone", "Anthe", "Mneme", "Pallene", "Polydeuces", "S/2004 S12", "S/2004 S6", "S/2004 S4", "S/2004 S7", "S/2004 S13", "S/2004 S8", "S/2004 S9", "S/2004 S10", "S/2004 S5", "S/2004 S11", "Ymir", "Kiviuq", "Skathi", "Ijiraq", "Paaliaq", "Tarqeq", "S/2007 S3", "S/2007 S2", "S/2007 S1", "E ring", "Albiorix", "S/2004 S17", "Erriapus", "Bebhionn", "Bergelmir", "Bestla", "Fenrir", "Fornjot", "Hyrrokkin", "Kari", "Loge", "Midgard", "Mundilfari", "Narvi", "Saturn LII", "S/2004 S16", "S/2004 S15", "S/2004 S14", "S/2004 S18", "S/2004 S19"
    
    # Moons of Uranus
    "Miranda", "Ariel", "Umbriel", "Titania", "Oberon", "Caliban", "Sycorax", "Prospero", "Setebos", "Margaret", "Stephano", "Trinculo", "Francisco", "Margaret", "Cupid", "Portia", "Rosalind", "Belinda", "Cressida", "Desdemona", "Juliet", "Ophelia", "Bianca", "Perdita", "Mab", "Cupid"

    # Moons of Neptune
    "Triton", "Nereid", "Naiad", "Thalassa", "Despina", "Galatea", "Larissa", "Proteus", "Halimede", "Psamathe", "Sao", "Laomedeia", "Neso"
    
    # Moons of Pluto
    "Charon", "Nix", "Hydra", "Kerberos", "Styx"
]

# 3. For each celestial object, connect to Wikipedia and get the infobox data
for obj_type, obj_list in [("planet", planet_names), ("constellation", constellation_names)]:
    for obj_name in obj_list:
        url = f"https://en.wikipedia.org/wiki/{obj_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Successfully fetched data for {obj_name}.")
            soup = BeautifulSoup(response.text, 'html.parser')
            infobox = soup.find('table', {'class': 'infobox'})
            
            if infobox:
                obj_data = {}
                for row in infobox.find_all('tr'):
                    header = row.find('th')
                    value = row.find('td')
                    if header and value:
                        obj_data[header.text.strip()] = value.text.strip()
                
                cursor.execute("INSERT INTO celestial_objects (name, type, data) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE data = %s", (obj_name, obj_type, json.dumps(obj_data), json.dumps(obj_data)))
                conn.commit()
                
                print(f"Database updated for {obj_name}.")
                print(f"Infobox data: {obj_data}")
            else:
                print(f"No infobox found for {obj_name}.")
        else:
            print(f"Failed to fetch data for {obj_name}.")

# Close the MySQL database connection
conn.close()
