def encryption(message, key):
    cryptomessage = ""
    key *= len(message) // len(key) + 1
    for i, j in enumerate(message):
        code = (ord(j) + ord(key[i]) - 64) % 126 + 31
        cryptomessage += str(code) + ' ' + chr(code)
    return cryptomessage

def decryption(cryptomessage, key):
    message = ""
    key *= len(message) // len(key) + 1
    for i, j in enumerate(cryptomessage):
        code = ord(j) - ord(key[i])
        message += str(code)
    return message

text = "HELLO"
key = "WORLD"

print(encryption(message=text,key=key))