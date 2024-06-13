elements_dict = {
    1: {'Symbol': 'H', 'Name': 'Hydrogen', 'Electrons': 1, 'Shells': [1]},
    2: {'Symbol': 'He', 'Name': 'Helium', 'Electrons': 2, 'Shells': [2]},
    3: {'Symbol': 'Li', 'Name': 'Lithium', 'Electrons': 3, 'Shells': [2, 1]},
    4: {'Symbol': 'Be', 'Name': 'Beryllium', 'Electrons': 4, 'Shells': [2, 2]},
    5: {'Symbol': 'B', 'Name': 'Boron', 'Electrons': 5, 'Shells': [2, 3]},
    6: {'Symbol': 'C', 'Name': 'Carbon', 'Electrons': 6, 'Shells': [2, 4]},
    7: {'Symbol': 'N', 'Name': 'Nitrogen', 'Electrons': 7, 'Shells': [2, 5]},
    8: {'Symbol': 'O', 'Name': 'Oxygen', 'Electrons': 8, 'Shells': [2, 6]},
    9: {'Symbol': 'F', 'Name': 'Fluorine', 'Electrons': 9, 'Shells': [2, 7]},
    10: {'Symbol': 'Ne', 'Name': 'Neon', 'Electrons': 10, 'Shells': [2, 8]},
    11: {'Symbol': 'Na', 'Name': 'Sodium', 'Electrons': 11, 'Shells': [2, 8, 1]},
    12: {'Symbol': 'Mg', 'Name': 'Magnesium', 'Electrons': 12, 'Shells': [2, 8, 2]},
    13: {'Symbol': 'Al', 'Name': 'Aluminium', 'Electrons': 13, 'Shells': [2, 8, 3]},
    14: {'Symbol': 'Si', 'Name': 'Silicon', 'Electrons': 14, 'Shells': [2, 8, 4]},
    15: {'Symbol': 'P', 'Name': 'Phosphorus', 'Electrons': 15, 'Shells': [2, 8, 5]},
    16: {'Symbol': 'S', 'Name': 'Sulfur', 'Electrons': 16, 'Shells': [2, 8, 6]},
    17: {'Symbol': 'Cl', 'Name': 'Chlorine', 'Electrons': 17, 'Shells': [2, 8, 7]},
    18: {'Symbol': 'Ar', 'Name': 'Argon', 'Electrons': 18, 'Shells': [2, 8, 8]},
    19: {'Symbol': 'K', 'Name': 'Potassium', 'Electrons': 19, 'Shells': [2, 8, 8, 1]},
    20: {'Symbol': 'Ca', 'Name': 'Calcium', 'Electrons': 20, 'Shells': [2, 8, 8, 2]},
    21: {'Symbol': 'Sc', 'Name': 'Scandium', 'Electrons': 21, 'Shells': [2, 8, 9, 2]},
    22: {'Symbol': 'Ti', 'Name': 'Titanium', 'Electrons': 22, 'Shells': [2, 8, 10, 2]},
    23: {'Symbol': 'V', 'Name': 'Vanadium', 'Electrons': 23, 'Shells': [2, 8, 11, 2]},
    24: {'Symbol': 'Cr', 'Name': 'Chromium', 'Electrons': 24, 'Shells': [2, 8, 13, 1]},
    25: {'Symbol': 'Mn', 'Name': 'Manganese', 'Electrons': 25, 'Shells': [2, 8, 13, 2]},
    26: {'Symbol': 'Fe', 'Name': 'Iron', 'Electrons': 26, 'Shells': [2, 8, 14, 2]},
    27: {'Symbol': 'Co', 'Name': 'Cobalt', 'Electrons': 27, 'Shells': [2, 8, 15, 2]},
    28: {'Symbol': 'Ni', 'Name': 'Nickel', 'Electrons': 28, 'Shells': [2, 8, 16, 2]},
    29: {'Symbol': 'Cu', 'Name': 'Copper', 'Electrons': 29, 'Shells': [2, 8, 18, 1]},
    30: {'Symbol': 'Zn', 'Name': 'Zinc', 'Electrons': 30, 'Shells': [2, 8, 18, 2]},
    31: {'Symbol': 'Ga', 'Name': 'Gallium', 'Electrons': 31, 'Shells': [2, 8, 18, 3]},
    32: {'Symbol': 'Ge', 'Name': 'Germanium', 'Electrons': 32, 'Shells': [2, 8, 18, 4]},
    # ... Continue for other elements
    33: {'Symbol': 'As', 'Name': 'Arsenic', 'Electrons': 33, 'Shells': [2, 8, 18, 5]},
    34: {'Symbol': 'Se', 'Name': 'Selenium', 'Electrons': 34, 'Shells': [2, 8, 18, 6]},
    35: {'Symbol': 'Br', 'Name': 'Bromine', 'Electrons': 35, 'Shells': [2, 8, 18, 7]},
    36: {'Symbol': 'Kr', 'Name': 'Krypton', 'Electrons': 36, 'Shells': [2, 8, 18, 8]},
    37: {'Symbol': 'Rb', 'Name': 'Rubidium', 'Electrons': 37, 'Shells': [2, 8, 18, 8, 1]},
    38: {'Symbol': 'Sr', 'Name': 'Strontium', 'Electrons': 38, 'Shells': [2, 8, 18, 8, 2]},
    39: {'Symbol': 'Y', 'Name': 'Yttrium', 'Electrons': 39, 'Shells': [2, 8, 18, 9, 2]},
    40: {'Symbol': 'Zr', 'Name': 'Zirconium', 'Electrons': 40, 'Shells': [2, 8, 18, 10, 2]},
    41: {'Symbol': 'Nb', 'Name': 'Niobium', 'Electrons': 41, 'Shells': [2, 8, 18, 12, 1]},
    42: {'Symbol': 'Mo', 'Name': 'Molybdenum', 'Electrons': 42, 'Shells': [2, 8, 18, 13, 1]},
    43: {'Symbol': 'Tc', 'Name': 'Technetium', 'Electrons': 43, 'Shells': [2, 8, 18, 13, 2]},
    44: {'Symbol': 'Ru', 'Name': 'Ruthenium', 'Electrons': 44, 'Shells': [2, 8, 18, 15, 1]},
    45: {'Symbol': 'Rh', 'Name': 'Rhodium', 'Electrons': 45, 'Shells': [2, 8, 18, 16, 1]},
    46: {'Symbol': 'Pd', 'Name': 'Palladium', 'Electrons': 46, 'Shells': [2, 8, 18, 18, 0]},
    47: {'Symbol': 'Ag', 'Name': 'Silver', 'Electrons': 47, 'Shells': [2, 8, 18, 18, 1]},
    48: {'Symbol': 'Cd', 'Name': 'Cadmium', 'Electrons': 48, 'Shells': [2, 8, 18, 18, 2]},
    49: {'Symbol': 'In', 'Name': 'Indium', 'Electrons': 49, 'Shells': [2, 8, 18, 18, 3]},
    50: {'Symbol': 'Sn', 'Name': 'Tin', 'Electrons': 50, 'Shells': [2, 8, 18, 18, 4]},
    51: {'Symbol': 'Sb', 'Name': 'Antimony', 'Electrons': 51, 'Shells': [2, 8, 18, 18, 5]},
    52: {'Symbol': 'Te', 'Name': 'Tellurium', 'Electrons': 52, 'Shells': [2, 8, 18, 18, 6]},
    53: {'Symbol': 'I', 'Name': 'Iodine', 'Electrons': 53, 'Shells': [2, 8, 18, 18, 7]},
    54: {'Symbol': 'Xe', 'Name': 'Xenon', 'Electrons': 54, 'Shells': [2, 8, 18, 18, 8]},
    55: {'Symbol': 'Cs', 'Name': 'Cesium', 'Electrons': 55, 'Shells': [2, 8, 18, 18, 8, 1]},
    55: {'Symbol': 'Cs', 'Name': 'Cesium', 'Electrons': 55, 'Shells': [2, 8, 18, 18, 8, 1]},
    56: {'Symbol': 'Ba', 'Name': 'Barium', 'Electrons': 56, 'Shells': [2, 8, 18, 18, 8, 2]},
    57: {'Symbol': 'La', 'Name': 'Lanthanum', 'Electrons': 57, 'Shells': [2, 8, 18, 18, 9, 2]},
    58: {'Symbol': 'Ce', 'Name': 'Cerium', 'Electrons': 58, 'Shells': [2, 8, 18, 19, 9, 2]},
    59: {'Symbol': 'Pr', 'Name': 'Praseodymium', 'Electrons': 59, 'Shells': [2, 8, 18, 21, 8, 2]},
    60: {'Symbol': 'Nd', 'Name': 'Neodymium', 'Electrons': 60, 'Shells': [2, 8, 18, 22, 8, 2]},
    61: {'Symbol': 'Pm', 'Name': 'Promethium', 'Electrons': 61, 'Shells': [2, 8, 18, 23, 8, 2]},
    62: {'Symbol': 'Sm', 'Name': 'Samarium', 'Electrons': 62, 'Shells': [2, 8, 18, 24, 8, 2]},
    63: {'Symbol': 'Eu', 'Name': 'Europium', 'Electrons': 63, 'Shells': [2, 8, 18, 25, 8, 2]},
    64: {'Symbol': 'Gd', 'Name': 'Gadolinium', 'Electrons': 64, 'Shells': [2, 8, 18, 25, 9, 2]},
    # ...
    65: {'Symbol': 'Tb', 'Name': 'Terbium', 'Electrons': 65, 'Shells': [2, 8, 18, 27, 8, 2]},
    66: {'Symbol': 'Dy', 'Name': 'Dysprosium', 'Electrons': 66, 'Shells': [2, 8, 18, 28, 8, 2]},
    67: {'Symbol': 'Ho', 'Name': 'Holmium', 'Electrons': 67, 'Shells': [2, 8, 18, 29, 8, 2]},
    68: {'Symbol': 'Er', 'Name': 'Erbium', 'Electrons': 68, 'Shells': [2, 8, 18, 30, 8, 2]},
    69: {'Symbol': 'Tm', 'Name': 'Thulium', 'Electrons': 69, 'Shells': [2, 8, 18, 31, 8, 2]},
    70: {'Symbol': 'Yb', 'Name': 'Ytterbium', 'Electrons': 70, 'Shells': [2, 8, 18, 32, 8, 2]},
    71: {'Symbol': 'Lu', 'Name': 'Lutetium', 'Electrons': 71, 'Shells': [2, 8, 18, 32, 9, 2]},
    72: {'Symbol': 'Hf', 'Name': 'Hafnium', 'Electrons': 72, 'Shells': [2, 8, 18, 32, 10, 2]},
    73: {'Symbol': 'Ta', 'Name': 'Tantalum', 'Electrons': 73, 'Shells': [2, 8, 18, 32, 11, 2]},
    74: {'Symbol': 'W', 'Name': 'Tungsten', 'Electrons': 74, 'Shells': [2, 8, 18, 32, 12, 2]},
    75: {'Symbol': 'Re', 'Name': 'Rhenium', 'Electrons': 75, 'Shells': [2, 8, 18, 32, 13, 2]},
    76: {'Symbol': 'Os', 'Name': 'Osmium', 'Electrons': 76, 'Shells': [2, 8, 18, 32, 14, 2]},
    77: {'Symbol': 'Ir', 'Name': 'Iridium', 'Electrons': 77, 'Shells': [2, 8, 18, 32, 15, 2]},
    78: {'Symbol': 'Pt', 'Name': 'Platinum', 'Electrons': 78, 'Shells': [2, 8, 18, 32, 17, 1]},
    79: {'Symbol': 'Au', 'Name': 'Gold', 'Electrons': 79, 'Shells': [2, 8, 18, 32, 18, 1]},
    80: {'Symbol': 'Hg', 'Name': 'Mercury', 'Electrons': 80, 'Shells': [2, 8, 18, 32, 18, 2]},
    81: {'Symbol': 'Tl', 'Name': 'Thallium', 'Electrons': 81, 'Shells': [2, 8, 18, 32, 18, 3]},
    82: {'Symbol': 'Pb', 'Name': 'Lead', 'Electrons': 82, 'Shells': [2, 8, 18, 32, 18, 4]},
    # ...
    83: {'Symbol': 'Bi', 'Name': 'Bismuth', 'Electrons': 83, 'Shells': [2, 8, 18, 32, 18, 5]},
    84: {'Symbol': 'Po', 'Name': 'Polonium', 'Electrons': 84, 'Shells': [2, 8, 18, 32, 18, 6]},
    85: {'Symbol': 'At', 'Name': 'Astatine', 'Electrons': 85, 'Shells': [2, 8, 18, 32, 18, 7]},
    86: {'Symbol': 'Rn', 'Name': 'Radon', 'Electrons': 86, 'Shells': [2, 8, 18, 32, 18, 8]},
    87: {'Symbol': 'Fr', 'Name': 'Francium', 'Electrons': 87, 'Shells': [2, 8, 18, 32, 18, 8, 1]},
    88: {'Symbol': 'Ra', 'Name': 'Radium', 'Electrons': 88, 'Shells': [2, 8, 18, 32, 18, 8, 2]},
    89: {'Symbol': 'Ac', 'Name': 'Actinium', 'Electrons': 89, 'Shells': [2, 8, 18, 32, 18, 9, 2]},
    90: {'Symbol': 'Th', 'Name': 'Thorium', 'Electrons': 90, 'Shells': [2, 8, 18, 32, 18, 10, 2]},
    91: {'Symbol': 'Pa', 'Name': 'Protactinium', 'Electrons': 91, 'Shells': [2, 8, 18, 32, 20, 9, 2]},
    92: {'Symbol': 'U', 'Name': 'Uranium', 'Electrons': 92, 'Shells': [2, 8, 18, 32, 21, 9, 2]},
    93: {'Symbol': 'Np', 'Name': 'Neptunium', 'Electrons': 93, 'Shells': [2, 8, 18, 32, 22, 9, 2]},
    94: {'Symbol': 'Pu', 'Name': 'Plutonium', 'Electrons': 94, 'Shells': [2, 8, 18, 32, 24, 8, 2]},
    95: {'Symbol': 'Am', 'Name': 'Americium', 'Electrons': 95, 'Shells': [2, 8, 18, 32, 25, 8, 2]},
    96: {'Symbol': 'Cm', 'Name': 'Curium', 'Electrons': 96, 'Shells': [2, 8, 18, 32, 25, 9, 2]},
    # ...
    97: {'Symbol': 'Bk', 'Name': 'Berkelium', 'Electrons': 97, 'Shells': [2, 8, 18, 32, 27, 8, 2]},
    98: {'Symbol': 'Cf', 'Name': 'Californium', 'Electrons': 98, 'Shells': [2, 8, 18, 32, 28, 8, 2]},
    99: {'Symbol': 'Es', 'Name': 'Einsteinium', 'Electrons': 99, 'Shells': [2, 8, 18, 32, 29, 8, 2]},
    100: {'Symbol': 'Fm', 'Name': 'Fermium', 'Electrons': 100, 'Shells': [2, 8, 18, 32, 30, 8, 2]},
    101: {'Symbol': 'Md', 'Name': 'Mendelevium', 'Electrons': 101, 'Shells': [2, 8, 18, 32, 31, 8, 2]},
    102: {'Symbol': 'No', 'Name': 'Nobelium', 'Electrons': 102, 'Shells': [2, 8, 18, 32, 32, 8, 2]},
    103: {'Symbol': 'Lr', 'Name': 'Lawrencium', 'Electrons': 103, 'Shells': [2, 8, 18, 32, 32, 8, 3]},
    104: {'Symbol': 'Rf', 'Name': 'Rutherfordium', 'Electrons': 104, 'Shells': [2, 8, 18, 32, 32, 10, 2]},
    105: {'Symbol': 'Db', 'Name': 'Dubnium', 'Electrons': 105, 'Shells': [2, 8, 18, 32, 32, 11, 2]},
    106: {'Symbol': 'Sg', 'Name': 'Seaborgium', 'Electrons': 106, 'Shells': [2, 8, 18, 32, 32, 12, 2]},
    107: {'Symbol': 'Bh', 'Name': 'Bohrium', 'Electrons': 107, 'Shells': [2, 8, 18, 32, 32, 13, 2]},
    108: {'Symbol': 'Hs', 'Name': 'Hassium', 'Electrons': 108, 'Shells': [2, 8, 18, 32, 32, 14, 2]},
    109: {'Symbol': 'Mt', 'Name': 'Meitnerium', 'Electrons': 109, 'Shells': [2, 8, 18, 32, 32, 15, 2]},
    110: {'Symbol': 'Ds', 'Name': 'Darmstadtium', 'Electrons': 110, 'Shells': [2, 8, 18, 32, 32, 16, 2]},
    111: {'Symbol': 'Rg', 'Name': 'Roentgenium', 'Electrons': 111, 'Shells': [2, 8, 18, 32, 32, 17, 2]},
    112: {'Symbol': 'Cn', 'Name': 'Copernicium', 'Electrons': 112, 'Shells': [2, 8, 18, 32, 32, 18, 2]},
    113: {'Symbol': 'Nh', 'Name': 'Nihonium', 'Electrons': 113, 'Shells': [2, 8, 18, 32, 32, 18, 3]},
    114: {'Symbol': 'Fl', 'Name': 'Flerovium', 'Electrons': 114, 'Shells': [2, 8, 18, 32, 32, 18, 4]},
    115: {'Symbol': 'Mc', 'Name': 'Moscovium', 'Electrons': 115, 'Shells': [2, 8, 18, 32, 32, 18, 5]},
    116: {'Symbol': 'Lv', 'Name': 'Livermorium', 'Electrons': 116, 'Shells': [2, 8, 18, 32, 32, 18, 6]},
    117: {'Symbol': 'Ts', 'Name': 'Tennessine', 'Electrons': 117, 'Shells': [2, 8, 18, 32, 32, 18, 7]},
    118: {'Symbol': 'Og', 'Name': 'Oganesson', 'Electrons': 118, 'Shells': [2, 8, 18, 32, 32, 18, 8]},
# ... Continue for all 118 elements
    # ... Theory
    119: {'Symbol': 'Α', 'Name': 'Alphaon', 'Electrons': 119, 'Shells': [2, 8, 18, 32, 32, 18, 9], 'Type': 'Theoretical'},
    120: {'Symbol': 'Β', 'Name': 'Betaon', 'Electrons': 120, 'Shells': [2, 8, 18, 32, 32, 18, 10], 'Type': 'Theoretical'},
    121: {'Symbol': 'Γ', 'Name': 'Gammaon', 'Electrons': 121, 'Shells': [2, 8, 18, 32, 32, 18, 11], 'Type': 'Theoretical'},
    122: {'Symbol': 'Δ', 'Name': 'Deltaon', 'Electrons': 122, 'Shells': [2, 8, 18, 32, 32, 18, 12], 'Type': 'Theoretical'},
    123: {'Symbol': 'Ε', 'Name': 'Epsilonon', 'Electrons': 123, 'Shells': [2, 8, 18, 32, 32, 18, 13], 'Type': 'Theoretical'},
    124: {'Symbol': 'Ζ', 'Name': 'Zetaon', 'Electrons': 124, 'Shells': [2, 8, 18, 32, 32, 18, 14], 'Type': 'Theoretical'},
    125: {'Symbol': 'Η', 'Name': 'Etaon', 'Electrons': 125, 'Shells': [2, 8, 18, 32, 32, 18, 15], 'Type': 'Theoretical'},
    126: {'Symbol': 'Θ', 'Name': 'Thetaon', 'Electrons': 126, 'Shells': [2, 8, 18, 32, 32, 18, 16], 'Type': 'Theoretical'},
    127: {'Symbol': 'Ι', 'Name': 'Iotaon', 'Electrons': 127, 'Shells': [2, 8, 18, 32, 32, 18, 17], 'Type': 'Theoretical'},
    128: {'Symbol': 'Κ', 'Name': 'Kappaon', 'Electrons': 128, 'Shells': [2, 8, 18, 32, 32, 18, 18], 'Type': 'Theoretical'}
    # ...

}

theoretical_elements = {
    256: {'Symbol': 'Alpha', 'Name': 'Theoretical-Alpha', 'Electrons': 256, 'Shells': [2, 8, 18, 32, 50, 72, 98, 128, 162, 196, 230, 256]},
    512: {'Symbol': 'Beta', 'Name': 'Theoretical-Beta', 'Electrons': 512, 'Shells': [2, 8, 18, 32, 50, 72, 98, 128, 162, 196, 230, 256, 288, 320, 352, 384, 416, 448, 480, 512]},
    1024: {'Symbol': 'Gamma', 'Name': 'Theoretical-Gamma', 'Electrons': 1024, 'Shells': [2, 8, 18, 32, 50, 72, 98, 128, 162, 196, 230, 256, 288, 320, 352, 384, 416, 448, 480, 512, 544, 576, 608, 640, 672, 704, 736, 768, 800, 832, 864, 896, 928, 960, 992, 1024]}
}

# Initialize the extended periodic table as an empty list
extended_periodic_table = []

# Function to dynamically add elements to the extended periodic table
def add_elements_from_dict(elements_dict):
    for atomic_number, element_data in elements_dict.items():
        n = element_data['Electrons']  # Number of electrons
        l = len(element_data['Shells'])  # Number of shells
        ml = None  # Placeholder for electromagnetic spectrum (this would need to be defined)
        ms = None  # Placeholder for spin (this would need to be defined)
        q = None  # Placeholder for additional quantum number
        vq = None  # Placeholder for time of the observer
        
        element = {
            'Atomic Number': atomic_number,
            'Symbol': element_data['Symbol'],
            'Name': element_data['Name'],
            'Electrons': element_data['Electrons'],
            'Shells': element_data['Shells'],
            'Quantum Numbers': {
                'n': n,
                'l': l,
                'ml': ml,
                'ms': ms,
                'q': q,
                'v(q)': vq
            }
        }
        extended_periodic_table.append(element)

add_elements_from_dict(elements_dict)

elements_description_type = {
    1: {'Description': 'Lightest element, forms water when combined with oxygen', 'Type': 'Stable'},
    2: {'Description': 'Noble gas, does not readily form compounds', 'Type': 'Stable'},
    3: {'Description': 'Alkali metal, reacts with water', 'Type': 'Stable'},
    4: {'Description': 'Alkaline earth metal, used in aerospace materials', 'Type': 'Stable'},
    5: {'Description': 'Metalloid, used in making strong, lightweight alloys', 'Type': 'Stable'},
    6: {'Description': 'Non-metal, basis of organic chemistry', 'Type': 'Stable'},
    7: {'Description': 'Non-metal, makes up about 78% of Earth\'s atmosphere', 'Type': 'Stable'},
    8: {'Description': 'Non-metal, essential for respiration', 'Type': 'Stable'},
    9: {'Description': 'Halogen, most electronegative element', 'Type': 'Stable'},
    10: {'Description': 'Noble gas, used in neon signs', 'Type': 'Stable'},
    # ... Continue for other elements
    43: {'Description': 'First radioactive element discovered', 'Type': 'Unstable'},
    61: {'Description': 'Does not have stable isotopes', 'Type': 'Unstable'},
    93: {'Description': 'First transuranic element', 'Type': 'Synthetic'},
    94: {'Description': 'Used in nuclear reactors', 'Type': 'Synthetic'},
    118: {'Description': 'Superheavy, noble gas', 'Type': 'Synthetic'},
    # ... Continue for other elements
}

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', elements=extended_periodic_table)

@app.route('/element/<int:atomic_number>')
def element(atomic_number):
    element = next((e for e in extended_periodic_table if e['Atomic Number'] == atomic_number), None)
    return render_template('element.html', element=element)

if __name__ == '__main__':
    app.run(debug=True)

