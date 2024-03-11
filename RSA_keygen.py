from PrimeGenerator import PrimeGenerator
from FindMI import MI


def write_primes(p, q):
    with open("primes", "w") as file:
        file.write(f"{p}\n{q}")

def keygen():
    num_of_bits_desired = 64
    e = 65537        # 4. Select the public exponent e such that 𝑔𝑐𝑑(𝑒, 𝜙(𝑛)) = 1

    # 1. Generate two different primes 𝑝 and 𝑞
    p = q = 2
    while p == q or (p % e == 1) or (q % e == 1):
        generator = PrimeGenerator( bits = num_of_bits_desired )
        p = generator.findPrime()
        q = generator.findPrime()
    write_primes(p, q)

    # 2. Calculate the modulus 𝑛 = 𝑝 × 𝑞
    n = p * q

    # 3. Calculate the totient 𝜙(𝑛) = (𝑝 − 1) × (𝑞 − 1)
    phi_n = (p - 1) * (q - 1)

    # 5. Calculate the private exponent d = e^-1 mod 𝜙(𝑛)
    d = MI(e, phi_n)
    if not d:
        print("[Error] can't compute private exponent (d)")
        exit(1)

    print(f"public key [n, e]: [{n}, {e}]")
    print(f"private key [n, d]: [{n}, {d}]")

    # Write the public and private keys to output files
    with open("id_rsa.pub", "w") as file:
        file.write(f"{n}\n{e}")

    with open("id_rsa", "w") as file:
        file.write(f"{n}\n{d}")

if __name__ == '__main__':
    keygen()