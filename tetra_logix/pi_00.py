from decimal import Decimal, getcontext, MAX_PREC

# Define the scales array
scales = [
    0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
]

from decimal import Decimal, getcontext, MAX_PREC

def calculate_pi_precision(scales):
    pi_values = []
    for precision in scales:
        if precision < 1:
            actual_precision = 1
        elif precision > MAX_PREC:
            print(f"Precision of {precision} exceeds MAX_PREC ({MAX_PREC}). Using MAX_PREC instead.")
            actual_precision = MAX_PREC
        else:
            actual_precision = precision
            
        getcontext().prec = actual_precision
        pi = sum(1/Decimal(16)**k * 
                 (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)) 
                 for k in range(actual_precision))
        pi_values.append((actual_precision, pi))
    
    return pi_values

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

# Calculate pi with varying precision based on scales
pi_precisions = calculate_pi_precision(scales)

# Translate precision into lowercase roman numerals and print
for precision, pi in pi_precisions:
    roman_precision = int_to_roman(precision).lower()
    print(f"Precision: {roman_precision} digits, Pi: {pi}")

