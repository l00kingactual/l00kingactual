def factorial(n):
    """Function to compute the factorial of a number using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function invocation
result = factorial(5)
print(result)  # Output: 120
