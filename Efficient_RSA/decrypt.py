import rsa
from RSAKeyUtil import *
import sys
import time

def decrypt_message(ciphertext):
    with open("../private_key.pem", "rb") as f:
        private_key_data = f.read()
    private_key = rsa.PrivateKey.load_pkcs1(private_key_data)
    plaintext = rsa.decrypt(ciphertext, private_key)
    return plaintext.decode()


if __name__ == '__main__':
    start = time.time()

    if len(sys.argv) > 2:
        ciphertext = open(sys.argv[1], 'rb').read()
    else:
        print("Usage: python3 decrypt.py <ciphertext_file> <plaintext_file>")
        exit(1)
    
    plaintext = decrypt_message(ciphertext)

    with open(sys.argv[2], "w") as file:
        file.write(plaintext)
    
    print(f"Decryption complete. Plaintext written to file: {sys.argv[2]}")
    print("--- %s seconds ---" % (time.time() - start))