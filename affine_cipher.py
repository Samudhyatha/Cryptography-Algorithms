# affine_cipher.py
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(text, a, b, m=26):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    encrypted = ''.join(
        chr((a * (ord(char) - ord('A')) + b) % m + ord('A'))
        if char.isalpha() else char for char in text.upper()
    )
    return encrypted

def affine_decrypt(cipher, a, b, m=26):
    a_inv = mod_inverse(a, m)
    if not a_inv:
        raise ValueError("Modular inverse doesn't exist.")
    decrypted = ''.join(
        chr((a_inv * (ord(char) - ord('A') - b)) % m + ord('A'))
        if char.isalpha() else char for char in cipher.upper()
    )
    return decrypted

# Example usage
if __name__ == "_main_":
    plaintext = "HELLO"
    a, b = 5, 8  # Encryption keys
    ciphertext = affine_encrypt(plaintext, a, b)
    print(f"Encrypted: {ciphertext}")
    print(f"Decrypted: {affine_decrypt(ciphertext, a, b)}")
