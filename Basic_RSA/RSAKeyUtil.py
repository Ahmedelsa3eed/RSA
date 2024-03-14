def read_key(key):
    """Returns (n, e) for public key or (n, d) for private key"""
    try:
        file = open("./" + key, 'r')
    except FileNotFoundError:
        print("[Error] key not found")
        exit(1)
    n = int(file.readline())
    exponent = int(file.readline())
    return n, exponent

def write_key(key, n, exponent):
    """Writes the public or private key to a file
        separate the n and exponent with a newline character"""
    with open("./" + key, "w") as file:
        file.write(f"{n}\n{exponent}")

def string_to_int(s: str):
    return int.from_bytes(s.encode('utf-8'), byteorder='big')

def int_to_string(num: int):
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode()

def write_message(message: str, filename):
    """Write the text message to a file as a string"""
    with open("./" + filename, 'w') as file:
        file.write(message)

def read_message(filename) -> str:
    """Read the plaintext string from a file"""
    with open("./" + filename, 'r') as file:
        text = file.read()

    return text

def write_primes(p, q):
    """Write the primes p and q to a file to be used later for decryption"""
    with open("./" + "primes", "w") as file:
        file.write(f"{p}\n{q}")

def read_primes():
    """Read the primes p and q from a file"""
    try:
        file = open("./" + "primes", 'r')
        p = int(file.readline())
        q = int(file.readline())
        return p, q
    except FileNotFoundError:
        print("[Error] primes not found")
        exit(1)