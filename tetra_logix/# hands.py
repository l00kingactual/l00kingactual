import decimal

# Set precision for decimal module
decimal.getcontext().prec = 5000

# Define the number of values each bit cell can represent
values_2bit = 4
values_5bit = 32
values_8bit = 256
values_10bit = 1024
values_12bit = 4096

# Define the number of cells in each dimension of the cube
cube_size = 13

# Calculate the total number of cells in the cube
total_cells = cube_size ** 3

# Calculate the total number of combinations for the first cube
total_combinations_cube1 = decimal.Decimal(values_2bit * values_5bit * values_8bit * values_10bit * values_12bit) ** total_cells

# Calculate the total number of combinations for the second cube (squared)
total_combinations_cube2 = total_combinations_cube1 ** 2

# Calculate the total number of combinations for the third cube (cubed)
total_combinations_cube3 = total_combinations_cube1 ** 3

# Calculate the total number of combinations for the fourth cube (to the power of 4)
total_combinations_cube4 = total_combinations_cube1 ** 4

# Print the results
print("Total combinations for the first cube:", total_combinations_cube1)
print("Total combinations for the second cube (squared):", total_combinations_cube2)
print("Total combinations for the third cube (cubed):", total_combinations_cube3)
print("Total combinations for the fourth cube (to the power of 4):", total_combinations_cube4)
