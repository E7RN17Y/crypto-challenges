
# Crypto Hack  Registration Challenges
# Make use of roman emperor decipher

cipher = 'LJAKXW EJURM HXDCQ MXEN'

# def roman_emperor_cipher(cipher, shift):
#     crypted=""
#     for i in cipher:
#         val = (ord(i) + shift + 25)%90 + 65
#         while val > 90: val = val%90 + 64
#         crypted+=chr(val)
        
#     return crypted

def roman_emperor_decipher(cipher, shift):
    decrypted=""
    for i in cipher:
        val = (ord(i) - shift + 25)%90 + 65
        while val > 90: val = val%90 + 26
        decrypted+=chr(val)
    return decrypted

for i in cipher.split():
    for j in range(0,10):   
        print('cipher={} , shift={}, result='.format(i,j),roman_emperor_decipher(i, j), ' ')

