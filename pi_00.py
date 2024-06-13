# lines from 3 to 371
'''
The selected code is part of a function that is used to open a file dialog box and allow the user to select a directory. The function starts by importing the necessary modules: `os` for operating system-related tasks, `tkinter` for creating the GUI, and `filedialog` for creating the file dialog box.

The function then defines a nested function, `create_animations`, which is used to create the animations. This function takes four arguments: `input_dirs`, `output_dir`, `fps`, and `duration`.

The function then defines a list, `image_files`, which contains the names of all the files in the input directory that have a supported image format (`.png`, `.jpg`, or `.bmp`). The files are sorted based on their names, and the function loops through each file in the list.

The function then reads in the image using the `imageio` module, and appends it to the `images` list. Once all the images have been read in, the function creates a GIF using the `imageio` module and saves it to the output directory. It also creates an MP4 using the `imageio` module and saves it to the output directory.

The function then creates a GUI using the `tkinter` module. The GUI has three main components: a listbox for selecting input directories, an entry box for selecting the output directory, and an entry box for specifying the FPS.

The function then defines a function, `add_input_dir`, which is used to add a directory to the listbox. This function uses the `filedialog` module to open a file dialog box and allow the user to select a directory.

The function then defines a function, `browse_output_dir`, which is used to open a file dialog box and allow the user to select a directory. This function uses the `filedialog` module to open a file dialog box and allow the user to select a directory.

The function then defines a function, `generate_animations`, which is used to generate the animations. This function uses the `create_animations` function to create the animations using the selected input directories, output directory, and FPS.

The function then creates a main window with a title, `Animated GIF and MP4 Creator`. It then adds three labels, `Input Directories:`, `Output Directory:`, and `Frames Per Second (FPS):`, and three entry boxes for inputting the input directories, output directory, and FPS, respectively.

It then adds two buttons: `Add Directory` and `Browse`. The `Add Directory` button is used to add a directory to the listbox, while the `Browse` button is used to open a file dialog box and allow the user to select an output directory.

The function then adds a `Generate Animations` button, which is used to generate the animations using the selected input directories, output directory, and FPS.

Finally, the function starts the main loop of the GUI, which allows the user to interact with the GUI and generate the animations.

The provided script pi_00.py includes a variety of Python constructs such as variables, constants, functions, dictionaries, and imports from libraries. Here is a detailed breakdown of its key components:

Variables
Numerical Variables: Variables like r, d, mm, cm, meter, km, mega_km, giga_km, terra_km, milli_sec, arc_sec, and milli_seconds are defined with various numeric and string values, representing measurements and numeric representations in different systems.
Rune0Zero: A long string that seems to represent numerals in various languages and scripts.
Dictionaries
my_pi: A dictionary containing various representations of π (pi):
asgard_nums_pi: A string representing a unique format of pi.
chinese_nums_base_pi: A list of strings representing pi in a Chinese-based system.
pi_decimal: Pi to many decimal places.
pi_mixed_numerals: A list of dictionaries, each containing a numerator and denominator, representing fractions.
pi_roman_numerals: A string representing pi in Roman numerals.
pi_words: A list representing zero in various languages.
em_spectrum: A dictionary containing information about different types of electromagnetic waves, such as radio waves, microwaves, and X-rays, with their wavelength and frequency ranges.
Constants
A list named constants contains tuples defining various physical constants with their names, values, and descriptions.
Electromagnetic wave wavelengths such as gamma_ray_wavelength, x_ray_wavelength, ultraviolet_a_wavelength, etc., are defined as constants.
Functions
describe_electromagnetic_wave(wavelength): A function that returns descriptions of various types of electromagnetic waves based on the input wavelength.
Several functions for calculating geometric properties: calculate_area(square_side_length), calculate_volume(cube_side_length), calculate_area_circle(radius), and calculate_volume_sphere(radius).
Symbolic Mathematics using SymPy
The script imports the sympy library for symbolic mathematics.
Defines symbolic variables x, y, z and performs various symbolic operations like differentiation, integration, and substitution on expressions.
Demonstrates the creation of a symbolic dictionary and a list to store symbolic variables.
Import Statements
Imports mathematical libraries like math, numpy, and sympy.
Import statement for pandas, suggesting the script might be handling data, particularly from Excel files.
DataFrames and Excel Handling
Reads data from an Excel file (lang_table.xlsx) into a dictionary of DataFrames and concatenates them into a master DataFrame.
Miscellaneous
A section commented as "if name == 'main':" suggests that the script has a main execution block, but it's commented out.
The script contains several print statements to display outputs, particularly for the electromagnetic spectrum data and dictionary values from my_pi.
Overall Impression
The script appears to be a multifaceted demonstration of Python's capabilities in handling numeric data, symbolic mathematics, data manipulation (particularly with pandas), and defining and using functions. It includes explorations of mathematical concepts like pi, constants, and wavelengths, as well as handling and displaying multilingual data.

'''

# asgard_nums_pi = '1.3.341 7B99 1C11 8C97 1147 1A8B 73AA 13AC 78B 513 5'

r = 1.1
d = 3.14
mm = '1.3.314'
cm = '1.3.3410'
meter = '1.5'
km = '1.6'
mega_km = '1.01'
giga_km = '2.01'
terra_km = '3.01'

milli_sec = '1000'
arc_sec = '1000'
milli_seconds = '10000'


Rune0Zero = '零0영零DimN/AΜηδένНольصفرशून्यSunyaSıfırᚦ1One一1일一UnIΈναОдинواحدएकSijiBirᚢ2Two二10이二DauIIΔύοДваاثنانदोDhuaİkiᚢᛁ3Three三11삼三TriIIIΤρίαТриثلاثةतीनTigaÜçᚢᛁᚴ4Four四100사四PedwarIVΤέσσεραЧетыреأربعةचारEmpatDörtᚦ5Five五101오五PumpVΠέντεПятьخمسةपांचLimaBeşᚢᚴ6Six六110육六ChwechVIΈξιШестьستةछहEnamAltıᚢᚴᛁ7Seven七111칠七SaithVIIΕπτάСемьسبعةसातTujuhYediᚢᚴᛁᚴ8Eight八1000팔八WythVIIIΟκτώВосемьثمانيةआठDelapanSekizᚢᚴᛁᚴᛁ9Nine九1001구九NawIXΕννέαДевятьتسعةनौSembilanDokuzᚢᚴᛁᚴᛁᚱ10Ten十1010십十DegXΔέκαДесятьعشرةदसSepuluhOnᚢᚴᛁᚴᛁᚱᛁ'

my_pi = {
    "asgard_nums_pi": '1.3.341 7B99 1C11 8C97 1147 1A8B 73AA 13AC 78B 513 5',
    "chinese_nums_base_pi": ['ǎo', 'à', 'ǎn', 'é', 'ù' 'ī'],
    "pi_decimal": 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679,
    "pi_mixed_numerals": [
        {"numerator": 3, "denominator": 8},
        {"numerator": 3, "denominator": 7},
        {"numerator": 3, "denominator": 12},
        {"numerator": 3, "denominator": 60},
        {"numerator": 3, "denominator": 360},
    ],
    "pi_roman_numerals": '3.1.5.7.mx.mc.dm.e.0',
    "pi_words": [
        "零", "0",
        "영", "0",
        "零", "0",
        "Dim", "0",
        "Nulla", "0",
        "Μηδέν", "0",
        "Ноль", "0",
        "صفر", "0",
        "शून्य", "0",
        "Suna", "0",
    ]
}

base_360_pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
print (base_360_pi)





# Constants
constants = [
    ("Plank Time", 5.39e-44, "Plank time constant in seconds"),
    ("Initial Gravity", 9.8, "Initial gravity on Earth's surface in m/s²"),
    ("Speed of Light", 299792458, "Speed of light in meters per second"),
    ("Pi Reference", 3.1415926536, "Fixed value for Pi"),
    ("Parallax Constant", 1.496e11, "Astronomical Unit (AU) in meters"),
    ("Hubble Constant", 70.4, "Hubble constant in km/s/Mpc"),
    ("Red Shift Reference", 0, "Reference redshift value (usually 0 for nearby objects)"),
    ("Density", 1.225, "Air density at standard conditions in kg/m³"),
    ("Refractive Index", 1.0003, "Refractive index of air at standard conditions"),
    ("Wavelength", 633e-9, "Wavelength of red light in meters"),
    ("Frequency", 4.74e14, "Frequency of red light in Hz"),
]
print (constants)



# Define constants for electromagnetic waves
gamma_ray_wavelength = 1e-12  # 1 picometer (pm)
x_ray_wavelength = 1e-10  # 0.1 nanometer (nm)
ultraviolet_a_wavelength = 380e-9  # 380 nanometers (nm)
ultraviolet_b_wavelength = 315e-9  # 315 nanometers (nm)
blue_light_wavelength = 480e-9  # 480 nanometers (nm)
green_light_wavelength = 530e-9  # 530 nanometers (nm)
red_light_wavelength = 700e-9  # 700 nanometers (nm)
near_infrared_wavelength = 1e-6  # 1 micrometer (μm)
mid_infrared_wavelength = 10e-6  # 10 micrometers (μm)
far_infrared_wavelength = 1000e-6  # 1000 micrometers (μm)
microwave_wavelength = 1e-2  # 1 centimeter (cm)
uhf_wavelength = 1e-1  # 10 centimeters (cm)
vlf_wavelength = 1e1  # 10 meters (m)
ultra_long_wave_wavelength = 1e4  # 10,000 kilometers (km)
mega_long_wave_wavelength = 1e5 # 100,000 kilometers (km)

em_spectrum = {
    "Radio Waves": {"Wavelength": "Kilometers to millimeters", "Frequency": "Below 300 GHz"},
    "Microwaves": {"Wavelength": "Millimeters to centimeters", "Frequency": "300 MHz to 300 GHz"},
    "Infrared (IR) Waves": {"Wavelength": "Micrometers (µm) to millimeters", "Frequency": "300 GHz to 400 THz"},
    "Visible Light": {"Wavelength": "About 380 to 750 nm", "Frequency": "400 THz to 790 THz"},
    "Ultraviolet (UV) Waves": {"Wavelength": "About 10 to 380 nm", "Frequency": "790 THz to 30 PHz"},
    "X-Rays": {"Wavelength": "About 0.01 to 10 nm", "Frequency": "30 PHz to 30 EHz"},
    "Gamma Rays": {"Wavelength": "Less than 0.01 nm", "Frequency": "Above 30 EHz"}
}

# Accessing the dictionary values:
print("Radio Waves - Wavelength:", em_spectrum["Radio Waves"]["Wavelength"])
print("Radio Waves - Frequency:", em_spectrum["Radio Waves"]["Frequency"])

# Descriptions
plank_time_description = "Plank time is a fundamental constant in physics and cannot be calculated from other values."
initial_g_description = "The initial gravity on Earth's surface (9.8 m/s²) is a known constant and doesn't need calculation."
speed_of_light_description = "The speed of light in meters per second is a fundamental constant and is approximately 299,792,458 meters per second. It can also be calculated from other fundamental constants: Speed of light (c) = 1 / √(ε₀ * μ₀), where ε₀ (epsilon naught) is the vacuum permittivity (approximately 8.854 x 10^(-12) F/m) and μ₀ (mu naught) is the vacuum permeability (approximately 4π x 10^(-7) T·m/A)."
pi_reference_description = "Pi (π) is a mathematical constant and is a known fixed value approximately equal to 3.1415926536. It doesn't need calculation."
parallax_constant_description = "The Astronomical Unit (AU) is the average distance between the Earth and the Sun, and it is approximately 1.496 x 10^11 meters. It is a defined constant in astronomy."
hubble_constant_description = "The Hubble constant (H₀) represents the current rate of expansion of the Universe and is approximately 70.4 km/s/Mpc. It is determined through observations and measurements of the cosmic microwave background radiation, galaxy redshifts, and other cosmological data."
red_shift_reference_description = "The reference redshift value (usually 0) is often used as a baseline for measuring redshift in astronomy. It represents the absence of cosmological redshift (e.g., for nearby objects). It is set to 0 by convention."

# Print the descriptions
print("Constant Descriptions:")
print(f"Plank Time (plank_time): {plank_time_description}")
print(f"Initial Gravity (initial_g): {initial_g_description}")
print(f"Speed of Light (speed_of_light): {speed_of_light_description}")
print(f"Pi (pi_reference): {pi_reference_description}")
print(f"Astronomical Unit (parallax_constant): {parallax_constant_description}")
print(f"Hubble Constant (hubble_constant): {hubble_constant_description}")
print(f"Redshift Reference (red_shift_reference): {red_shift_reference_description}")



# Function to describe electromagnetic waves
def describe_electromagnetic_wave(wavelength):
    if wavelength < gamma_ray_wavelength:
        return "Gamma Rays: Extremely high-energy electromagnetic waves."
    elif wavelength < x_ray_wavelength:
        return "X-Rays: High-energy electromagnetic waves used in medical imaging."
    elif wavelength < ultraviolet_a_wavelength:
        return "Ultraviolet (UV) Rays: Shorter wavelengths, subdivided into UVA, UVB, and UVC."
    elif wavelength < blue_light_wavelength:
        return "Blue Light: Part of the visible spectrum, with shorter wavelengths."
    elif wavelength < green_light_wavelength:
        return "Green Light: Part of the visible spectrum, responsible for green color."
    elif wavelength < red_light_wavelength:
        return "Red Light: Part of the visible spectrum, with longer wavelengths."
    elif wavelength < near_infrared_wavelength:
        return "Near Infrared: Used in remote controls and thermal imaging."
    elif wavelength < mid_infrared_wavelength:
        return "Mid Infrared: Used in IR spectroscopy and some communication."
    elif wavelength < far_infrared_wavelength:
        return "Far Infrared: Used in astronomy and heat sensing."
    elif wavelength < microwave_wavelength:
        return "Microwaves: Used in microwave ovens and communication."
    elif wavelength < uhf_wavelength:
        return "Ultra High Frequency (UHF): Commonly used in TV broadcasting."
    elif wavelength < vlf_wavelength:
        return "Very Low Frequency (VLF): Used for navigation and military communication."
    elif wavelength < ultra_long_wave_wavelength:
        return "Ultra Long Wave: Extremely long wavelengths used in radio communication."
    else:
        return "Radio Waves: Subdivided into various bands, including AM and FM radio."


import math

def calculate_area(square_side_length):
    try:
        # Calculate the area of a square
        area = square_side_length ** 2
        return area
    except Exception as e:
        print("Error in calculating square area:", e)
        return None

def calculate_volume(cube_side_length):
    try:
        # Calculate the volume of a cube
        volume = cube_side_length ** 3
        return volume
    except Exception as e:
        print("Error in calculating cube volume:", e)
        return None

def calculate_area_circle(radius):
    try:
        # Calculate the area of a circle
        area = math.pi * radius ** 2
        return area
    except Exception as e:
        print("Error in calculating circle area:", e)
        return None

def calculate_volume_sphere(radius):
    try:
        # Calculate the volume of a sphere
        volume = (4/3) * math.pi * radius ** 3
        return volume
    except Exception as e:
        print("Error in calculating sphere volume:", e)
        return None

# Add similar functions for other shapes




'''
if __name__ == "__main__":
    try:
        square_side_length = 10
        cube_side_length = 5
        circle_radius = 3
        sphere_radius = 4

        # Calculate and print the area and volume for various shapes
        square_area = calculate_area(square_side_length)
        cube_volume = calculate_volume(cube_side_length)
        circle_area = calculate_area_circle(circle_radius)
        sphere_volume = calculate_volume_sphere(sphere_radius)

        print("Square Area:", square_area)
        print("Cube Volume:", cube_volume)
        print("Circle Area:", circle_area)
        print("Sphere Volume:", sphere_volume)

        # Add calculations for other shapes here

    except Exception as e:
        print("Main Error:", e)
'''



# Example: Describe an electromagnetic wave with a wavelength of 300 nanometers
#wavelength_to_describe = 300e-9  # 300 nanometers (nm)
#description = describe_electromagnetic_wave(wavelength_to_describe)
#print(description)
# Assuming you have the em_spectrum dictionary defined:

# Accessing the dictionary values:
for category, data in em_spectrum.items():
    print(f"{category} - Wavelength: {data['Wavelength']}")
    print(f"{category} - Frequency: {data['Frequency']}")
    print()  # Print a newline for better readability

# Accessing the values in the dictionary:
#print("Representation of pi in Roman numerals:", my_pi["pi_roman_numerals"])
#print("Representation of pi in Chinese base:", my_pi["chinese_nums_base_pi"])
# Assuming you have the my_pi dictionary defined:

# Accessing the values in the dictionary:
for key, value in my_pi.items():
    print(f"{key}: {value}")

import math

pi_value = math.pi
print("Pi from math module:", pi_value)

import numpy as np

pi_value = np.pi
print("Pi from numpy library:", pi_value)

import sympy as sp

pi_value = sp.pi
print("Pi from sympy library:", pi_value)

import sympy as sp

x, y, z = sp.symbols('x y z')
expr = x**2 + 2*y - sp.sin(z)
simplified_expr = sp.simplify(expr)
solutions = sp.solve(x**2 - 4, x)
derivative = sp.diff(x**2, x)
substituted_expr = expr.subs(x, 2)
sp.pprint(simplified_expr)

# Define a symbolic expression using x, y, and z
expr = x**2 + 2*y - sp.sin(z)

# Perform symbolic operations on the expression
derivative = sp.diff(expr, x)  # Find the derivative with respect to x
integral = sp.integrate(expr, (y, 0, 1))  # Integrate with respect to y from 0 to 1


import sympy as sp

# Define symbolic variables
x, y, z = sp.symbols('x y z')

# Define a symbolic expression
expr = x**2 + 2*y - sp.sin(z)

# Pretty-print the expression
sp.pprint(expr)

import sympy as sp

# Define symbolic variables
x, y, z = sp.symbols('x y z')

# Define a symbolic expression
expr = x**2 + 2*y - sp.sin(z)

# Print the expression
print(expr)

import sympy as sp

# Define symbolic variables for shapes and characters
square = sp.Symbol('Square')
circle = sp.Symbol('Circle')
triangle = sp.Symbol('Triangle')

# Define symbolic variables for numerical values
value1 = sp.Rational(1, 3)
value2 = sp.Rational(2, 5)
value3 = sp.Rational(4, 7)

# Create a symbolic dictionary
symbolic_dict = {
    square: 'Symbol for square',
    circle: 'Symbol for circle',
    triangle: 'Symbol for triangle',
    value1: 'One-third',
    value2: 'Two-fifths',
    value3: 'Four-sevenths',
}

# Access and print values from the symbolic dictionary
print(symbolic_dict[square])  # Output: Symbol for square
print(symbolic_dict[value1])   # Output: One-third

import sympy as sp

# Define symbolic variables using sympy.symbols
x, y, z = sp.symbols('x y z')

# Create a list to store the symbolic variables
symbol_list = [x, y, z]

# Access and print all symbolic variables in the list
for symbol in symbol_list:
    print(symbol)

# You can also add more symbols to the list as needed
additional_symbols = sp.symbols('a b c')
symbol_list.extend(additional_symbols)

# Access and print all symbolic variables again
for symbol in symbol_list:
    print(symbol)

import pandas as pd

# Define the Excel file path
excel_file = 'lang_table.xlsx'

# Read all sheets into a dictionary of DataFrames
sheets_dict = pd.read_excel(excel_file, sheet_name=None)

# Create an empty DataFrame to store the master data
master_df = pd.DataFrame()

# Iterate through each sheet and concatenate data into the master DataFrame
for sheet_name, sheet_df in sheets_dict.items():
    # Store the individual frames for reference
    sheet_df_name = f"{sheet_name}_df"
    globals()[sheet_df_name] = sheet_df
    
    # Concatenate the data into the master DataFrame
    master_df = pd.concat([master_df, sheet_df], ignore_index=True)

# Print the master DataFrame
print("Master DataFrame:")
print(master_df)

# Now, you can work with the master_df for your analysis, and individual frames are available for reference.
# with the master_df created, ouptut the master DataFrame to excelwork \\table_col_row.xlxs and then transform the row/col so it becomes row/col and ouput as \\table_row_col.xlxs
# with the master_df created, ouptut the master DataFrame to excelwork \\table_col_col.xlxs and row_row so we have the cols as ros and cols and the same  for the row idea.




'''
import pandas as pd

# Assuming master_df is your DataFrame

# Convert all values in the DataFrame to strings
master_df = master_df.astype(str)

# Unique Chars
try:
    unique_chars = master_df.drop(columns=['Language']).stack().dropna().unique()
    unique_chars_df = pd.DataFrame({'Unique Value': unique_chars, 'Category': 'Chars'})
except Exception as e:
    unique_chars_df = pd.DataFrame({'Unique Value': [], 'Category': 'Chars', 'Error': str(e)})

# Unique Symbols
try:
    unique_symbols = master_df.drop(columns=['Language']).stack().dropna().unique()
    unique_symbols_df = pd.DataFrame({'Unique Value': unique_symbols, 'Category': 'Symbols'})
except Exception as e:
    unique_symbols_df = pd.DataFrame({'Unique Value': [], 'Category': 'Symbols', 'Error': str(e)})

# Unique Words
try:
    unique_words = master_df.drop(columns=['Language']).stack().dropna().unique()
    unique_words_df = pd.DataFrame({'Unique Value': unique_words, 'Category': 'Words'})
except Exception as e:
    unique_words_df = pd.DataFrame({'Unique Value': [], 'Category': 'Words', 'Error': str(e)})

# Unique Numbers
try:
    unique_numbers = master_df.drop(columns=['Language']).stack().dropna().unique()
    unique_numbers_df = pd.DataFrame({'Unique Value': unique_numbers, 'Category': 'Numbers'})
except Exception as e:
    unique_numbers_df = pd.DataFrame({'Unique Value': [], 'Category': 'Numbers', 'Error': str(e)})

# Unique Letters (Assuming you want unique letters within the words)
try:
    unique_letters_data = []

    # Find all unique characters in the DataFrame
    unique_chars = ''.join(master_df.stack().unique())
    unique_chars = ''.join(filter(str.isalnum, unique_chars))  # Keep alphanumeric characters only

    # Iterate through the sheets and find occurrences of unique characters
    for sheet in master_df.columns[1:]:
        sheet_data = master_df[['Language', sheet]]
        for char in unique_chars:
            if sheet_data.isin([char]).any().any():
                unique_letters_data.append({'Unique Character': char, 'Sheet Reference': sheet})

    # Create a DataFrame from the list of results
    unique_letters_df = pd.DataFrame(unique_letters_data)

    # Reset the index of the final DataFrame
    unique_letters_df.reset_index(drop=True, inplace=True)
except Exception as e:
    unique_letters_df = pd.DataFrame({'Unique Character': [], 'Sheet Reference': [], 'Error': str(e)})

# Display the tables
print("Unique Chars:")
print(unique_chars_df)

print("\nUnique Symbols:")
print(unique_symbols_df)

print("\nUnique Words:")
print(unique_words_df)

print("\nUnique Numbers:")
print(unique_numbers_df)

print("\nUnique Letters:")
print(unique_letters_df)

'''


