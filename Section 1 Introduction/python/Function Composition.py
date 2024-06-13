def double(x):
    return x * 2

def square(x):
    return x * x

# Function composition
def double_then_square(x):
    return square(double(x))

# Function invocation
result = double_then_square(3)
print(result)  # Output: 36
