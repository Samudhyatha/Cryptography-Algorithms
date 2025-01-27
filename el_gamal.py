import random

def modular_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def elgamal_encrypt(plaintext, p, e1, e2):
    r = random.randint(1, p - 1)
    c1 = modular_exponentiation(e1, r, p)
    c2 = [(ord(char) * modular_exponentiation(e2, r, p)) % p for char in plaintext]
    return c1, c2

def elgamal_decrypt(c1, c2, d, p):
    s = modular_exponentiation(c1, d, p)
    s_inv = mod_inverse(s, p)
    plaintext = ''.join([chr((char * s_inv) % p) for char in c2])
    return plaintext

# Example usage
if _name_ == "_main_":
    p = 467  # Large prime
    e1 = 2   # Primitive root of p
    d = random.randint(1, p - 2)
    e2 = modular_exponentiation(e1, d, p)

    plaintext = "HELLO"
    c1, c2 = elgamal_encrypt(plaintext, p, e1, e2)
    decrypted = elgamal_decrypt(c1, c2, d, p)

    print(f"Public Key (p, e1, e2): ({p}, {e1}, {e2})")
    print(f"Private Key (d): {d}")
    print(f"Ciphertext: (c1={c1}, c2={c2})")
    print(f"Decrypted: {decrypted}")