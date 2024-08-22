import pyperclip

# Encryption algorithm!!
def encrypt(key, message):
    if key is isinstance(int):
        pass
    else:
        key = int(key)

    cypherText = [''] * key

    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            cypherText[column] += message[currentIndex]
            currentIndex+=key
