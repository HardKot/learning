def encryption(message,key):
    cryptionmessage = ""
    for char in message:
        code = ord(char)
        if code + key <= 256 :
            newchar = code + key
        else:
            newchar = code + key - 256
        cryptionmessage += chr(newchar)
    return cryptionmessage

def decryption(cryptionmessage,key):
    message = ""
    for char in cryptionmessage:
        code = ord(char)
        if code - key >= 0 :
            newchar = code - key
        else:
            newchar = 256 - (key - code)
        message += chr(newchar)
    return message