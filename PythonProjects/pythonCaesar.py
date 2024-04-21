

def caesar_cipher(text, key, encrypt = True):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    if not encrypt:
        translation_table = str.maketrans(shifted_alphabet, alphabet)
    return text.translate(translation_table)

def encrypt_file(input_file, key):
    with open(input_file, "r") as file:
        text = file.read()
    encrypted_text = caesar_cipher(text, key)
    with open(f"{input_file}_encrypted.txt", 'w') as file:
        file.write(encrypted_text)

def decrypt_file(input_file, key):
    with open(input_file, "r") as file:
        text = file.read()
    encrypted_text = caesar_cipher(text, key, encrypt=False)
    with open(f"{input_file}_decrypted.txt", 'w') as file:
        file.write(encrypted_text)

#example of how to use (let key be 5)
text = "This is a message to encode!"
shiftKey = 5
encrypted_text = caesar_cipher(text, shiftKey)
print(encrypted_text)

#example of how to decrypt
decrypted_text = caesar_cipher(encrypted_text, shiftKey, encrypt=False)
print(decrypted_text)

#example of file encryption (let key be 5)
filename = 'C:\\Users\\Conner Batson\\Documents\\Python\\PythonProjects\\caesar.txt'
encrypt_file(filename, shiftKey)

with open(f"{filename}_encrypted.txt", 'r') as file:
    file.read()

filename2 = f"{filename}_encrypted.txt"
decrypt_file(filename2, shiftKey)

with open(f"{filename2}_decrypted.txt", 'r') as file:
    file.read()
