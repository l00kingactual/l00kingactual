import random
import math

def gcd(a, b):
    """Calculate the greatest common divisor of a and b"""
    while b:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    """Calculate the modular multiplicative inverse of a mod m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def is_prime(n):
    """Determine if a number is prime"""
    if n in [2, 3]:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_keypair(p, q):
    """Generate a public and private key pair for the RSA algorithm"""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Euclidean algorithm to generate the private key
    d = mod_inv(e, phi)

    # Public key pair is (e, n) and private key pair is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    """Encrypt the plaintext message using the public key"""
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    """Decrypt the ciphertext message using the private key"""
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

if __name__ == '__main__':
    p = 61
    q = 53
    public, private = generate_keypair(p, q)
    print("Public key: ", public)
    print("Private key: ", private)
    message = "The quick brown fox jumps over the lazy dog"
    encrypted_msg = encrypt(public, message)
    print("Encrypted message: " + str(encrypted_msg))
    print("Decrypted message: " + decrypt(private, encrypted_msg))

