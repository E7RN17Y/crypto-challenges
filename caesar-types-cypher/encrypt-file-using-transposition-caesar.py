from columnartranspositioncypher import encrypt, decryption
import os, sys

def main():
    mode = 'decrypt'

    fileInputName= 'frankenstein.txt' if mode == 'encrypt' else 'encrypted-outputfile.txt'

    if not os.path.exists(fileInputName):
        print('File doesn\'t exist')
        sys.exit()

    file = open(fileInputName, 'r', encoding= 'utf-8' if mode =='encrypt' else 'windows-1252')
    content = file.read()
    file.close()
    if mode ==  'encrypt':
        encrypted = encrypt(10, content)
        outputFile = open('encrypted-outputfile.txt','w')
        outputFile.write(encrypted)
    else:
        decrypted= decryption(10,content)
        outputFile = open('decryption-outputfile.txt','w',  encoding='utf-8')
        outputFile.write(decrypted)



if __name__ == '__main__':
    main()
