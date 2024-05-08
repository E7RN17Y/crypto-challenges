import sys

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b,a%b)

if __name__ == '__main__':
    args = sys.argv[1:]
    if(len(args) == 2):
        val = gcd(int(float(args[0])), int(float(args[1])))
        print(val)
        