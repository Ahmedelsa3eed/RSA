from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from RSAKeyUtil import *
import sys
import time

def decrypt_message(private_key_file, ciphertext):
    private_key = load_privatekey_from_file(private_key_file)
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()


if __name__ == '__main__':
    start = time.time()
    private_key_file = "private_key.pem"

    if len(sys.argv) > 2:
        ciphertext = open(sys.argv[1], 'rb').read()
    else:
        print("Usage: python3 decrypt.py <ciphertext_file> <plaintext_file>")
        exit(1)
    
    plaintext = decrypt_message(private_key_file, ciphertext)

    with open(sys.argv[2], "w") as file:
        file.write(plaintext)
    
    print(f"Decryption complete. Plaintext written to file: {sys.argv[2]}")
    print("--- %s seconds ---" % (time.time() - start))