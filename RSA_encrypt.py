def read_publickey():
    # make sure the file id_rsa.pub exists
    try:
        file = open('id_rsa.pub', 'r')
    except FileNotFoundError:
        print("[Error] id_rsa.pub not found")
        exit(1)
    n = int(file.readline())
    e = int(file.readline())
    print(f"public key [n, e]: [{n}, {e}]")
    return n, e

def encrypt(m, e, n):
    c = pow(m, e, n)
    return c

if __name__ == '__main__':
    # read plaintext message as string then convert to integer
    m = input("Enter the plaintext message: ")
    m = int.from_bytes(m.encode(), byteorder='big')
    print("Converted message to integer: ", m)
    
    # read public key
    n, e = read_publickey()
    
    # encrypt the message   
    c = encrypt(m, e, n)
    print(f"Ciphertext: {c}")
    
    # write the ciphertext to a file
    with open("encrypted_message", "w") as file:
        file.write(str(c))