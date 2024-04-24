import sys
import base64

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")


hexval= '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
hex2bin = bytes.fromhex(hexval)
bin2base64= base64.b64encode(hex2bin)
print(bin2base64)
