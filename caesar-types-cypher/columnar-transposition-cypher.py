import pyperclip
from math import ceil

# Encryption algorithm!!
def encrypt(key, message):
    if isinstance(key,int):
        pass
    else:
        key = int(key)

    cipherText = [''] * key

    for column in range(key):
        currentIndex = column
        # print(cipherText,'\n')
        while currentIndex < len(message):
            cipherText[column] += message[currentIndex]
            currentIndex+=key
    return ''.join(cipherText)
    

def decryption(key, message):
    total_length = len(message)
    pre_last_parts = key - (ceil(len(message) / key) * key - len(message))
    each_parts = ceil(len(message) / key)
    result = ['']*pre_last_parts
    start = 0
    # re-rarrange messages
    for i in range(pre_last_parts):
        result[i]=message[start:start+each_parts]
        start += each_parts
    if pre_last_parts != key:
        length = round((len(message) - start)/(key - pre_last_parts))
        for j in range((key - pre_last_parts)):
            result.append(message[start:start+length])
            start+=length

    plaintext=['']*each_parts
    # decrypt
    for o in range(each_parts):
        for j in range(key):
            try:
                plaintext[o]+=result[j][o]
            except: pass
            

    return ''.join(plaintext)
 
if __name__ == '__main__':
    print("Encrypted value:",encrypt(8,'Hello world...damn'))
    # print("____decrypt____")
    print("Decrypted Value:",decryption(8,encrypt(8,'Hello world...damn')))