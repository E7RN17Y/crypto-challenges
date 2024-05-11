import sys

def gcd(a, b):return b if a%b == 0 else gcd(b,a%b)

if __name__ == '__main__':
    args = sys.argv[1:]
    if(len(args) == 2):
        val = gcd(int(float(args[0])), int(float(args[1])))
        print(val)
        