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

# Number sequence
scales = [  
    0, 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 15, 16, 19, 22, 24, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 128, 171, 196, 206, 345, 360, 512, 720, 845, 1080, 4096, 4394, 5239, 5261
]

# Translate scales into lowercase roman numerals
roman_numerals = [int_to_roman(num) for num in scales]

for num, roman in zip(scales, roman_numerals):
    print(f"{num}: {roman}")
