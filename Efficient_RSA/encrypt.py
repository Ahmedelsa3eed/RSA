import rsa
from RSAKeyUtil import *
import sys
import time

def encrypt_message(public_key_file, message):
    with open(public_key_file, "rb") as f:
        public_key_data = f.read()
    public_key = rsa.PublicKey.load_pkcs1(public_key_data)
    ciphertext = rsa.encrypt(message, public_key)
    return ciphertext


if __name__ == '__main__':
    start = time.time()
    public_key_file = "../public_key.pem"
    
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