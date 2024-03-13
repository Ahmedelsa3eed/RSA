import rsa
from Crypto.Util import number
from FindMI import MI
from RSAKeyUtil import *
import sys
import time


def keygen(bits=1024):
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

    public_key = rsa.PublicKey(n, e)
    private_key = rsa.PrivateKey(n, e, d, p, q)

    # save the keys to files
    with open("public_key.pem", "wb") as f:
        f.write(public_key.save_pkcs1())

    with open("private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1())

if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) > 1:
        keygen(int(sys.argv[1]))
    else:
        keygen()
    print("--- %s seconds ---" % (time.time() - start))
