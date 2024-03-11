import os

cwd = os.getcwd()

def read_key(key):
    """Returns (n, e) for public key or (n, d) for private key"""
    try:
        file = open(cwd + f'/{key}', 'r')
    except FileNotFoundError:
        print("[Error] key not found")
        exit(1)
    n = int(file.readline())
    exponent = int(file.readline())
    return n, exponent

def write_key(key, n, exponent):
    """Writes the public or private key to a file
        separate the n and exponent with a newline character"""
    with open(cwd + f"/{key}", "w") as file:
        file.write(f"{n}\n{exponent}")

def read_message(filename):
    """Read the plaintext/ciphertext from a file and return it as an integer"""
    try:
        file = open(cwd + f"/{filename}", 'r')
        message = int(file.readline())
        return message
    except FileNotFoundError:
        print("[Error] message not found")
        exit(1)

def write_message(message, filename):
    """Write the plaintext/ciphertext to a file as a string"""
    with open(cwd + f"/{filename}", "w") as file:
        file.write(str(message))

def write_primes(p, q):
    """Write the primes p and q to a file to be used later for decryption"""
    with open(cwd + "/primes", "w") as file:
        file.write(f"{p}\n{q}")

def read_primes():
    """Read the primes p and q from a file"""
    try:
        file = open(cwd + "/primes", 'r')
        p = int(file.readline())
        q = int(file.readline())
        return p, q
    except FileNotFoundError:
        print("[Error] primes not found")
        exit(1)