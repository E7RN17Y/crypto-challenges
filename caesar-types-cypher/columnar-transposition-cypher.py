import pyperclip

# Encryption algorithm!!
def encrypt(key, message):
    print('message length', len(message))
    if isinstance(key,int):
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
    

def decryption(key, message):
    total_length = len(message)
    pre_last_parts = key - (round(len(message) / key) * key - len(message))
    print("pre",pre_last_parts)
    # each_parts = round(len(message) / key)
    result = ['']*pre_last_parts
    start = 0
    for i in range(pre_last_parts):
        result[i]=message[start:start+each_parts]
        start += each_parts

    if pre_last_parts != key:
        length = round((len(message) - start)/(key - pre_last_parts))
        for j in range((key - pre_last_parts)):
            result.append(message[start:start+length])
            start+=length

    plaintext=['']*each_parts

    for o in range(each_parts):
        for j in range(key):
            try:
                plaintext[o]+=result[j][o]
            except: pass
            

    return ''.join(plaintext)
 
if __name__ == '__main__':
    print(encrypt(8,'Hello world...da'))
    # print("____decrypt____")
    print(decryption(8,encrypt(8,'Hello world...da')))