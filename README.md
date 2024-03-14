# RSA Encryption/Decryption Implementation

## Directory Stucture
```
└── 📁RSA
    └── .gitignore
    └── 📁Basic_RSA
        └── FindMI.py
        └── PrimeGenerator.py
        └── RSAKeyUtil.py
        └── RSA_decrypt.py
        └── RSA_encrypt.py
        └── RSA_keygen.py
    └── 📁Efficient_RSA
        └── FindMI.py
        └── RSAKeyUtil.py
        └── decrypt.py
        └── encrypt.py
        └── keygen.py
```

## Install required packages for part 2 (Efficient_RSA)
```bash
pip install rsa pycryptodome
```
## User Guide
### Basic RSA
#### Key Generation
```bash
cd Basic_RSA
python RSA_keygen.py [bits]
```
Replace ``[bits]`` with the desired key length in bits. If you don't provide any value, it defaults to 2048 bits.
#### Encryption
```bash
python RSA_encrypt.py [plaintext_file] [ciphertext_file]
```
Replace ``[plaintext_file]`` with the path to the file containing the plaintext and ``[ciphertext_file]`` with the path to the file where the ciphertext will be stored.
#### Decryption
```bash
python RSA_decrypt.py [ciphertext_file] [plaintext_file]
```
Replace ``[ciphertext_file]`` with the path to the file containing the ciphertext and ``[plaintext_file]`` with the path to the file where the plaintext will be stored.

### Efficient RSA
The usage is like Basic_RSA