
# Crypto Hack  Registration Challenges
# Make use of roman emperor decipher

cipher = 'ZDRXV ARTBVK GRKTY GRTK'

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

result=''
# define the shift range
for j in range(0,30):
    for i in cipher.split():
            result +=roman_emperor_decipher(i, j) + ' '
    print("shift:%d,result="%(j),result)
    result=""

