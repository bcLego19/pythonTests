

def caesar_cipher(text, key, encrypt = True):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    translation_table = str.maketrans(shifted_alphabet, alphabet)
    if not encrypt:
        translation_table = str.maketrans(shifted_alphabet, alphabet)
    return text.translate(translation_table)

#example of how to use (let key be 5)
text = "This is a message to encode!"
shiftKey = 5
encrypted_text = caesar_cipher(text, shiftKey)
print(encrypted_text)

#example of how to decrypt
decrypted_text = caesar_cipher(text, shiftKey, encrypt=False)
print(decrypted_text)