from Crypto.Util.number import long_to_bytes

# La chaîne de caractères hexadécimale à décoder
hex_str = "127739306028321100971803338843291053714892708270088284311840537009930335101"

# Convertir la chaîne de caractères hexadécimale en un entier
num = int(hex_str)

# Convertir l'entier en bytes
decoded_bytes = long_to_bytes(num)

# Afficher le résultat
print("Decoded bytes:", decoded_bytes)
print("Decoded string:", decoded_bytes.decode('utf-8', errors='ignore'))