from decimal import Decimal, getcontext

def find_first_zero_in_pi(precision=5000):
    getcontext().prec = precision  # Setting the precision to calculate pi
    pi = sum(1/Decimal(16)**k *
             (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6))
             for k in range(precision))  # Calculate pi
    pi_str = str(pi)[2:]  # Convert pi to string and skip the "3."
    first_zero_index = pi_str.find('0')  # Find the index of first '0'
    return first_zero_index + 1  # Add 1 to adjust for the index starting at 0

# Example usage
precision = 5000  # You can adjust the precision as needed
first_zero_position = find_first_zero_in_pi(precision)
print(f"The first '0' in the decimal places of pi occurs at position: {first_zero_position}")
