from pwn import xor


label=b"label"

flag = "".join([ chr(xor(i,13)) for i in label])

print(flag)