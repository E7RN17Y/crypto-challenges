import pyperclip

# Encryption algorithm!
def encrypt(key, message):
    cypherText = [''] * 8
    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            cypherText[column] += message[currentIndex]
            currentIndex+=key 
