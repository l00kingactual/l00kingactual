def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(count):
    """Generate a list of the first 'count' prime numbers."""
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Example usage: Get the first 10 prime numbers
num_primes = 10
prime_numbers = generate_primes(num_primes)
print(f"The first {num_primes} prime numbers are: {prime_numbers}")
