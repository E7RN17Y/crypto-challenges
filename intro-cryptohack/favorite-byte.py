from pwn import xor

hex2bytes= bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(0,256):
    try:
        flag= "".join([xor(j,i).decode('utf-8')  for j in hex2bytes])
        if flag.startswith('crypto{'):
            print(flag,  '\n')
            break
    except:
        pass
