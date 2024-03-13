from RSAKeyUtil import *
import time
import sys


def encrypt(m, e, n) -> int:
    c = pow(m, e, n)
    return c

if __name__ == '__main__':
    start = time.time()
    
    if len(sys.argv) > 2:
        plaintext = read_message(sys.argv[1])
        plaintext = string_to_int(plaintext)
    else:
        print("Usage: python3 encrypt.py <plaintext_file> <ciphertext_file>")
        exit(1)
    
    n, e = read_key("public_key")
    
    ciphertext = encrypt(plaintext, e, n)
    print("ciphertext: ", ciphertext)
    
    write_message(str(ciphertext), sys.argv[2])
    
    print("--- %s ms ---" % ((time.time() - start) * 1000))