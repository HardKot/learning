import random
def encryption(message, key, table=None):
    cryptomessage = ""
    key *= len(message) // len(key) + 1
    for i, j in enumerate(message):
        code = (ord(j) + ord(key[i])) % 26
        if table:
            cryptomessage += table[code]
        else:
            cryptomessage += chr(code + 65)
    return cryptomessage

def decryption(cryptomessage, key, table=None):
    message = ""
    key *= len(cryptomessage) // len(key) + 1
    for i, j in enumerate(cryptomessage):
        if table:
            code = (table.index(j) - ord(key[i]) - 65) % 26 
        else:
            code = (ord(j) + ord(key[i])) % 26
        message += chr(code + 65)
    return message

def createtable():
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    table = []
    for i in range(26):
        char = random.randrange(0, 26 - i, 1)
        table.append(abc[char])
        abc = abc[:char] + abc[char + 1:]
    return table
