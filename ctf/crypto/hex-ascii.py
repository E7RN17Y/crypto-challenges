

# hex_str = r'\x31\x5a\x5f\x34\x61\x5a\x5a\x79\x5f\x49\x5f'

# clean_hex_str = hex_str.replace('\\x', '')

# ascii_str = bytes.fromhex(clean_hex_str).decode('ascii')

# print(ascii_str)

# Given bytes object
byte_string = b'\xd5\xf3\x9d\x9a\xb4}\r\xc7Zq\xea\t\xdd\xfd\xf6\xf0\xeew_\x844\x05\xac\x8b\xc87u\x80\xda\xc1\xb3U'

# Convert bytes object to hexadecimal representation
hex_string = byte_string.hex()

print("Hexadecimal representation:", hex_string)
