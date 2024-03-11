from FindMI import MI

def read_ciphertext():
    # make sure the file encrypted_message exists
    try:
        file = open('encrypted_message', 'r')
    except FileNotFoundError:
        print("[Error] encrypted_message not found")
        exit(1)
    c = int(file.readline())
    print("Ciphertext: ", c)
    return c

def read_privatekey():
    # make sure the file id_rsa exists
    try:
        file = open('id_rsa', 'r')
    except FileNotFoundError:
        print("[Error] id_rsa not found")
        exit(1)
    n = int(file.readline())
    d = int(file.readline())
    print(f"private key [n, d]: [{n}, {d}]")
    return n, d

def read_primes():
    # make sure the file primes exists
    try:
        file = open('primes', 'r')
    except FileNotFoundError:
        print("[Error] primes not found")
        exit(1)
    p = int(file.readline())
    q = int(file.readline())
    return p, q

def decrypt(c, d, n, p, q):
    # use the chinese remainder theorem to speed up the calculation
    V_p = pow(c, d, p)
    V_q = pow(c, d, q)

    X_p = q * MI(q, p)
    X_q = p * MI(p, q)

    m = (V_p * X_p + V_q * X_q) % n
    return m

if __name__ == '__main__':
    # read ciphertext as integer
    c = read_ciphertext()
    
    # read private key
    n, d = read_privatekey()

    # read primes
    p, q = read_primes()
    
    # decrypt the message
    m = decrypt(c, d, n, p, q)
    print("Decrypted message: ", m)
    
    # convert the decrypted message to string
    m = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode()
    print("Decrypted message as string: ", m)
    
    # write the decrypted message to a file
    with open("decrypted_message", "w") as file:
        file.write(m)