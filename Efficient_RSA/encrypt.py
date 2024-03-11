from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from RSAKeyUtil import *
import sys
import time

def encrypt_message(public_key_file, message):
    public_key = load_publickey_from_file(public_key_file)
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


if __name__ == '__main__':
    start = time.time()
    public_key_file = "public_key.pem"
    
    if len(sys.argv) > 2:
        plaintext = open(sys.argv[1], 'r').read().encode()
    else:
        print("Usage: python3 encrypt.py <plaintext_file> <ciphertext_file>")
        exit(1)
    
    ciphertext = encrypt_message(public_key_file, plaintext)

    with open(sys.argv[2], "wb") as file:
        file.write(ciphertext)
    
    print(f"Encryption complete. Ciphertext written to file: {sys.argv[2]}")
    print("--- %s seconds ---" % (time.time() - start))