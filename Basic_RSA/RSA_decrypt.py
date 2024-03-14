from FindMI import MI
from RSAKeyUtil import *
import time
import sys

def decrypt(c, d, n, p, q) -> int:
    """Decrypt the ciphertext using the private key and the primes
    Args:
        c: the ciphertext to decrypt
        d: the private decryption key
        n: the modulus used for encryption/decryption
        p: one of the prime factors of the modulus
        q: one of the prime factors of the modulus
    Returns:
        m: the decrypted message
    """
    # Using the Chinese Remainder Theorem to speed up the calculation
    V_p = pow(c, d, p)
    V_q = pow(c, d, q)

    X_p = q * MI(q, p)
    X_q = p * MI(p, q)

    m = (V_p * X_p + V_q * X_q) % n
    return m

if __name__ == '__main__':
    start = time.time()

    if len(sys.argv) > 2:
        c = read_message(sys.argv[1])
        c = int(c)
    else:
        print("Usage: python3 decrypt.py <ciphertext_file> <plaintext_file>")
        exit(1)
    
    n, d = read_key("private_key")

    p, q = read_primes()
    
    m = decrypt(c, d, n, p, q)

    m = int_to_string(m)
    
    write_message(m, sys.argv[2])

    print("--- %s ms ---" % ((time.time() - start) * 1000))