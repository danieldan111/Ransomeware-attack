from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

import socket
import ssl


IV = b'4\xf4j\xfa\xcf\xcc\x00\xf4K\xf1\xad\xa8G\x92(\x81'
secret = b'S+\xc7H\xba\xdd\x19\x80HS\xd6\xae\x8a\xa9x\xceg\xa3\xb8\xe5H\x0f\xd9%\xed\xc6\x81r.Z\xf1E'

def encrypet_file(key, filepath):
    def encrypet_text(text):
        cipher = Cipher(algorithms.AES(key), modes.CBC(IV))
        encryptor = cipher.encryptor()
        padded_payload = text + b' ' * (16 - len(text) % 16) 
        ciphertext = encryptor.update(padded_payload) + encryptor.finalize()

        return ciphertext
    

    with open(filepath, "rb") as file:
        file_data = file.read()
    

    with open(filepath, "r+") as file:
        file.truncate()
    

    with open(filepath, "wb") as file:
        file.write(encrypet_text(file_data))

def decrypet_file(key, filepath):   
    def decrypet_text(ciphertext):
        cipher = Cipher(algorithms.AES(key), modes.CBC(IV))
        decryptor = cipher.decryptor()
        decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

        return decrypted_text
    
    with open(filepath, "rb") as file:
        decrypet_file_data = decrypet_text(file.read())

    with open(filepath, "r+") as file:
        file.truncate()    

    with open(filepath, "wb") as file:
        file.write(decrypet_file_data)

# context = ssl.create_default_context()

# encrypet_file(secret, "file1.txt")
decrypet_file(secret, "file1.txt")

def main():
    pass