def parsermessage(text):
    words = []
    word = ''
    for char in text:
        if char == " " or char == '.': # Привести к более красивому виду через строки
            if not words.count(word):
                 words.append(word)
            continue
        word += char
    return words

def analysis(words,dicts):
    # собираем рабочий словарик. Слова длинной в 2-3 символа
    workword = []
    for word in words:
        if len(word) == 3 or len(word) == 2:
            workword.append(word)
    
    # Ищим похожие слова в рабочем словаре, с помощью алгоритва сравнения

    