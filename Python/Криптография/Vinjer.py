def encryption(message, key):
    cryptomessage = ""
    key *= len(message) // len(key) + 1
    for i, j in enumerate(message):
        code = (ord(j) + ord(key[i])) % 26  + 65
        cryptomessage += chr(code)
    return cryptomessage

def decryption(cryptomessage, key):
    message = ""
    key *= len(message) // len(key) + 1
    for i, j in enumerate(cryptomessage):
        code = (ord(j) - ord(key[i])) % 26 + 65
        message += chr(code)
    return message
