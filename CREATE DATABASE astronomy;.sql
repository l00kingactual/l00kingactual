CREATE DATABASE astronomy;
USE astronomy;

CREATE TABLE planets (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  description TEXT,
  image_url VARCHAR(255),
  vrml_url VARCHAR(255)
);

CREATE TABLE constellations (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  description TEXT,
  image_url VARCHAR(255),
  vrml_url VARCHAR(255)
);

CREATE TABLE messier_objects (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  description TEXT,
  image_url VARCHAR(255),
  vrml_url VARCHAR(255)
);

-- Moons Table
CREATE TABLE moons (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  description TEXT,
  image_url VARCHAR(255),
  vrml_url VARCHAR(255)
);

-- Asteroids Table
CREATE TABLE asteroids (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  description TEXT,
  image_url VARCHAR(255),
  vrml_url VARCHAR(255)
);

-- Comets Table
CREATE TABLE comets (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  description TEXT,
  image_url VARCHAR(255),
  vrml_url VARCHAR(255)
);

ALTER TABLE planets ADD COLUMN wikipedia_url VARCHAR(255);
ALTER TABLE moons ADD COLUMN wikipedia_url VARCHAR(255);
ALTER TABLE asteroids ADD COLUMN wikipedia_url VARCHAR(255);
ALTER TABLE comets ADD COLUMN wikipedia_url VARCHAR(255);
ALTER TABLE constellations ADD COLUMN wikipedia_url VARCHAR(255);
ALTER TABLE messier_objects ADD COLUMN wikipedia_url VARCHAR(255);


ALTER TABLE planets ADD COLUMN x_coordinate FLOAT;
ALTER TABLE planets ADD COLUMN y_coordinate FLOAT;
ALTER TABLE planets ADD COLUMN z_coordinate FLOAT;
ALTER TABLE planets ADD COLUMN radius FLOAT;
ALTER TABLE planets ADD COLUMN orbital_radius FLOAT;
ALTER TABLE planets ADD COLUMN orbital_speed FLOAT;
ALTER TABLE planets ADD COLUMN inclination FLOAT;
ALTER TABLE planets ADD COLUMN composition TEXT;
ALTER TABLE planets ADD COLUMN density FLOAT;
ALTER TABLE planets ADD COLUMN color VARCHAR(7);
ALTER TABLE planets ADD COLUMN data JSON;


-- Create the Elements table
CREATE TABLE Elements (
    AtomicNumber INT PRIMARY KEY,
    Symbol VARCHAR(10) NOT NULL
);

-- Create the QuantumNumbers table
CREATE TABLE QuantumNumbers (
    AtomicNumber INT,
    Type VARCHAR(10),
    Value FLOAT,
    FOREIGN KEY (AtomicNumber) REFERENCES Elements(AtomicNumber)
);


-- Insert into Elements table
INSERT INTO Elements (AtomicNumber, Symbol) VALUES (1, 'H');

-- Insert into QuantumNumbers table
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'n', 1);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'l', 0);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'ml', 0);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'ms', 0.5);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'q', 0);



-- Insert into Elements table
INSERT INTO Elements (AtomicNumber, Symbol) VALUES (1, 'H');
INSERT INTO Elements (AtomicNumber, Symbol) VALUES (2, 'He');
-- ... Continue up to 118

-- Insert into QuantumNumbers table for Hydrogen (H)
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'n', 1);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'l', 0);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'ml', 0);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'ms', 0.5);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (1, 'q', 0);

-- Insert into QuantumNumbers table for Helium (He)
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (2, 'n', 1);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (2, 'l', 0);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (2, 'ml', 0);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (2, 'ms', -0.5);
INSERT INTO QuantumNumbers (AtomicNumber, Type, Value) VALUES (2, 'q', 0);

-- ... Continue for each element up to 118
elements_dict = {
    1: 'H',
    2: 'He',
    3: 'Li',
    4: 'Be',
    5: 'B',
    6: 'C',
    7: 'N',
    8: 'O',
    9: 'F',
    10: 'Ne',
    11: 'Na',
    12: 'Mg',
    13: 'Al',
    14: 'Si',
    15: 'P',
    16: 'S',
    17: 'Cl',
    18: 'Ar',
    19: 'K',
    20: 'Ca',
    21: 'Sc',
    22: 'Ti',
    23: 'V',
    24: 'Cr',
    25: 'Mn',
    26: 'Fe',
    27: 'Co',
    28: 'Ni',
    29: 'Cu',
    30: 'Zn',
    31: 'Ga',
    32: 'Ge',
    33: 'As',
    34: 'Se',
    35: 'Br',
    36: 'Kr',
    37: 'Rb',
    38: 'Sr',
    39: 'Y',
    40: 'Zr',
    41: 'Nb',
    42: 'Mo',
    43: 'Tc',
    44: 'Ru',
    45: 'Rh',
    46: 'Pd',
    47: 'Ag',
    48: 'Cd',
    49: 'In',
    50: 'Sn',
    51: 'Sb',
    52: 'Te',
    53: 'I',
    54: 'Xe',
    55: 'Cs',
    56: 'Ba',
    57: 'La',
    58: 'Ce',
    59: 'Pr',
    60: 'Nd',
    61: 'Pm',
    62: 'Sm',
    63: 'Eu',
    64: 'Gd',
    65: 'Tb',
    66: 'Dy',
    67: 'Ho',
    68: 'Er',
    69: 'Tm',
    70: 'Yb',
    71: 'Lu',
    72: 'Hf',
    73: 'Ta',
    74: 'W',
    75: 'Re',
    76: 'Os',
    77: 'Ir',
    78: 'Pt',
    79: 'Au',
    80: 'Hg',
    81: 'Tl',
    82: 'Pb',
    83: 'Bi',
    84: 'Po',
    85: 'At',
    86: 'Rn',
    87: 'Fr',
    88: 'Ra',
    89: 'Ac',
    90: 'Th',
    91: 'Pa',
    92: 'U',
    93: 'Np',
    94: 'Pu',
    95: 'Am',
    96: 'Cm',
    97: 'Bk',
    98: 'Cf',
    99: 'Es',
    100: 'Fm',
    101: 'Md',
    102: 'No',
    103: 'Lr',
    104: 'Rf',
    105: 'Db',
    106: 'Sg',
    107: 'Bh',
    108: 'Hs',
    109: 'Mt',
    110: 'Ds',
    111: 'Rg',
    112: 'Cn',
    113: 'Nh',
    114: 'Fl',
    115: 'Mc',
    116: 'Lv',
    117: 'Ts',
    118: 'Og'
}


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
    63: {'Symbol': 'Eu', 'Name': 'Europium', 'Electrons': 63, 'Shells': [2, 8, 18, 25, 8, 2]}
    64: {'Symbol': 'Gd', 'Name': 'Gadolinium', 'Electrons': 64, 'Shells': [2, 8, 18, 25, 9, 2]}
    

# ... Continue for all 118 elements
}
