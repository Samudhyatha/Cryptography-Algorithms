def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return ''.join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encrypt(text, key):
    encrypted = []
    for i in range(len(text)):
        char = (ord(text[i].upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
        encrypted.append(chr(char + ord('A')))
    return ''.join(encrypted)

def vigenere_decrypt(cipher, key):
    decrypted = []
    for i in range(len(cipher)):
        char = (ord(cipher[i]) - ord(key[i]) + 26) % 26
        decrypted.append(chr(char + ord('A')))
    return ''.join(decrypted)

# Example usage
if  __name__ == "_main_":
    text = "HELLO"
    key = "KEY"
    key = generate_key(text, key)
    encrypted = vigenere_encrypt(text, key)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {vigenere_decrypt(encrypted, key)}")