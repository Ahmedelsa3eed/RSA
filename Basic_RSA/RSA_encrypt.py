from RSAKeyUtil import *
import time
import sys


def encrypt(m, e, n):
    c = pow(m, e, n)
    return c

if __name__ == '__main__':
    start = time.time()
    
    if len(sys.argv) > 2:
        plaintext = open(sys.argv[1], 'r').read().encode()
    else:
        print("Usage: python3 encrypt.py <plaintext_file> <ciphertext_file>")
        exit(1)
    
    plaintext = int.from_bytes(plaintext, byteorder='big')
    
    n, e = read_key("public_key")
    
    ciphertext = encrypt(plaintext, e, n)
    
    write_message(ciphertext, "ciphertext")
    
    print("--- %s ms ---" % ((time.time() - start) * 1000))