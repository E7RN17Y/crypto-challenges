import sys


if sys.version_info.major == 2:
    print("You are using python version 2 which is no more supported.Please upgrade to python 3")

hexvalue= '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
hex2bin= bytes.fromhex(hexvalue)

print(hex2bin)