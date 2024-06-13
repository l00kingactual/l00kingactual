# Create a dictionary to represent the table
unit_conversions = {
    'Meter': {
        'Meters': 1,
        'Light-years': 1.06E-16,
        'Megaparsec': 3.24E-23,
        'Planck Reference Scale (meters)': 6.19E+34,
        'Seconds': 3.34E-09,
        'Minutes': 5.56E-11,
        'Hours': 9.27E-13,
        'Days': 3.86E-14,
        'Months': 1.27E-15,
        'Years': 1.06E-16
    },
    'Kilometer': {
        'Meters': 1.00E+03,
        'Light-years': 1.06E-13,
        'Megaparsec': 3.24E-20,
        'Planck Reference Scale (meters)': 6.19E+37,
        'Seconds': 3.34E-06,
        'Minutes': 5.56E-08,
        'Hours': 9.27E-10,
        'Days': 3.86E-11,
        'Months': 1.27E-12,
        'Years': 1.06E-13
    },
    'Astronomical Unit (AU)': {
        'Meters': 1.50E+11,
        'Light-years': 1.58E-05,
        'Megaparsec': 4.85E-12,
        'Planck Reference Scale (meters)': 9.26E+45,
        'Seconds': 4.99E+02,
        'Minutes': 8.32E+00,
        'Hours': 1.39E-01,
        'Days': 5.78E-03,
        'Months': 1.90E-04,
        'Years': 1.58E-05
    },
    'Light-year': {
        'Meters': 9.46E+15,
        'Light-years': 1,
        'Megaparsec': 3.07E-07,
        'Planck Reference Scale (meters)': 5.85E+50,
        'Seconds': 3.16E+07,
        'Minutes': 5.26E+05,
        'Hours': 8.77E+03,
        'Days': 3.65E+02,
        'Months': 1.20E+01,
        'Years': 1
    },
    'Parsec': {
        'Meters': 3.09E+16,
        'Light-years': 3.262,
        'Megaparsec': 1.00E-06,
        'Planck Reference Scale (meters)': 1.91E+51,
        'Seconds': 1.03E+08,
        'Minutes': 1.72E+06,
        'Hours': 2.86E+04,
        'Days': 1.19E+03,
        'Months': 3.91E+01,
        'Years': 3.262
    },
    'Kiloparsec': {
        'Meters': 3.09E+19,
        'Light-years': 3.26E+03,
        'Megaparsec': 1.00E-03,
        'Planck Reference Scale (meters)': 1.91E+54,
        'Seconds': 1.03E+11,
        'Minutes': 1.72E+09,
        'Hours': 2.86E+07,
        'Days': 1.19E+06,
        'Months': 3.91E+04,
        'Years': 3.26E+03
    },
    'Megaparsec': {
        'Meters': 3.09E+22,
        'Light-years': 3.27E+06,
        'Megaparsec': 1.001,
        'Planck Reference Scale (meters)': 1.91E+57,
        'Seconds': 1.03E+14,
        'Minutes': 1.72E+12,
        'Hours': 2.86E+10,
        'Days': 1.19E+09,
        'Months': 3.92E+07,
        'Years': 3.27E+06
    },
    '10^60 meters': {
        'Meters': 3.09E+60,
        'Light-years': 3.27E+44,
        'Megaparsec': 1.00E+38,
        'Planck Reference Scale (meters)': 6.19E+94,
        'Seconds': 1.03E+52,
        'Minutes': 1.72E+50,
        'Hours': 2.86E+48,
        'Days': 1.19E+47,
        'Months': 3.92E+45,
        'Years': 3.27E+44
    }
}

# Example usage:
print(unit_conversions['Meter']['Light-years'])  # Accessing a specific value
