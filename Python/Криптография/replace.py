def encryption(message,keys):
    cryptomessage = ""
    for char in message:
        for key in keys:
            if key == char:
                cryptomessage += keys[key]
                break
    return cryptomessage

def decryption(cryptomessage,keys):
    message = ""
    for code in cryptomessage:
        for key in keys:
            if keys[key] == code:
                message += key
                break
    return message