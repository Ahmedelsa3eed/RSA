from PrimeGenerator import PrimeGenerator
from FindMI import MI
from RSAKeyUtil import *
import time
import sys


def keygen(bits=2048):
    # 4. Select the public exponent e such that 𝑔𝑐𝑑(𝑒, 𝜙(𝑛)) = 1
    e = 65537

    # 1. Generate two different primes 𝑝 and 𝑞
    p = q = 2
    while p == q or (p % e == 1) or (q % e == 1):
        generator = PrimeGenerator( bits = bits )
        p = generator.findPrime()
        q = generator.findPrime()
    write_primes(p, q)

    # 2. Calculate the modulus 𝑛 = 𝑝 × 𝑞
    n = p * q

    # 3. Calculate the totient 𝜙(𝑛) = (𝑝 − 1) × (𝑞 − 1)
    phi_n = (p - 1) * (q - 1)

    # 5. Calculate the private exponent d = e^-1 mod 𝜙(𝑛)
    d = MI(e, phi_n)

    # Write the public and private keys to output files
    write_key("./public_key", n, e)
    write_key("./private_key", n, d)


if __name__ == '__main__':
    start = time.time()
    
    if len(sys.argv) > 1:
        keygen(int(sys.argv[1]))
    else:
        keygen()
    
    print("--- %s ms ---" % ((time.time() - start) * 1000))