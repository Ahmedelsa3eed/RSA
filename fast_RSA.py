from Crypto.Util import number

def keygen():
    num_of_bits_desired = 64
    
    # Chose the public exponent as 65537
    e = 65537
    
    # Generate two different primes p and q
    p = q = 2
    while p == q or (p % e == 1) or (q % e == 1):
        p = number.getPrime(num_of_bits_desired)
        q = number.getPrime(num_of_bits_desired)

    # Calculate the modulus n = p * q
    n = p * q

    # Calculate the totient phi(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)

    # Calculate the private exponent d = e^-1 mod phi(n)
    d = number.inverse(e, phi_n)

    # Write the public and private keys to output files
    with open("id_rsa_2.pub", "w") as file:
        file.write(f"{n}\n{e}")
    
    with open("id_rsa_2", "w") as file:
        file.write(f"{n}\n{d}")
    
    return n, e, d, p, q


def encrypt(m, e, n):
    c = pow(m, e, n)
    return c

def decrypt(c, d, n, p, q):
    # use the chinese remainder theorem to speed up the calculation
    V_p = pow(c, d, p)
    V_q = pow(c, d, q)

    X_p = q * number.inverse(q, p)
    X_q = p * number.inverse(p, q)

    m = (V_p * X_p + V_q * X_q) % n
    return m

if __name__ == '__main__':
    # read plaintext message as string then convert to integer
    m = input("Enter the plaintext message: ")
    m = int.from_bytes(m.encode(), byteorder='big')
    print("Converted message to integer: ", m)
    
    # generate public and private keys
    n, e, d, p, q = keygen()
    
    # encrypt the message   
    c = encrypt(m, e, n)
    print(f"Ciphertext: {c}")
    
    # write the ciphertext to a file
    with open("encrypted_message_2", "w") as file:
        file.write(str(c))
    
    # decrypt the message
    m = decrypt(c, d, n, p, q)
    print("Decrypted message: ", m)
    
    # convert the decrypted message back to string
    m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big')
    m = m.decode()
    print("Decrypted message as string: ", m)
    
    # write the decrypted message to a file
    with open("decrypted_message_2", "w") as file:
        file.write(m)
    
    print("The public key [n, e] is: ", [n, e])
    print("The private key [n, d] is: ", [n, d])
    print("The primes p and q are: ", [p, q])