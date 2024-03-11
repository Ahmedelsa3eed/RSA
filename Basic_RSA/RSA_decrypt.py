from FindMI import MI
from RSAKeyUtil import *
import time

def decrypt(c, d, n, p, q):
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
    # read ciphertext as integer
    c = read_message("encrypted_message")
    
    # read private key
    n, d = read_key("private_key")

    # read primes
    p, q = read_primes()
    
    # decrypt the message
    m = decrypt(c, d, n, p, q)
    
    # convert the decrypted message to string
    m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()
    print("Decrypted message as string: ", m)
    
    write_message(m, "decrypted_message")

    print("--- %s ms ---" % ((time.time() - start) * 1000))