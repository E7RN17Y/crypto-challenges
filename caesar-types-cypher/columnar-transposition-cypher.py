import pyperclip

# Encryption algorithm!!
def encrypt(key, message):
    if key is isinstance(int):
        pass
    else:
        key = int(key)

    cipherText = [''] * key

    for column in range(key):
        currentIndex = column
        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex+=key
    return ''.join(cipherText)


if __name__ == '__main__':
    encrypt(8,'Common sense is not so common.')