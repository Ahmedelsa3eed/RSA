from cryptography.hazmat.primitives.asymmetric import rsa
from Crypto.Util import number
from FindMI import MI
from RSAKeyUtil import *
import sys
import time


def keygen(num_of_bits_desired=1024):
    bits = num_of_bits_desired
    
    # Chose the public exponent as 65537
    e = 65537
    
    # Generate two different primes p and q
    p = q = 2
    while p == q or (p % e == 1) or (q % e == 1):
        p = number.getPrime(bits)
        q = number.getPrime(bits)

    # Calculate the modulus n = p * q
    n = p * q

    # Calculate the totient phi(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Calculate the private exponent d = e^-1 mod phi(n)
    d = MI(e, phi_n)

    # Convert to RSA key object
    private_key = rsa.generate_private_key(
        public_exponent=e,
        key_size=bits
    )
    public_key = private_key.public_key()
    
    save_public_key_to_file(public_key, "public_key.pem")
    save_private_key_to_file(private_key, "private_key.pem")
    
    return public_key, private_key


if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) > 1:
        keygen(int(sys.argv[1]))
    else:
        keygen()
    print("--- %s seconds ---" % (time.time() - start))
