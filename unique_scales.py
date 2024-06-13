def unique_scales(scales):
    unique = sorted(set(scales))
    return unique

scales = [
    0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 171, 206, 345, 360,
    0, 1, 2, 3, 4, 5, 8, 10, 11, 12, 13, 15, 16, 19, 22, 25,
    28, 31, 32, 33, 34, 35, 37, 45, 50, 51, 54, 57, 60, 64,
    94, 171, 206, 345, 360, 720, 1080
]

# This function call would return the unique, sorted list of scales.
unique_scales_list = unique_scales(scales)
